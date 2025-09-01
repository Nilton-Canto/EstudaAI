from django import forms #importando o forms do django
from .models import Usuario #importando o usuário que fizemos no models
from django.core.exceptions import ValidationError #

class UsuarioForm(forms.ModelForm): #classe do usuário no formulário. Conecta o formulário diretamente com o modelo Usuario
    password = forms.CharField(widget=forms.PasswordInput) #--> faz com que o campo de senha seja digitado como asteriscos no frontend.

    class Meta: #Classe Meta serve para configurar o comportamento do formulário
        model = Usuario #indica que o formulário está ligado à classe usuário
        fields = ['username','nome', 'email', 'universidade', 'curso', 'ano_formatura', 'idade', 'password'] #Quais campos queremos da classe usuários

    def clean_email(self): #função para verificar e tratar erro de email duplicado, pois o forms exige email unico
        email = self.cleaned_data.get('email') #Pega o valor digitado no campo "email" do formulário já tratado pelo Django,por isso cleaned data
        if email and Usuario.objects.filter(email__iexact=email).exists(): #Verifica se o usuário digitou algum email e se já existe outro usuário com esse mesmo email (sem diferenciar maiúsculas e minúsculas), filter retorna uma quer list e email__iexact=email verifica se é duplicado.
            raise ValidationError('Este e-mail já está em uso.')  #Se já existir, lança um erro de validação que será exibido no formulário
        return email #retorna o email caso não seja duplicado.