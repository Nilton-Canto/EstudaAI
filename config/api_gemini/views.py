from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
from django.conf import settings
import json
import logging

# Configurar logging
logger = logging.getLogger(__name__)

# Configurar a API do Gemini
try:
    genai.configure(api_key=settings.GEMINI_API_KEY)
    logger.info("API do Gemini configurada com sucesso")
except Exception as e:
    logger.error(f"Erro ao configurar API do Gemini: {e}")

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
