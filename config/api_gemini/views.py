from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
from django.conf import settings
import json
import logging
from .models import TrilhaCurso
from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()

# Configurar logging
logger = logging.getLogger(__name__)

# Configurar a API do Gemini
try:
    genai.configure(api_key=settings.GEMINI_API_KEY)
    logger.info("API do Gemini configurada com sucesso")
except Exception as e:
    logger.error(f"Erro ao configurar API do Gemini: {e}")

def gerar_prompt_trilha_curso(solicitacao_usuario, usuario_data=None):
    """
    Gera um prompt estruturado para criação de trilha de curso
    
    Args:
        solicitacao_usuario (str): Solicitação do usuário
        usuario_data (dict): Dados do usuário para personalização
    
    Returns:
        str: Prompt formatado para o LLM
    """
    prompt_base = f"""
Você é um assistente especializado em educação que cria trilhas de aprendizado personalizadas.

SOLICITAÇÃO DO USUÁRIO: {solicitacao_usuario}

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
            "topicos": [
                "Tópico 1",
                "Tópico 2",
                "Tópico 3"
            ],
            "recursos": [
                {{
                    "tipo": "video/livro/curso/artigo",
                    "titulo": "Nome do Recurso",
                    "descricao": "Breve descrição"
                }}
            ],
            "atividades_praticas": [
                "Atividade prática 1",
                "Projeto sugerido"
            ]
        }}
    ],
    "projeto_final": "Descrição de um projeto integrador",
    "recursos_complementares": [
        "Recurso adicional 1",
        "Recurso adicional 2"
    ]
}}

IMPORTANTE: 
- Responda APENAS com o JSON válido, sem texto adicional
- Certifique-se de que todos os campos estão preenchidos
- A trilha deve ser prática e aplicável
- Considere diferentes estilos de aprendizado
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

@api_view(['POST'])
def gerar_trilha_curso(request):
    """
    Endpoint para gerar trilha de curso personalizada baseada na solicitação do usuário
    """
    logger.info(f"Requisição de trilha de curso recebida: {request.method} {request.path}")
    
    try:
        # Verificar se a chave da API está configurada
        if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == 'test_key_for_verification':
            logger.error("Chave da API do Gemini não configurada")
            return Response(
                {'error': 'Chave da API do Gemini não configurada'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Obter dados da requisição
        data = request.data
        solicitacao = data.get('solicitacao', '')
        user_id = data.get('user_id', None)
        
        # Validação básica
        if not solicitacao.strip():
            logger.warning("Requisição sem solicitação de curso")
            return Response(
                {'error': 'Solicitação de curso é obrigatória'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        logger.info(f"Processando solicitação de trilha: {solicitacao[:100]}...")
        
        # Buscar dados do usuário se ID fornecido
        usuario_data = None
        usuario = None
        if user_id:
            try:
                usuario = User.objects.get(id=user_id)
                usuario_data = {
                    'curso': usuario.curso,
                    'universidade': usuario.universidade,
                    'ano_formatura': usuario.ano_formatura,
                    'idade': usuario.idade,
                }
                logger.info(f"Dados do usuário {usuario.username} carregados para personalização")
            except User.DoesNotExist:
                logger.warning(f"Usuário com ID {user_id} não encontrado")
        
        # Gerar prompt personalizado
        prompt = gerar_prompt_trilha_curso(solicitacao, usuario_data)
        
        # Configurar o modelo
        model = genai.GenerativeModel(settings.GEMINI_MODEL)
        
        # Gerar resposta
        response = model.generate_content(prompt)
        
        logger.info("Trilha gerada com sucesso pelo LLM")
        
        # Tentar parsear o JSON da resposta
        try:
            # Limpar a resposta removendo possíveis marcadores de código
            response_text = response.text.strip()
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.endswith('```'):
                response_text = response_text[:-3]
            response_text = response_text.strip()
            
            trilha_json = json.loads(response_text)
            logger.info("JSON da trilha parseado com sucesso")
            
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao parsear JSON da resposta: {e}")
            return Response(
                {'error': 'Erro ao processar resposta do LLM - JSON inválido'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Salvar trilha no banco de dados se usuário fornecido
        trilha_salva = None
        if usuario:
            try:
                trilha_salva = TrilhaCurso.objects.create(
                    usuario=usuario,
                    titulo=trilha_json.get('titulo', 'Trilha Personalizada'),
                    descricao=trilha_json.get('descricao', ''),
                    solicitacao_original=solicitacao,
                    conteudo_json=trilha_json
                )
                logger.info(f"Trilha salva no banco com ID {trilha_salva.id}")
            except Exception as e:
                logger.error(f"Erro ao salvar trilha no banco: {e}")
                # Continua sem falhar, apenas loga o erro
        
        # Preparar resposta
        response_data = {
            'solicitacao': solicitacao,
            'trilha': trilha_json,
            'status': 'success',
            'model_used': settings.GEMINI_MODEL,
            'personalizada': bool(usuario_data),
        }
        
        if trilha_salva:
            response_data['trilha_id'] = trilha_salva.id
            response_data['data_criacao'] = trilha_salva.data_criacao.isoformat()
        
        return Response(response_data)
        
    except genai.types.BlockedPromptException as e:
        logger.error(f"Prompt bloqueado: {e}")
        return Response(
            {'error': 'Conteúdo da solicitação foi bloqueado pelas políticas de segurança'},
            status=status.HTTP_400_BAD_REQUEST
        )
    except genai.types.StopCandidateException as e:
        logger.error(f"Geração interrompida: {e}")
        return Response(
            {'error': 'Geração de trilha foi interrompida'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    except Exception as e:
        logger.error(f"Erro ao processar requisição de trilha: {str(e)}")
        return Response(
            {'error': f'Erro ao processar requisição: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def listar_trilhas_usuario(request, user_id):
    """
    Endpoint para listar trilhas de um usuário específico
    """
    logger.info(f"Listando trilhas do usuário {user_id}")
    
    try:
        usuario = User.objects.get(id=user_id)
        trilhas = TrilhaCurso.objects.filter(usuario=usuario, ativa=True)
        
        trilhas_data = []
        for trilha in trilhas:
            trilhas_data.append({
                'id': trilha.id,
                'titulo': trilha.titulo,
                'descricao': trilha.descricao,
                'data_criacao': trilha.data_criacao.isoformat(),
                'conteudo': trilha.conteudo_json
            })
        
        return Response({
            'usuario': usuario.username,
            'total_trilhas': len(trilhas_data),
            'trilhas': trilhas_data
        })
        
    except User.DoesNotExist:
        return Response(
            {'error': 'Usuário não encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        logger.error(f"Erro ao listar trilhas: {str(e)}")
        return Response(
            {'error': f'Erro ao listar trilhas: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
def chat_with_gemini(request):
    """
    Endpoint principal para interagir com o Gemini AI
    """
    logger.info(f"Requisição recebida: {request.method} {request.path}")
    
    try:
        # Verificar se a chave da API está configurada
        if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == 'test_key_for_verification':
            logger.error("Chave da API do Gemini não configurada")
            return Response(
                {'error': 'Chave da API do Gemini não configurada'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Obter dados da requisição
        data = request.data
        message = data.get('message', '')
        
        if not message:
            logger.warning("Requisição sem mensagem")
            return Response(
                {'error': 'Mensagem é obrigatória'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        logger.info(f"Processando mensagem: {message[:50]}...")
        
        # Configurar o modelo
        model = genai.GenerativeModel(settings.GEMINI_MODEL)
        
        # Gerar resposta
        response = model.generate_content(message)
        
        logger.info("Resposta gerada com sucesso")
        
        # Retornar resposta
        return Response({
            'message': message,
            'response': response.text,
            'status': 'success',
            'model_used': settings.GEMINI_MODEL
        })
        
    except genai.types.BlockedPromptException as e:
        logger.error(f"Prompt bloqueado: {e}")
        return Response(
            {'error': 'Conteúdo da mensagem foi bloqueado pelas políticas de segurança'},
            status=status.HTTP_400_BAD_REQUEST
        )
    except genai.types.StopCandidateException as e:
        logger.error(f"Geração interrompida: {e}")
        return Response(
            {'error': 'Geração de resposta foi interrompida'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    except Exception as e:
        logger.error(f"Erro ao processar requisição: {str(e)}")
        return Response(
            {'error': f'Erro ao processar requisição: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def health_check(request):
    """
    Endpoint para verificar o status da API
    """
    logger.info("Health check solicitado")
    
    # Verificar se a API está configurada corretamente
    gemini_configured = bool(settings.GEMINI_API_KEY and settings.GEMINI_API_KEY != 'test_key_for_verification')
    
    return Response({
        'status': 'healthy',
        'service': 'EstudaAI Gemini API',
        'gemini_configured': gemini_configured,
        'model': settings.GEMINI_MODEL,
        'version': '1.0.0'
    })

def test_api_page(request):
    """
    Renderiza a página de teste da API
    """
    return render(request, 'api_gemini/test_api.html')
