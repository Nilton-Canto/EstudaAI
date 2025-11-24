"""
Módulo de integração com Google Gemini AI.

Este módulo contém toda a lógica para geração de trilhas
usando a API do Google Gemini.
"""

import json
import logging
import os
from typing import Any, Dict, Optional

import google.generativeai as genai
from django.conf import settings
from django.contrib.auth import get_user_model

from .exceptions import GeminiAPIException, InvalidJSONResponseException

Usuario = get_user_model()
logger = logging.getLogger(__name__)


# Configurar a API do Gemini
try:
    # Tenta configurar usando settings ou variável de ambiente (abordagem híbrida)
    api_key = getattr(settings, "GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
    if api_key:
        genai.configure(api_key=api_key)
        logger.info("API do Gemini configurada com sucesso")
    else:
        logger.warning("Chave da API do Gemini não encontrada")
except Exception as e:
    logger.error(f"Erro ao configurar API do Gemini: {e}")


class GeminiService:
    """Serviço para interação com a API do Gemini."""

    def __init__(self):
        """Inicializa o serviço do Gemini."""
        # Verifica se a chave está configurada (pode ter sido via env var no configure acima)
        # Mas aqui verificamos settings.GEMINI_API_KEY explicitamente como no código original do HEAD
        # Ajustando para ser compatível com a configuração global
        if not getattr(settings, "GEMINI_API_KEY", None) and not os.getenv("GEMINI_API_KEY"):
             raise GeminiAPIException("Chave da API do Gemini não configurada")

        self.model = genai.GenerativeModel(settings.GEMINI_MODEL)

    def gerar_prompt_trilha(self, solicitacao, usuario_data=None):
        """
        Gera um prompt estruturado para criação de trilha de curso.

        Args:
            solicitacao (str): Solicitação do usuário
            usuario_data (dict): Dados do usuário para personalização

        Returns:
            str: Prompt formatado para o LLM
        """
        prompt_base = f"""
Você é um assistente especializado em educação que cria trilhas de aprendizado personalizadas.

SOLICITAÇÃO DO USUÁRIO: {solicitacao}

INSTRUÇÕES:
1. Crie uma trilha de aprendizado estruturada e progressiva
2. Divida o conteúdo em módulos lógicos e sequenciais
3. Para cada módulo, inclua tópicos específicos e recursos de estudo
4. Estime a duração de cada módulo
5. Sugira recursos práticos como projetos, exercícios ou atividades

FORMATO DE RESPOSTA (OBRIGATÓRIO JSON):
{{
    "titulo": "Título da Trilha de Aprendizado",
    "descricao": "Descrição geral da trilha e objetivos",
    "nivel": "Iniciante/Intermediário/Avançado",
    "duracao_total": "X semanas/meses",
    "modulos": [
        {{
            "numero": 1,
            "titulo": "Nome do Módulo",
            "descricao": "Descrição do que será aprendido",
            "duracao": "X semanas",
            "topicos": ["Tópico 1", "Tópico 2"],
            "recursos": [
                {{
                    "tipo": "video/livro/curso/artigo",
                    "titulo": "Nome do Recurso",
                    "descricao": "Breve descrição"
                }}
            ],
            "atividades_praticas": ["Atividade prática 1"]
        }}
    ],
    "projeto_final": "Descrição de um projeto integrador",
    "recursos_complementares": ["Recurso adicional 1"]
}}

IMPORTANTE: 
- Responda APENAS com o JSON válido, sem texto adicional
- Certifique-se de que todos os campos estão preenchidos
- A trilha deve ser prática e aplicável
"""

        if usuario_data:
            prompt_base += f"""

DADOS DO USUÁRIO PARA PERSONALIZAÇÃO:
- Curso: {usuario_data.get('curso', 'Não informado')}
- Universidade: {usuario_data.get('universidade', 'Não informada')}
- Ano de formatura: {usuario_data.get('ano_formatura', 'Não informado')}
- Idade: {usuario_data.get('idade', 'Não informada')}

Use essas informações para personalizar a trilha de acordo com o perfil do usuário.
"""

        return prompt_base

    def gerar_trilha_com_ia(self, solicitacao, usuario=None):
        """
        Gera uma trilha usando IA do Gemini.

        Args:
            solicitacao (str): Solicitação do usuário
            usuario (Usuario): Instância do usuário (opcional)

        Returns:
            dict: Trilha gerada em formato JSON

        Raises:
            GeminiAPIException: Se houver erro na API
            InvalidJSONResponseException: Se resposta não for JSON válido
        """
        logger.info(f"Gerando trilha para solicitação: {solicitacao[:100]}...")

        # Preparar dados do usuário
        usuario_data = None
        if usuario:
            usuario_data = {
                "curso": usuario.curso,
                "universidade": usuario.universidade,
                "ano_formatura": usuario.ano_formatura,
                "idade": usuario.idade,
            }
            logger.info(f"Personalizando para usuário: {usuario.username}")

        # Gerar prompt
        prompt = self.gerar_prompt_trilha(solicitacao, usuario_data)

        try:
            # Gerar resposta
            response = self.model.generate_content(prompt)
            logger.info("Trilha gerada com sucesso")

            # Parsear JSON
            trilha_json = self._parsear_resposta(response.text)

            return trilha_json

        except genai.types.BlockedPromptException as e:
            logger.error(f"Prompt bloqueado: {e}")
            raise GeminiAPIException(
                "Conteúdo bloqueado pelas políticas de segurança"
            )
        except genai.types.StopCandidateException as e:
            logger.error(f"Geração interrompida: {e}")
            raise GeminiAPIException("Geração de trilha foi interrompida")
        except Exception as e:
            logger.error(f"Erro ao gerar trilha: {str(e)}")
            raise GeminiAPIException(f"Erro ao gerar trilha: {str(e)}")

    def chat(self, mensagem):
        """
        Interage com o Gemini em modo chat.

        Args:
            mensagem (str): Mensagem do usuário

        Returns:
            str: Resposta do Gemini

        Raises:
            GeminiAPIException: Se houver erro na API
        """
        logger.info(f"Chat: {mensagem[:50]}...")

        try:
            response = self.model.generate_content(mensagem)
            logger.info("Resposta gerada com sucesso")
            return response.text

        except genai.types.BlockedPromptException:
            raise GeminiAPIException(
                "Conteúdo bloqueado pelas políticas de segurança"
            )
        except genai.types.StopCandidateException:
            raise GeminiAPIException("Geração de resposta foi interrompida")
        except Exception as e:
            raise GeminiAPIException(f"Erro no chat: {str(e)}")

    def _parsear_resposta(self, texto):
        """
        Parseia a resposta do Gemini removendo marcadores de código.

        Args:
            texto (str): Texto da resposta

        Returns:
            dict: JSON parseado

        Raises:
            InvalidJSONResponseException: Se JSON for inválido
        """
        try:
            # Limpar marcadores de código
            texto = texto.strip()
            if texto.startswith("```json"):
                texto = texto[7:]
            if texto.startswith("```"):
                texto = texto[3:]
            if texto.endswith("```"):
                texto = texto[:-3]
            texto = texto.strip()

            # Parsear JSON
            return json.loads(texto)

        except json.JSONDecodeError as e:
            logger.error(f"Erro ao parsear JSON: {e}")
            raise InvalidJSONResponseException(
                f"Resposta não é um JSON válido: {str(e)}"
            )

# ---------------------------------------------------------------------
# Funções auxiliares vindas da branch develop
# ---------------------------------------------------------------------

def configure_gemini() -> bool:
    """
    Configura o cliente da API Gemini usando a chave do settings ou ENV.
    """
    api_key = getattr(settings, "GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))

    if not api_key:
        logger.warning("GEMINI_API_KEY não encontrada.")
        return False

    try:
        genai.configure(api_key=api_key)
        logger.info("Gemini API configurada com sucesso.")
        return True
    except Exception as e:
        logger.exception(f"Erro ao configurar Gemini: {e}")
        return False


# Chama configuração ao importar (mantendo comportamento do develop)
CONFIGURED = configure_gemini()


def is_configured() -> bool:
    """Retorna True se a API estiver configurada."""
    return CONFIGURED


def get_model(model_name: Optional[str] = None):
    """
    Retorna o modelo configurado.
    """
    model = model_name or getattr(settings, "GEMINI_MODEL", None)

    if not model:
        raise RuntimeError("O GEMINI_MODEL não foi configurado no settings.")

    return genai.GenerativeModel(model)


def clean_json_text(text: str) -> str:
    """Remove fences ```json para permitir o parse."""
    text = text.strip()
    if text.startswith("```"):
        parts = text.split("```")
        if len(parts) >= 2:
            return parts[1].strip()
    return text


def generate_content(
    prompt: str, model_name: Optional[str] = None, **kwargs
) -> Dict[str, Any]:
    """
    Gera conteúdo usando o Gemini.
    """
    if not is_configured():
        raise RuntimeError("Gemini não configurado. Verifique GEMINI_API_KEY.")

    model = get_model(model_name)

    try:
        response = model.generate_content(prompt, **kwargs)
        text = getattr(response, "text", str(response))

        parsed_json = None
        try:
            parsed_json = json.loads(clean_json_text(text))
        except Exception:
            parsed_json = None

        return {
            "text": text,
            "json": parsed_json,
            "raw": response,
        }

    except Exception as e:
        logger.exception(f"Erro ao gerar conteúdo: {e}")
        raise
