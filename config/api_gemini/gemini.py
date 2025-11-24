# config/api/gemini.py
import os
import json
import logging
from typing import Optional, Dict, Any

import google.generativeai as genai
from django.conf import settings

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------
# 1. Configuração do Gemini (somente se houver chave no settings)
# ---------------------------------------------------------------------
def configure_gemini() -> bool:
    """
    Configura o cliente da API Gemini usando a chave do settings ou ENV.
    Não altera nada no projeto existente. Apenas fornece um módulo auxiliar.
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


# Chama configuração ao importar
CONFIGURED = configure_gemini()


def is_configured() -> bool:
    """Retorna True se a API estiver configurada."""
    return CONFIGURED


# ---------------------------------------------------------------------
# 2. Função utilitária para pegar o modelo correto
# ---------------------------------------------------------------------
def get_model(model_name: Optional[str] = None):
    """
    Retorna o modelo configurado.
    Não altera lógica existente no API Gemini original.
    """
    model = model_name or getattr(settings, "GEMINI_MODEL", None)

    if not model:
        raise RuntimeError("O GEMINI_MODEL não foi configurado no settings.")

    return genai.GenerativeModel(model)


# ---------------------------------------------------------------------
# 3. Função utilitária para remover ```json
# ---------------------------------------------------------------------
def clean_json_text(text: str) -> str:
    """Remove fences ```json para permitir o parse."""
    text = text.strip()
    if text.startswith("```"):
        parts = text.split("```")
        if len(parts) >= 2:
            return parts[1].strip()
    return text


# ---------------------------------------------------------------------
# 4. Função para chamar o LLM (auxiliar, não substitui nada existente)
# ---------------------------------------------------------------------
def generate_content(prompt: str, model_name: Optional[str] = None, **kwargs) -> Dict[str, Any]:
    """
    Gera conteúdo usando o Gemini.
    Não substitui implementações já existentes no projeto.
    Somente adiciona uma alternativa caso outras partes precisem.
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
