# Importações necessárias
from django import forms  # Sistema de formulários do Django
from django.core.exceptions import ValidationError  # Para lançar erros de validação

from .models import Usuario  # Modelo de usuário customizado


class UsuarioForm(forms.ModelForm):
    """
    Formulário para cadastro de novos usuários.
    Conecta diretamente com o modelo Usuario.
    """

    # Campo de senha com widget especial para ocultar o texto
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """Configurações do formulário"""

        model = Usuario  # Modelo associado
        fields = [
            "username",
            "nome",
            "email",
            "universidade",
            "curso",
            "ano_formatura",
            "idade",
            "password",
        ]  # Campos que aparecerão no formulário

    def clean_email(self):
        """
        Validação customizada para garantir email único.
        Chamada automaticamente pelo Django durante a validação.
        """
        email = self.cleaned_data.get("email")  # Obtém email já validado

        # Verifica se já existe usuário com este email (case-insensitive)
        if email and Usuario.objects.filter(email__iexact=email).exists():
            raise ValidationError("Este e-mail já está em uso.")

        return email  # Retorna email se válido
