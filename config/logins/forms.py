from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulário de criação/login de conta
class AccountSignupForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Senha", 
        widget=forms.PasswordInput(attrs={}),
    )
    # Confirmação da senha
    password2 = forms.CharField(
        label="Confirmação da Senha",
        widget=forms.PasswordInput(attrs={}),
    )

    class Meta: # Dados do formulário
        model = User
        fields = ['username', 'email', 'password1', 'password2']
