# Testes básicos da API

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Area, TrilhaCurso, ProgressoTrilhaCurso

Usuario = get_user_model()


class AreaModelTestCase(TestCase):
    """Testes para o modelo Area"""

    def test_criar_area(self):
        """Testa criação de uma área"""
        area = Area.objects.create(nome="Programação", descricao="Área de programação")
        self.assertEqual(area.nome, "Programação")
        self.assertEqual(str(area), "Programação")

    def test_area_ativa_por_padrao(self):
        """Testa se área é criada ativa por padrão"""
        area = Area.objects.create(nome="Matemática")
        self.assertTrue(area.ativa)


class TrilhaCursoModelTestCase(TestCase):
    """Testes para o modelo TrilhaCurso"""

    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username="testuser", password="senha123", email="test@example.com"
        )
        self.area = Area.objects.create(nome="Python")

    def test_criar_trilha(self):
        """Testa criação de uma trilha"""
        trilha = TrilhaCurso.objects.create(
            usuario=self.usuario,
            titulo="Aprenda Python",
            descricao="Curso de Python",
            area=self.area,
            conteudo_json={"modulos": []},
        )
        self.assertEqual(trilha.titulo, "Aprenda Python")
        self.assertTrue(trilha.ativa)

    def test_trilha_pertence_usuario(self):
        """Testa relação entre trilha e usuário"""
        trilha = TrilhaCurso.objects.create(
            usuario=self.usuario, titulo="Minha Trilha", conteudo_json={}
        )
        self.assertEqual(trilha.usuario, self.usuario)
        self.assertIn(trilha, self.usuario.trilhas_curso.all())


class ProgressoTrilhaCursoModelTestCase(TestCase):
    """Testes para o modelo ProgressoTrilhaCurso"""

    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            username="testuser", password="senha123"
        )
        self.trilha = TrilhaCurso.objects.create(
            usuario=self.usuario, titulo="Trilha Teste", conteudo_json={}
        )

    def test_criar_progresso(self):
        """Testa criação de progresso"""
        progresso = ProgressoTrilhaCurso.objects.create(
            trilha=self.trilha,
            identificador="mod_0_aula_0",
            modulo_indice=0,
            aula_indice=0,
            concluida=True,
        )
        self.assertTrue(progresso.concluida)
        self.assertEqual(progresso.identificador, "mod_0_aula_0")

    def test_progresso_nao_concluido_por_padrao(self):
        """Testa se progresso não é concluído por padrão"""
        progresso = ProgressoTrilhaCurso.objects.create(
            trilha=self.trilha, identificador="mod_1_aula_1", modulo_indice=1, aula_indice=1
        )
        self.assertFalse(progresso.concluida)
