from rest_framework import serializers

from .models import Area, Trilha, TrilhaCurso


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class TrilhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trilha
        fields = "__all__"
        read_only_fields = ["usuario", "data_criacao", "data_atualizacao"]


class TrilhaCursoSerializer(serializers.ModelSerializer):
    """Serializer para trilhas de curso geradas pela IA."""

    class Meta:
        model = TrilhaCurso
        fields = [
            "id",
            "titulo",
            "descricao",
            "solicitacao_original",
            "conteudo_json",
            "ativa",
            "data_criacao",
            "data_atualizacao",
        ]
        read_only_fields = ["data_criacao", "data_atualizacao"]
