"""
Testes completos para a API de Geração de Trilhas de Curso - EstudaAI
Este arquivo contém todos os testes organizados e sem duplicações para:
- Health Check
- Modelos (TrilhaCurso)
- Geração de Prompts
- API de Trilhas
- Chat API
"""

import json
from unittest.mock import MagicMock, patch

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import TrilhaCurso
from .views import gerar_prompt_trilha_curso

User = get_user_model()


# ============================================================================
# TESTES DE HEALTH CHECK
# ============================================================================


class HealthCheckTestCase(APITestCase):
    """Testes para o endpoint de health check"""

    def setUp(self):
        self.client = APIClient()
        self.health_url = reverse("api_gemini:health_check")

    def test_health_check_success(self):
        """Testa o endpoint de health check básico"""
        response = self.client.get(self.health_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data

        self.assertIn("status", data)
        self.assertIn("service", data)
        self.assertIn("gemini_configured", data)
        self.assertIn("model", data)
        self.assertIn("version", data)
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["service"], "EstudaAI Gemini API")

    @override_settings(GEMINI_API_KEY="valid_api_key_for_testing")
    def test_health_check_with_valid_api_key(self):
        """Testa health check com chave válida"""
        response = self.client.get(self.health_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertTrue(data["gemini_configured"])

    @override_settings(GEMINI_API_KEY=None)
    def test_health_check_without_api_key(self):
        """Testa health check sem chave"""
        response = self.client.get(self.health_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertFalse(data["gemini_configured"])


# ============================================================================
# TESTES DO MODELO TRILHACURSO
# ============================================================================


class TrilhaCursoModelTest(TestCase):
    """Testes para o modelo TrilhaCurso"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            nome="Usuário Teste",
            universidade="Universidade Teste",
            curso="Ciência da Computação",
            ano_formatura=2025,
            idade=22,
        )

    def test_criar_trilha_curso(self):
        """Teste criação de trilha de curso"""
        trilha_data = {
            "titulo": "Python para Iniciantes",
            "descricao": "Trilha completa de Python",
            "nivel": "Iniciante",
            "modulos": [],
        }

        trilha = TrilhaCurso.objects.create(
            usuario=self.user,
            titulo="Python para Iniciantes",
            descricao="Trilha completa de Python",
            solicitacao_original="Quero aprender Python",
            conteudo_json=trilha_data,
        )

        self.assertEqual(trilha.titulo, "Python para Iniciantes")
        self.assertEqual(trilha.usuario, self.user)
        self.assertTrue(trilha.ativa)
        self.assertEqual(str(trilha), "Python para Iniciantes - testuser")

    def test_get_conteudo_formatado(self):
        """Teste formatação do conteúdo JSON"""
        trilha_data = {"titulo": "Teste", "nivel": "Iniciante"}

        trilha = TrilhaCurso.objects.create(
            usuario=self.user,
            titulo="Teste",
            descricao="Descrição teste",
            solicitacao_original="Solicitação teste",
            conteudo_json=trilha_data,
        )

        conteudo_formatado = trilha.get_conteudo_formatado()
        self.assertIn("titulo", conteudo_formatado)
        self.assertIn("Teste", conteudo_formatado)


# ============================================================================
# TESTES DE GERAÇÃO DE PROMPT
# ============================================================================


class GerarPromptTest(TestCase):
    """Testes para a função de geração de prompt"""

    def test_gerar_prompt_basico(self):
        """Teste geração de prompt básico"""
        solicitacao = "Quero aprender JavaScript"
        prompt = gerar_prompt_trilha_curso(solicitacao)

        self.assertIn(solicitacao, prompt)
        self.assertIn("FORMATO DE RESPOSTA", prompt)
        self.assertIn("JSON", prompt)

    def test_gerar_prompt_com_dados_usuario(self):
        """Teste geração de prompt com dados do usuário"""
        solicitacao = "Quero aprender Machine Learning"
        usuario_data = {
            "curso": "Ciência da Computação",
            "universidade": "USP",
            "ano_formatura": 2025,
            "idade": 22,
        }

        prompt = gerar_prompt_trilha_curso(solicitacao, usuario_data)

        self.assertIn(solicitacao, prompt)
        self.assertIn("DADOS DO USUÁRIO", prompt)
        self.assertIn("Ciência da Computação", prompt)
        self.assertIn("USP", prompt)


# ============================================================================
# TESTES DA API DE TRILHAS
# ============================================================================


class APITrilhaTest(APITestCase):
    """Testes para os endpoints da API de trilhas"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            nome="Usuário Teste",
            universidade="Universidade Teste",
            curso="Ciência da Computação",
            ano_formatura=2025,
            idade=22,
        )

        # Mock response do Gemini
        self.mock_trilha_response = {
            "titulo": "Trilha de Python",
            "descricao": "Aprenda Python do zero",
            "nivel": "Iniciante",
            "duracao_total": "8 semanas",
            "modulos": [
                {
                    "numero": 1,
                    "titulo": "Introdução ao Python",
                    "descricao": "Fundamentos da linguagem",
                    "duracao": "2 semanas",
                    "topicos": ["Sintaxe básica", "Variáveis", "Tipos de dados"],
                    "recursos": [
                        {
                            "tipo": "video",
                            "titulo": "Python Básico",
                            "descricao": "Curso introdutório",
                        }
                    ],
                    "atividades_praticas": ["Exercícios básicos"],
                }
            ],
            "projeto_final": "Sistema de gerenciamento simples",
            "recursos_complementares": ["Documentação oficial"],
        }

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_gerar_trilha_sucesso(self, mock_model):
        """Teste geração de trilha com sucesso"""
        # Mock da resposta do modelo
        mock_response = MagicMock()
        mock_response.text = json.dumps(self.mock_trilha_response)
        mock_model.return_value.generate_content.return_value = mock_response

        url = reverse("api_gemini:gerar_trilha_curso")
        data = {"solicitacao": "Quero aprender Python", "user_id": self.user.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "success")
        self.assertIn("trilha", response.data)
        self.assertEqual(response.data["trilha"]["titulo"], "Trilha de Python")

        # Verificar se a trilha foi salva no banco
        trilha_salva = TrilhaCurso.objects.filter(usuario=self.user).first()
        self.assertIsNotNone(trilha_salva)
        self.assertEqual(trilha_salva.titulo, "Trilha de Python")

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_gerar_trilha_com_dados_usuario(self, mock_model):
        """Teste geração de trilha considerando dados do usuário"""
        # Mock da resposta do modelo
        mock_response = MagicMock()
        mock_trilha_personalizada = self.mock_trilha_response.copy()
        mock_trilha_personalizada["titulo"] = "Python para Ciência da Computação"
        mock_response.text = json.dumps(mock_trilha_personalizada)
        mock_model.return_value.generate_content.return_value = mock_response

        url = reverse("api_gemini:gerar_trilha_curso")
        data = {
            "solicitacao": "Quero aprender Python para meu curso",
            "user_id": self.user.id,
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["trilha"]["titulo"], "Python para Ciência da Computação"
        )

        # Verificar se os dados do usuário foram considerados
        prompt_usado = mock_model.return_value.generate_content.call_args[0][0]
        self.assertIn("Ciência da Computação", prompt_usado)
        self.assertIn("Universidade Teste", prompt_usado)

    def test_gerar_trilha_sem_solicitacao(self):
        """Teste erro quando solicitação não é fornecida"""
        url = reverse("api_gemini:gerar_trilha_curso")
        data = {"user_id": self.user.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_gerar_trilha_sem_user_id(self, mock_model):
        """Teste geração de trilha sem user_id (deve funcionar sem personalização)"""
        # Mock da resposta do modelo
        mock_response = MagicMock()
        mock_response.text = json.dumps(self.mock_trilha_response)
        mock_model.return_value.generate_content.return_value = mock_response

        url = reverse("api_gemini:gerar_trilha_curso")
        data = {"solicitacao": "Quero aprender Python"}

        response = self.client.post(url, data, format="json")

        # Deve funcionar sem personalização
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "success")
        self.assertFalse(response.data.get("personalizada", False))

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_gerar_trilha_usuario_inexistente(self, mock_model):
        """Teste geração de trilha com usuário inexistente (deve funcionar sem personalização)"""
        # Mock da resposta do modelo
        mock_response = MagicMock()
        mock_response.text = json.dumps(self.mock_trilha_response)
        mock_model.return_value.generate_content.return_value = mock_response

        url = reverse("api_gemini:gerar_trilha_curso")
        data = {"solicitacao": "Quero aprender Python", "user_id": 99999}

        response = self.client.post(url, data, format="json")

        # Deve funcionar mesmo com usuário inexistente (sem personalização)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "success")
        self.assertFalse(response.data.get("personalizada", False))

    @override_settings(GEMINI_API_KEY="test_key_for_verification")
    def test_gerar_trilha_api_nao_configurada(self):
        """Teste erro quando API não está configurada"""
        url = reverse("api_gemini:gerar_trilha_curso")
        data = {"solicitacao": "Teste", "user_id": self.user.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("error", response.data)

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_gerar_trilha_erro_gemini(self, mock_model):
        """Teste tratamento de erro da API do Gemini"""
        # Mock de erro na API
        mock_model.return_value.generate_content.side_effect = Exception(
            "Erro na API do Gemini"
        )

        url = reverse("api_gemini:gerar_trilha_curso")
        data = {"solicitacao": "Quero aprender Python", "user_id": self.user.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("error", response.data)

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_gerar_trilha_json_invalido(self, mock_model):
        """Teste tratamento de JSON inválido do Gemini"""
        # Mock de resposta com JSON inválido
        mock_response = MagicMock()
        mock_response.text = "Resposta inválida não JSON"
        mock_model.return_value.generate_content.return_value = mock_response

        url = reverse("api_gemini:gerar_trilha_curso")
        data = {"solicitacao": "Quero aprender Python", "user_id": self.user.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("error", response.data)

    def test_listar_trilhas_usuario(self):
        """Teste listagem de trilhas do usuário"""
        # Criar trilhas de teste
        TrilhaCurso.objects.create(
            usuario=self.user,
            titulo="Trilha 1",
            descricao="Primeira trilha",
            solicitacao_original="Solicitação 1",
            conteudo_json={"titulo": "Trilha 1"},
        )

        TrilhaCurso.objects.create(
            usuario=self.user,
            titulo="Trilha 2",
            descricao="Segunda trilha",
            solicitacao_original="Solicitação 2",
            conteudo_json={"titulo": "Trilha 2"},
        )

        url = reverse(
            "api_gemini:listar_trilhas_usuario", kwargs={"user_id": self.user.id}
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_trilhas"], 2)
        self.assertEqual(len(response.data["trilhas"]), 2)
        self.assertEqual(response.data["usuario"], "testuser")

    def test_listar_trilhas_usuario_inexistente(self):
        """Teste listagem de trilhas para usuário inexistente"""
        url = reverse("api_gemini:listar_trilhas_usuario", kwargs={"user_id": 99999})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("error", response.data)

    def test_listar_trilhas_usuario_sem_trilhas(self):
        """Teste listagem para usuário sem trilhas"""
        url = reverse(
            "api_gemini:listar_trilhas_usuario", kwargs={"user_id": self.user.id}
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_trilhas"], 0)
        self.assertEqual(len(response.data["trilhas"]), 0)

    def test_listar_trilhas_apenas_ativas(self):
        """Teste que lista apenas trilhas ativas"""
        # Trilha ativa
        TrilhaCurso.objects.create(
            usuario=self.user,
            titulo="Trilha Ativa",
            descricao="Trilha ativa",
            solicitacao_original="Solicitação ativa",
            conteudo_json={"titulo": "Trilha Ativa"},
            ativa=True,
        )

        # Trilha inativa
        TrilhaCurso.objects.create(
            usuario=self.user,
            titulo="Trilha Inativa",
            descricao="Trilha inativa",
            solicitacao_original="Solicitação inativa",
            conteudo_json={"titulo": "Trilha Inativa"},
            ativa=False,
        )

        url = reverse(
            "api_gemini:listar_trilhas_usuario", kwargs={"user_id": self.user.id}
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_trilhas"], 1)
        self.assertEqual(response.data["trilhas"][0]["titulo"], "Trilha Ativa")


# ============================================================================
# TESTES DA API DE CHAT
# ============================================================================


class ChatAPITest(APITestCase):
    """Testes para o endpoint de chat com Gemini"""

    def setUp(self):
        self.client = APIClient()
        self.chat_url = reverse("api_gemini:chat_with_gemini")

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_chat_sucesso(self, mock_model):
        """Teste chat com sucesso"""
        # Mock da resposta do modelo
        mock_response = MagicMock()
        mock_response.text = "Esta é uma resposta de teste do Gemini"
        mock_model.return_value.generate_content.return_value = mock_response

        response = self.client.post(
            self.chat_url, data={"message": "Olá, como você está?"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("response", response.data)
        self.assertEqual(
            response.data["response"], "Esta é uma resposta de teste do Gemini"
        )

    @override_settings(GEMINI_API_KEY="test_key_for_verification")
    def test_chat_sem_mensagem(self):
        """Teste erro quando mensagem não é fornecida"""
        response = self.client.post(self.chat_url, data={}, format="json")

        # API key é verificada primeiro, então erro 500
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @override_settings(GEMINI_API_KEY="test_key_for_verification")
    def test_chat_api_nao_configurada(self):
        """Teste erro quando API não está configurada"""
        response = self.client.post(
            self.chat_url, data={"message": "teste"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_chat_erro_gemini(self, mock_model):
        """Teste tratamento de erro da API do Gemini"""
        # Mock de erro na API
        mock_model.return_value.generate_content.side_effect = Exception(
            "Erro na API do Gemini"
        )

        response = self.client.post(
            self.chat_url, data={"message": "Teste"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertIn("error", response.data)

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_chat_mensagem_vazia(self, mock_model):
        """Teste chat com mensagem vazia"""
        response = self.client.post(self.chat_url, data={"message": ""}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_chat_mensagem_longa(self, mock_model):
        """Teste chat com mensagem muito longa"""
        # Mock da resposta do modelo
        mock_response = MagicMock()
        mock_response.text = "Resposta para mensagem longa"
        mock_model.return_value.generate_content.return_value = mock_response

        mensagem_longa = "a" * 10000  # 10k caracteres

        response = self.client.post(
            self.chat_url, data={"message": mensagem_longa}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("response", response.data)

    @override_settings(GEMINI_API_KEY="valid_test_key")
    @patch("api_gemini.views.genai.configure")
    @patch("api_gemini.views.genai.GenerativeModel")
    def test_chat_com_sucesso_completo(self, mock_model_class, mock_configure):
        """Teste chat com mocking completo"""
        # Mock da resposta do Gemini
        mock_response = MagicMock()
        mock_response.text = "Esta é uma resposta de teste do Gemini"

        mock_model = MagicMock()
        mock_model.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model

        response = self.client.post(
            self.chat_url,
            data={"message": "Olá, como você pode me ajudar?"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data

        self.assertIn("message", data)
        self.assertIn("response", data)
        self.assertIn("status", data)
        self.assertIn("model_used", data)
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["message"], "Olá, como você pode me ajudar?")
        self.assertEqual(data["response"], "Esta é uma resposta de teste do Gemini")

        # Verificar se o modelo foi chamado corretamente
        mock_model_class.assert_called_once_with(settings.GEMINI_MODEL)
        mock_model.generate_content.assert_called_once_with(
            "Olá, como você pode me ajudar?"
        )

    def test_chat_invalid_json(self):
        """Teste chat com JSON inválido"""
        # Para testar JSON inválido, vamos usar o client do Django diretamente
        from django.test import Client

        django_client = Client()

        response = django_client.post(
            self.chat_url, data="invalid json", content_type="application/json"
        )

        # O Django pode retornar 400 para JSON inválido
        self.assertIn(
            response.status_code,
            [status.HTTP_400_BAD_REQUEST, status.HTTP_500_INTERNAL_SERVER_ERROR],
        )


# ============================================================================
# TESTES DE INTEGRAÇÃO
# ============================================================================


class IntegrationTestCase(APITestCase):
    """Testes de integração para verificar se os endpoints funcionam juntos"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="integration_user",
            email="integration@test.com",
            nome="Usuário Integração",
            universidade="Universidade Teste",
            curso="Ciência da Computação",
            ano_formatura=2025,
            idade=22,
        )
        self.health_url = reverse("api_gemini:health_check")
        self.trilha_url = reverse("api_gemini:gerar_trilha_curso")
        self.chat_url = reverse("api_gemini:chat_with_gemini")

    def test_endpoints_existem(self):
        """Verifica se todos os endpoints existem e respondem"""
        # Health check sempre deve funcionar
        response = self.client.get(self.health_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Trilha endpoint existe (pode falhar por falta de API key, mas endpoint existe)
        response = self.client.post(
            self.trilha_url, data={"solicitacao": "teste"}, format="json"
        )
        self.assertIn(
            response.status_code,
            [
                status.HTTP_200_OK,
                status.HTTP_400_BAD_REQUEST,
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            ],
        )

        # Chat endpoint existe (pode falhar por falta de API key, mas endpoint existe)
        response = self.client.post(
            self.chat_url, data={"message": "teste"}, format="json"
        )
        self.assertIn(
            response.status_code,
            [
                status.HTTP_200_OK,
                status.HTTP_400_BAD_REQUEST,
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            ],
        )

    def test_formato_resposta_padrao(self):
        """Verifica se todas as respostas seguem formato padrão"""
        # Health check deve ter formato específico
        response = self.client.get(self.health_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        required_fields = ["status", "service", "gemini_configured", "model", "version"]
        for field in required_fields:
            self.assertIn(field, response.data)

    def test_validacao_entrada_consistente(self):
        """Verifica se a validação de entrada é consistente entre endpoints"""
        # Teste com dados vazios
        response_trilha = self.client.post(self.trilha_url, data={}, format="json")
        response_chat = self.client.post(self.chat_url, data={}, format="json")

        # Ambos devem retornar erro (400 ou 500 dependendo da configuração)
        self.assertIn(
            response_trilha.status_code,
            [status.HTTP_400_BAD_REQUEST, status.HTTP_500_INTERNAL_SERVER_ERROR],
        )
        self.assertIn(
            response_chat.status_code,
            [status.HTTP_400_BAD_REQUEST, status.HTTP_500_INTERNAL_SERVER_ERROR],
        )
