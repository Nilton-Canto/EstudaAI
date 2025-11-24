"""Configuração da aplicação Usuários."""

from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    """Configuração da aplicação de usuários e autenticação."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "usuarios"
    verbose_name = "Usuários"

    def ready(self):
        """Executa quando a aplicação estiver pronta."""
        # Importar signals, tasks, etc aqui se necessário
        pass
