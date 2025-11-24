"""Configuração da aplicação API."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuração da aplicação de trilhas e áreas."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
    verbose_name = "API de Trilhas"

    def ready(self):
        """Executa quando a aplicação estiver pronta."""
        # Importar signals, tasks, etc aqui se necessário
        pass
