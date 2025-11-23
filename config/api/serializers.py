from rest_framework import serializers
from .models import Area, Trilha

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class TrilhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trilha
        fields = "__all__"
        read_only_fields = ["usuario", "data_criacao", "data_atualizacao"]
