from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Usuario

# ===== IMPORTANTE: COMO FUNCIONAM OS USUÁRIOS TEMPORÁRIOS NOS TESTES =====
# O Django cria um banco de dados TEMPORÁRIO para cada execução de teste.
# Todos os usuários criados durante os testes são AUTOMATICAMENTE APAGADOS
# ao final da execução. Isso garante que:
# 1. Os testes não interferem uns nos outros
# 2. Os testes não afetam o banco de dados real da aplicação
# 3. Cada teste roda com dados limpos e previsíveis


class LoginTestCase(TestCase):
    """Testes para funcionalidade de login"""

    def setUp(self):
        """Configura dados para os testes - executado antes de cada teste"""
        # Cria usuário de teste
        self.usuario_teste = Usuario.objects.create_user(
            username="usuario_teste",
            password="senha123",
            nome="João Silva",
            email="joao@teste.com",
            universidade="UFMG",
            curso="Ciência da Computação",
            idade=22,
            ano_formatura=2025,
        )

        # Cliente para fazer requisições
        self.client = Client()

        # URL da página de login
        self.login_url = reverse("login")

    def test_pagina_login_carrega(self):
        """Testa se a página de login carrega corretamente"""
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")
        self.assertContains(response, "login-title")

    def test_login_com_credenciais_validas(self):
        """Testa login com usuário e senha corretos"""
        # Faz login
        login_success = self.client.login(username="usuario_teste", password="senha123")

        # Verifica se login foi bem-sucedido
        self.assertTrue(login_success)

        # Verifica se usuário está na sessão
        response = self.client.get(self.login_url)
        self.assertTrue("_auth_user_id" in self.client.session)

    def test_login_com_credenciais_invalidas(self):
        """Testa login com senha incorreta"""
        response = self.client.post(
            self.login_url, {"username": "usuario_teste", "password": "senha_errada"}
        )

        # Deve permanecer na página de login
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")

    def test_login_usuario_inexistente(self):
        """Testa login com usuário que não existe"""
        response = self.client.post(
            self.login_url,
            {"username": "usuario_inexistente", "password": "qualquer_senha"},
        )

        # Deve permanecer na página de login
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")

    def test_campos_obrigatorios(self):
        """Testa envio do formulário com campos vazios"""
        response = self.client.post(self.login_url, {"username": "", "password": ""})

        # Deve permanecer na página de login
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")


class CadastroTestCase(TestCase):
    """Testes para funcionalidade de cadastro de usuários"""

    def setUp(self):
        """Configura dados para os testes - executado antes de cada teste"""
        self.client = Client()
        self.signup_url = reverse("signup")

        # Dados válidos para teste
        self.dados_validos = {
            "username": "novo_usuario",
            "nome": "Maria Silva",
            "email": "maria@teste.com",
            "universidade": "USP",
            "curso": "Engenharia",
            "ano_formatura": 2026,
            "idade": 20,
            "password": "senha123",
        }

    def test_pagina_cadastro_carrega(self):
        """Testa se a página de cadastro carrega corretamente"""
        response = self.client.get(self.signup_url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cadastro")
        self.assertContains(response, "login-title")

    def test_criacao_usuario_valido(self):
        """Testa criação de usuário com dados válidos"""
        # Verifica que não existe usuário antes
        self.assertFalse(Usuario.objects.filter(username="novo_usuario").exists())

        # Envia dados do formulário
        response = self.client.post(self.signup_url, self.dados_validos)

        # Deve redirecionar após cadastro bem-sucedido
        self.assertEqual(response.status_code, 302)

        # Verifica se usuário foi criado no banco TEMPORÁRIO
        usuario_criado = Usuario.objects.get(username="novo_usuario")
        self.assertEqual(usuario_criado.nome, "Maria Silva")
        self.assertEqual(usuario_criado.email, "maria@teste.com")

        # IMPORTANTE: Este usuário só existe durante este teste!
        # Será automaticamente apagado quando o teste terminar.

    def test_email_duplicado(self):
        """Testa erro ao tentar cadastrar email já existente"""
        # Cria primeiro usuário
        Usuario.objects.create_user(
            username="usuario1", email="email@teste.com", password="senha123"
        )

        # Tenta criar segundo usuário com mesmo email
        dados_duplicados = self.dados_validos.copy()
        dados_duplicados["email"] = "email@teste.com"
        dados_duplicados["username"] = "usuario2"

        response = self.client.post(self.signup_url, dados_duplicados)

        # Deve permanecer na página de cadastro
        self.assertEqual(response.status_code, 200)

        # Verifica que segundo usuário NÃO foi criado
        self.assertFalse(Usuario.objects.filter(username="usuario2").exists())

    def test_campos_obrigatorios_cadastro(self):
        """Testa cadastro com campos obrigatórios vazios"""
        dados_incompletos = {"username": "", "email": "", "password": ""}

        response = self.client.post(self.signup_url, dados_incompletos)

        # Deve permanecer na página de cadastro
        self.assertEqual(response.status_code, 200)

        # Verifica que nenhum usuário foi criado
        self.assertEqual(Usuario.objects.count(), 0)

    def test_senha_criptografada(self):
        """Testa se a senha é criptografada corretamente"""
        response = self.client.post(self.signup_url, self.dados_validos)

        # Busca usuário criado
        usuario = Usuario.objects.get(username="novo_usuario")

        # Verifica que senha não está em texto plano
        self.assertNotEqual(usuario.password, "senha123")

        # Verifica que senha foi criptografada (método check_password)
        self.assertTrue(usuario.check_password("senha123"))

    def tearDown(self):
        """Executado após cada teste - OPCIONAL pois Django já limpa automaticamente"""
        # NOTA: Este método é opcional nos testes do Django.
        # O Django automaticamente apaga o banco temporário após cada teste.
        # Incluído apenas para demonstrar o ciclo de vida dos testes.
        pass
