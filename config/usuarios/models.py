# Importações necessárias
from django.contrib.auth.models import AbstractUser  # Modelo base de usuário do Django
from django.core.validators import (  # Validadores de valores
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models  # Tipos de campos do banco de dados


class Usuario(AbstractUser):  # criação de uma classe usuário
    nome = models.CharField(
        max_length=100
    )  # Char pois é tudo caracter, o tamanho pode variar, sendo de caso a caso
    email = models.EmailField(
        unique=True
    )  # modelo específico de email, pois email tem seus peculiaridades, ex: @
    universidade = models.CharField(max_length=255)  # Char pois é tudo caracter
    curso = models.CharField(max_length=255)  # Char pois é tudo caracter
    ano_formatura = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(2000), MaxValueValidator(2060)],
    )  # Intenger para números inteiros, null=True --> o Banco não dará erro se estiver vazio
    idade = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(8), MaxValueValidator(100)]
    )  # blank=True --> o django aceitará formulários com essa parte em branco, mine max value validator para validar e não ter número absurdoss

    # Campos básicos do perfil
    nome = models.CharField(max_length=100)  # Nome completo do usuário
    email = models.EmailField(unique=True)  # Email único no sistema

    # Campos acadêmicos
    universidade = models.CharField(max_length=255)  # Nome da universidade
    curso = models.CharField(max_length=255)  # Nome do curso

    # Campos opcionais com validação
    ano_formatura = models.IntegerField(
        null=True,
        blank=True,  # Permite valores vazios
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(2060),
        ],  # Entre 2000 e 2060
    )

    idade = models.IntegerField(
        null=True,
        blank=True,  # Permite valores vazios
        validators=[MinValueValidator(8), MaxValueValidator(100)],  # Entre 8 e 100 anos
    )

    # Campos obrigatórios para criação de superusuário
    REQUIRED_FIELDS = [
        "nome",
        "email",
        "universidade",
        "curso",
        "ano_formatura",
        "idade",
    ]

    def __str__(self):
        """Define como o objeto aparece em strings (admin, logs, etc.)"""
        return self.username
