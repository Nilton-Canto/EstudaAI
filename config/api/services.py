"""
Serviços de lógica de negócio para a aplicação API.
"""

from django.contrib.auth import get_user_model
from django.db import transaction

from .constants import MAX_TRILHAS_POR_USUARIO
from .exceptions import AreaInativaException, TrilhaLimitExceededException
from .models import Area, Trilha

Usuario = get_user_model()


class TrilhaService:
    """Serviço para manipulação de trilhas."""

    @staticmethod
    def criar_trilha(usuario, titulo, descricao, area_id=None, conteudo=""):
        """
        Cria uma nova trilha para o usuário.

        Args:
            usuario: Instância do usuário
            titulo: Título da trilha
            descricao: Descrição da trilha
            area_id: ID da área (opcional)
            conteudo: Conteúdo JSON da trilha (opcional)

        Returns:
            Trilha: Instância da trilha criada

        Raises:
            TrilhaLimitExceededException: Se usuário excedeu limite
            AreaInativaException: Se área está inativa
        """
        # Verificar limite de trilhas
        count_trilhas = Trilha.objects.filter(usuario=usuario, ativa=True).count()
        if count_trilhas >= MAX_TRILHAS_POR_USUARIO:
            raise TrilhaLimitExceededException()

        # Verificar se área está ativa
        area = None
        if area_id:
            try:
                area = Area.objects.get(id=area_id)
                if not area.ativa:
                    raise AreaInativaException()
            except Area.DoesNotExist:
                raise AreaInativaException(detail="Área não encontrada.")

        # Criar trilha
        with transaction.atomic():
            trilha = Trilha.objects.create(
                usuario=usuario,
                titulo=titulo,
                descricao=descricao,
                area=area,
                conteudo=conteudo,
            )

        return trilha

    @staticmethod
    def atualizar_trilha(trilha, **dados):
        """
        Atualiza uma trilha existente.

        Args:
            trilha: Instância da trilha
            **dados: Dados a serem atualizados

        Returns:
            Trilha: Instância da trilha atualizada
        """
        for campo, valor in dados.items():
            if hasattr(trilha, campo):
                setattr(trilha, campo, valor)

        trilha.save()
        return trilha

    @staticmethod
    def arquivar_trilha(trilha):
        """
        Arquiva uma trilha (soft delete).

        Args:
            trilha: Instância da trilha

        Returns:
            Trilha: Instância da trilha arquivada
        """
        trilha.ativa = False
        trilha.save()
        return trilha


class AreaService:
    """Serviço para manipulação de áreas."""

    @staticmethod
    def listar_areas_ativas():
        """
        Retorna todas as áreas ativas.

        Returns:
            QuerySet: Áreas ativas ordenadas por nome
        """
        return Area.objects.filter(ativa=True).order_by("nome")

    @staticmethod
    def criar_area(nome, descricao, icone="📚", cor="#4f46e5"):
        """
        Cria uma nova área de conhecimento.

        Args:
            nome: Nome da área
            descricao: Descrição da área
            icone: Ícone/emoji da área
            cor: Cor hexadecimal da área

        Returns:
            Area: Instância da área criada
        """
        with transaction.atomic():
            area = Area.objects.create(
                nome=nome,
                descricao=descricao,
                icone=icone,
                cor=cor,
            )

        return area
