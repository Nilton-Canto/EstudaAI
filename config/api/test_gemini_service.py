from django.test import TestCase
from unittest.mock import patch, MagicMock
from api.gemini import GeminiService

class GeminiServiceTestCase(TestCase):
    @patch('api.gemini.genai.GenerativeModel')
    @patch('api.gemini.configure_gemini')
    def test_chat_guardrails(self, mock_configure, mock_model_class):
        # Configuração do mock
        mock_configure.return_value = True
        mock_model_instance = MagicMock()
        mock_model_class.return_value = mock_model_instance
        
        # Mock da resposta
        mock_response = MagicMock()
        mock_response.text = "Resposta educada sobre educação."
        mock_model_instance.generate_content.return_value = mock_response

        # Instancia o serviço
        service = GeminiService()
        
        # Chama o chat
        mensagem_usuario = "Como aprender Python?"
        resposta = service.chat(mensagem_usuario)
        
        # Verifica se a resposta é a esperada
        self.assertEqual(resposta, "Resposta educada sobre educação.")
        
        # Verifica se o generate_content foi chamado com o prompt contendo guardrails
        args, _ = mock_model_instance.generate_content.call_args
        prompt_enviado = args[0]
        
        self.assertIn("Você é o assistente virtual do EstudaAI", prompt_enviado)
        self.assertIn("REGRAS (GUARDRAILS):", prompt_enviado)
        self.assertIn(mensagem_usuario, prompt_enviado)

    @patch('api.gemini.genai.GenerativeModel')
    @patch('api.gemini.configure_gemini')
    def test_chat_historico_e_nome(self, mock_configure, mock_model_class):
        # Configuração do mock
        mock_configure.return_value = True
        mock_model_instance = MagicMock()
        mock_model_class.return_value = mock_model_instance
        
        mock_response = MagicMock()
        mock_response.text = "Resposta com contexto."
        mock_model_instance.generate_content.return_value = mock_response

        service = GeminiService()
        
        mensagem = "E qual o próximo passo?"
        historico = [
            {"role": "user", "parts": ["Quero aprender Python"]},
            {"role": "model", "parts": ["Comece pela sintaxe básica"]}
        ]
        nome = "Gabriel"
        
        service.chat(mensagem, historico=historico, nome_usuario=nome)
        
        args, _ = mock_model_instance.generate_content.call_args
        prompt = args[0]
        
        self.assertIn("O usuário se chama Gabriel", prompt)
        self.assertIn("HISTÓRICO DA CONVERSA:", prompt)
        self.assertIn("Usuário: Quero aprender Python", prompt)
        self.assertIn("Assistente: Comece pela sintaxe básica", prompt)
