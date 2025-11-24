from django.contrib.auth import get_user_model
from django.db import models

Usuario = get_user_model()


class Area(models.Model):
    """
    Modelo para áreas de conhecimento/estudo
    """

    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    icone = models.CharField(
        max_length=50, blank=True, help_text="Nome do ícone ou emoji"
    )
    cor = models.CharField(
        max_length=7, default="#4f46e5", help_text="Cor em hexadecimal"
    )
    ativa = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

    def __str__(self):
        return self.nome


class Trilha(models.Model):
    """
    Modelo para trilhas de estudo dos usuários
    """

    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="trilhas"
    )
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    area = models.ForeignKey(
        Area, on_delete=models.SET_NULL, null=True, blank=True, related_name="trilhas"
    )
    conteudo = models.TextField(
        blank=True, help_text="Conteúdo JSON da trilha gerada pela IA"
    )
    ativa = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-data_criacao"]
        verbose_name = "Trilha"
        verbose_name_plural = "Trilhas"

    def __str__(self):
        return f"{self.titulo} - {self.usuario.nome}"


class Progresso(models.Model):
    """
    Progresso do estudante dentro de uma trilha
    """

    trilha = models.ForeignKey(
        Trilha, on_delete=models.CASCADE, related_name="progresso"
    )
    etapa = models.CharField(max_length=255)
    concluida = models.BooleanField(default=False)
    data_conclusao = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Progresso"
        verbose_name_plural = "Progresso"

    def __str__(self):
        return f"{self.trilha.titulo} - {self.etapa}"


class TrilhaCurso(models.Model):
    """
    Modelo para trilhas de curso geradas pela IA (Gemini).
    Armazena trilhas completas com conteúdo estruturado em JSON.
    """

    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="trilhas_curso"
    )
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    solicitacao_original = models.TextField(
        help_text="Texto original enviado pelo usuário"
    )
    conteudo_json = models.JSONField(
        help_text="Conteúdo completo da trilha em formato JSON"
    )
    ativa = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-data_criacao"]
        verbose_name = "Trilha de Curso (IA)"
        verbose_name_plural = "Trilhas de Curso (IA)"

    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"
