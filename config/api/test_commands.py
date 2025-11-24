from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth import get_user_model
from api.models import Area, TrilhaCurso
from io import StringIO
import json
import os
from unittest.mock import patch, mock_open

Usuario = get_user_model()

class PopulateAreasCommandTestCase(TestCase):
    def test_populate_areas(self):
        """Testa se o comando populate_areas cria as áreas corretamente"""
        out = StringIO()
        call_command('populate_areas', stdout=out)
        
        # Verifica se as áreas foram criadas
        self.assertTrue(Area.objects.filter(nome="Desenvolvimento Web").exists())
        self.assertTrue(Area.objects.filter(nome="Ciência de Dados").exists())
        self.assertTrue(Area.objects.filter(nome="Inteligência Artificial").exists())
        
        # Verifica output
        self.assertIn('Area "Desenvolvimento Web" created', out.getvalue())

    def test_populate_areas_idempotency(self):
        """Testa se rodar o comando duas vezes não duplica áreas"""
        out = StringIO()
        call_command('populate_areas', stdout=out)
        count_first = Area.objects.count()
        
        call_command('populate_areas', stdout=out)
        count_second = Area.objects.count()
        
        self.assertEqual(count_first, count_second)

class PopulateTrilhasCommandTestCase(TestCase):
    def setUp(self):
        # Cria usuário admin necessário e uma área
        self.admin_user = Usuario.objects.create(
            username="admin_trilhas",
            email="admin@estudaai.com",
            is_staff=True
        )
        self.area = Area.objects.create(nome="Desenvolvimento Web")
        
        # Dados de exemplo para mockar o JSON
        self.mock_data = [
            {
                "area_nome": "Desenvolvimento Web",
                "titulo": "Trilha Teste",
                "descricao": "Descrição Teste",
                "conteudo": {
                    "modulos": [
                        {
                            "titulo": "Módulo 1",
                            "aulas": [
                                {
                                    "titulo": "Aula 1",
                                    "descricao": "Desc",
                                    "tipo": "video",
                                    "duracao": "10m"
                                }
                            ]
                        }
                    ]
                }
            }
        ]

    @patch('api.management.commands.populate_trilhas.Command.carregar_trilhas')
    def test_populate_trilhas_creation(self, mock_carregar):
        """Testa a criação de trilhas a partir do JSON"""
        mock_carregar.return_value = self.mock_data
        out = StringIO()
        
        call_command('populate_trilhas', stdout=out)
        
        self.assertTrue(TrilhaCurso.objects.filter(titulo="Trilha Teste").exists())
        trilha = TrilhaCurso.objects.get(titulo="Trilha Teste")
        self.assertEqual(trilha.area, self.area)
        self.assertIn("Criada: Trilha Teste", out.getvalue())

    @patch('api.management.commands.populate_trilhas.Command.carregar_trilhas')
    def test_populate_trilhas_dry_run(self, mock_carregar):
        """Testa a flag --dry-run"""
        mock_carregar.return_value = self.mock_data
        out = StringIO()
        
        call_command('populate_trilhas', '--dry-run', stdout=out)
        
        self.assertFalse(TrilhaCurso.objects.filter(titulo="Trilha Teste").exists())
        self.assertIn("[Dry-run] Prepararia criação da trilha: Trilha Teste", out.getvalue())

    @patch('api.management.commands.populate_trilhas.Command.carregar_trilhas')
    def test_populate_trilhas_refresh(self, mock_carregar):
        """Testa a flag --refresh"""
        mock_carregar.return_value = self.mock_data
        
        # Cria uma trilha antiga
        TrilhaCurso.objects.create(
            usuario=self.admin_user,
            titulo="Trilha Antiga",
            area=self.area,
            conteudo_json={}
        )
        
        out = StringIO()
        call_command('populate_trilhas', '--refresh', stdout=out)
        
        self.assertFalse(TrilhaCurso.objects.filter(titulo="Trilha Antiga").exists())
        self.assertTrue(TrilhaCurso.objects.filter(titulo="Trilha Teste").exists())
        self.assertIn("Removidas 1 trilhas pré-definidas antigas", out.getvalue())

    @patch('api.management.commands.populate_trilhas.Command.carregar_trilhas')
    def test_populate_trilhas_only(self, mock_carregar):
        """Testa a flag --only"""
        mock_data_multiple = self.mock_data + [
            {
                "area_nome": "Desenvolvimento Web",
                "titulo": "Outra Trilha",
                "descricao": "Desc",
                "conteudo": {}
            }
        ]
        mock_carregar.return_value = mock_data_multiple
        out = StringIO()
        
        call_command('populate_trilhas', '--only', 'Outra', stdout=out)
        
        self.assertFalse(TrilhaCurso.objects.filter(titulo="Trilha Teste").exists())
        self.assertTrue(TrilhaCurso.objects.filter(titulo="Outra Trilha").exists())

    @patch('api.management.commands.populate_trilhas.Command.carregar_trilhas')
    def test_populate_trilhas_validation_warning(self, mock_carregar):
        """Testa avisos de validação"""
        invalid_data = [
            {
                "area_nome": "Desenvolvimento Web",
                "titulo": "Trilha Incompleta",
                "conteudo": {
                    "modulos": [
                        {
                            "aulas": [
                                {"titulo": "Aula Sem Campos"} # Faltam campos obrigatórios
                            ]
                        }
                    ]
                }
            }
        ]
        mock_carregar.return_value = invalid_data
        out = StringIO()
        
        call_command('populate_trilhas', stdout=out)
        
        self.assertIn("Avisos/Problemas de estrutura", out.getvalue())
        self.assertIn("[Faltando]", out.getvalue())
