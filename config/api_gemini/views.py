from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
from django.conf import settings
import json

# Configurar a API do Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

@api_view(['POST'])
def chat_with_gemini(request):
    """
    Endpoint principal para interagir com o Gemini AI
    """
    try:
        # Verificar se a chave da API está configurada
        if not settings.GEMINI_API_KEY:
            return Response(
                {'error': 'Chave da API do Gemini não configurada'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Obter dados da requisição
        data = request.data
        message = data.get('message', '')
        
        if not message:
            return Response(
                {'error': 'Mensagem é obrigatória'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Configurar o modelo
        model = genai.GenerativeModel(settings.GEMINI_MODEL)
        
        # Gerar resposta
        response = model.generate_content(message)
        
        # Retornar resposta
        return Response({
            'message': message,
            'response': response.text,
            'status': 'success'
        })
        
    except Exception as e:
        return Response(
            {'error': f'Erro ao processar requisição: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def health_check(request):
    """
    Endpoint para verificar o status da API
    """
    return Response({
        'status': 'healthy',
        'service': 'EstudaAI Gemini API',
        'gemini_configured': bool(settings.GEMINI_API_KEY)
    })
