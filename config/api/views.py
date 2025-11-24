"""
Views da API de trilhas e áreas.
"""

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import AreaInativaException, TrilhaLimitExceededException
from .models import Area, Trilha
from .serializers import AreaSerializer, TrilhaSerializer
from .services import AreaService, TrilhaService


# ==============================================================================
# ÁREAS
# ==============================================================================


class AreaListView(generics.ListAPIView):
    """Lista todas as áreas de conhecimento ativas."""

    serializer_class = AreaSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """Retorna apenas áreas ativas."""
        return AreaService.listar_areas_ativas()


# ==============================================================================
# TRILHAS DO ESTUDANTE
# ==============================================================================


class TrilhaListCreateView(generics.ListCreateAPIView):
    """
    Lista e cria trilhas do usuário autenticado.

    GET: Lista todas as trilhas ativas do usuário
    POST: Cria uma nova trilha
    """

    serializer_class = TrilhaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retorna apenas trilhas ativas do usuário autenticado."""
        return Trilha.objects.filter(
            usuario=self.request.user, ativa=True
        ).select_related("area", "usuario")

    def perform_create(self, serializer):
        """
        Cria trilha usando o service layer.

        Raises:
            TrilhaLimitExceededException: Se usuário excedeu limite
            AreaInativaException: Se área está inativa
        """
        try:
            trilha = TrilhaService.criar_trilha(
                usuario=self.request.user,
                titulo=serializer.validated_data.get("titulo"),
                descricao=serializer.validated_data.get("descricao", ""),
                area_id=serializer.validated_data.get("area").id
                if serializer.validated_data.get("area")
                else None,
                conteudo=serializer.validated_data.get("conteudo", ""),
            )
            serializer.instance = trilha
        except (TrilhaLimitExceededException, AreaInativaException) as e:
            raise e


class TrilhaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhes, atualização e exclusão de trilha.

    GET: Retorna detalhes da trilha
    PUT/PATCH: Atualiza a trilha
    DELETE: Arquiva a trilha (soft delete)
    """

    serializer_class = TrilhaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retorna apenas trilhas do usuário autenticado."""
        return Trilha.objects.filter(usuario=self.request.user).select_related(
            "area", "usuario"
        )

    def perform_update(self, serializer):
        """Atualiza trilha usando o service layer."""
        TrilhaService.atualizar_trilha(
            trilha=serializer.instance, **serializer.validated_data
        )

    def perform_destroy(self, instance):
        """Arquiva trilha (soft delete) ao invés de deletar."""
        TrilhaService.arquivar_trilha(instance)
