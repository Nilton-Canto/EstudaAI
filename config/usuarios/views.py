from django.shortcuts import render, redirect #render serve para gerar e retornar uma página HTML para o usuário.
#já o redirect é para redirecionar o usuário para algum lugar após alguma ação, como por exemplo, salvar no banco de dados.

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .forms import UsuarioForm #importamos diretamente da mesma pasta, portanto, pode-se usar o "."

from django.contrib import messages #utilizado para menssagens 

def signup(request): #criando uma função do botão signup. O objeto resquest que a função recebe é tudo que vem do navegador
    if request.method == 'POST': #qual o método http usado, o POST.
        form = UsuarioForm(request.POST)#resquest.POST --> dados enviado via formulário
        if form.is_valid():#lógica para confirmar se o formulário enviado pelo post é valido, ou seja, se contém o conteúdo
            usuario = form.save(commit=False)#salvando o formulário no usuário
            usuario.set_password(form.cleaned_data['password'])  # criptografando a senha
            usuario.save()#salva o usuário
            messages.success(request, 'Cadastro realizado com sucesso. Faça login.')
            return redirect('login')  #redireciona para a página de login ou outra página após cadastro. ##Alterar o caminho que redireciona
        else: #caso o formulário não seja válido
            messages.error(request, 'Há erros no formulário. Verifique os campos.')
    else:
        form = UsuarioForm()#formulário vazo
    return render(request, 'usuarios/signup.html', {'form': form})#mostra a página de cadastro com o formulário(vazio ou preenchido)

def login_view(request): #criação da função de login
    if request.method == 'POST':## verificação do método

        form = AuthenticationForm(request, data=request.POST) #identifica a requisição atual e os dados do formulario de login

        if form.is_valid(): #verifica se o formulário é válido e se o usuario existe
            usuario = form.get_user()
            login(request, usuario) #função de login do django, cria a sessão.

            return redirect('home')  # redirecione para a futura página principal
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})#mostra a página de login com o formulário(vazio ou preenchido)