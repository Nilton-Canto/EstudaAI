"""
Views para integração com Google Gemini AI.
"""

import logging

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .gemini import GeminiService
from .models import TrilhaCurso
from .serializers import TrilhaCursoSerializer

logger = logging.getLogger(__name__)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def gerar_trilha_curso(request):
    """
    Gera uma trilha de curso personalizada usando IA do Gemini.

    Espera um JSON com o campo 'solicitacao' contendo o pedido do usuário.
    Retorna a trilha gerada SEM salvar no banco (o salvamento é feito pelo formulário).
    """
    solicitacao = request.data.get("solicitacao", "").strip()

    if not solicitacao:
        return Response(
            {"erro": "A solicitação não pode estar vazia"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    logger.info(f"Gerando trilha para usuário {request.user.username}")

    try:
        # Instanciar serviço do Gemini
        gemini_service = GeminiService()

        # Gerar trilha com IA
        trilha_json = gemini_service.gerar_trilha_com_ia(
            solicitacao, usuario=request.user
        )

        # NÃO salvar no banco - apenas retornar o JSON
        # O salvamento será feito pelo formulário quando o usuário clicar em "Salvar Trilha"
        logger.info(f"Trilha gerada com sucesso para {request.user.username}")

        # Retornar o JSON diretamente
        return Response(trilha_json, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Erro ao gerar trilha: {str(e)}")
        return Response(
            {"erro": f"Erro ao gerar trilha: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def chat_com_gemini(request):
    """
    Endpoint para chat geral com o Gemini.

    Espera um JSON com o campo 'message'.
    Retorna a resposta do Gemini.
    """
    mensagem = request.data.get("message", "").strip()

    if not mensagem:
        return Response(
            {"erro": "A mensagem não pode estar vazia"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    logger.info(f"Chat com Gemini - usuário {request.user.username}")

    try:
        # Instanciar serviço
        gemini_service = GeminiService()

        # Enviar mensagem e obter resposta
        resposta = gemini_service.chat(mensagem)

        return Response({"response": resposta}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Erro no chat: {str(e)}")
        return Response(
            {"erro": f"Erro no chat: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def listar_trilhas_usuario(request):
    """
    Lista todas as trilhas de curso do usuário autenticado.
    """
    trilhas = TrilhaCurso.objects.filter(usuario=request.user, ativa=True)
    serializer = TrilhaCursoSerializer(trilhas, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def detalhe_trilha_curso(request, trilha_id):
    """
    Retorna os detalhes completos de uma trilha específica.
    """
    try:
        trilha = TrilhaCurso.objects.get(id=trilha_id, usuario=request.user)
        serializer = TrilhaCursoSerializer(trilha)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except TrilhaCurso.DoesNotExist:
        return Response(
            {"erro": "Trilha não encontrada"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deletar_trilha_curso(request, trilha_id):
    """
    Marca uma trilha como inativa (soft delete).
    """
    try:
        trilha = TrilhaCurso.objects.get(id=trilha_id, usuario=request.user)
        trilha.ativa = False
        trilha.save()

        return Response(
            {"mensagem": "Trilha removida com sucesso"},
            status=status.HTTP_200_OK,
        )

    except TrilhaCurso.DoesNotExist:
        return Response(
            {"erro": "Trilha não encontrada"}, status=status.HTTP_404_NOT_FOUND
        )


@api_view(["GET"])
def health_check(request):
    """
    Verifica o status da API.
    """
    return Response(
        {"status": "online", "servico": "API Gemini"}, status=status.HTTP_200_OK
    )


def test_api_page(request):
    """
    Renderiza página de teste da API.
    """
    return render(request, "api/test_gemini.html")
