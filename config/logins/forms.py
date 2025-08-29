from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AccountSignupForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={}),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1',]
