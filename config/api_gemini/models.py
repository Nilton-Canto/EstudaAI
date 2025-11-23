import json

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TrilhaCurso(models.Model):
    """
    Modelo para armazenar trilhas de curso geradas pela API
    """

    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trilhas_curso"
    )
    titulo = models.CharField(max_length=255, help_text="Título da trilha de curso")
    descricao = models.TextField(help_text="Descrição detalhada da trilha")
    solicitacao_original = models.TextField(help_text="Solicitação original do usuário")
    conteudo_json = models.JSONField(help_text="Conteúdo estruturado da trilha em JSON")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativa = models.BooleanField(default=True, help_text="Indica se a trilha está ativa")

    class Meta:
        ordering = ["-data_criacao"]
        verbose_name = "Trilha de Curso"
        verbose_name_plural = "Trilhas de Curso"

    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"

    def get_conteudo_formatado(self):
        """
        Retorna o conteúdo JSON formatado para exibição
        """
        try:
            return json.dumps(self.conteudo_json, indent=2, ensure_ascii=False)
        except:
            return str(self.conteudo_json)
