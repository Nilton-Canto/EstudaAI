from django.contrib.auth.models import AbstractUser #importar abstractUSer, pois o usuário será montado com características específicas
from django.db import models #importação do models, pois utilizaremos eles para especificar o tipo de cada campo do casdastro
from django.core.validators import MinValueValidator, MaxValueValidator #bibliotecas de validação de máximo e mínimo


class Usuario(AbstractUser): #criação de uma classe usuário
    nome = models.CharField(max_length=100)#Char pois é tudo caracter, o tamanho pode variar, sendo de caso a caso
    email = models.EmailField(unique=True)#modelo específico de email, pois email tem seus peculiaridades, ex: @
    universidade = models.CharField(max_length=255)#Char pois é tudo caracter
    curso = models.CharField(max_length=255)#Char pois é tudo caracter
    ano_formatura = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(2000), MaxValueValidator(2060)])# Intenger para números inteiros, null=True --> o Banco não dará erro se estiver vazio
    idade = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(8), MaxValueValidator(100)])#blank=True --> o django aceitará formulários com essa parte em branco, mine max value validator para validar e não ter número absurdoss
    
    REQUIRED_FIELDS = ['nome','email', 'universidade', 'curso', 'ano_formatura', 'idade']#indica quais campos são obrigatórios ao criar um superusuário, evitando que seja colocado apenas nome e senha, mas isso nãp tem efeito em formulários, apenas superusuarios!

    def __str__(self): #Esse método define como o objeto vai aparecer
        return self.username #por conta desse self username, retornará a própria string digitada pelo usuário
