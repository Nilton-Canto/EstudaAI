# ===== IMPORTAÇÕES =====
# Importações do Django para renderização de páginas e redirecionamentos
from django.shortcuts import render, redirect
# render: função que gera e retorna uma página HTML para o usuário
# redirect: função que redireciona o usuário para outra URL após uma ação

# Importações para autenticação de usuários
from django.contrib.auth import authenticate, login
# authenticate: verifica se as credenciais (usuário/senha) são válidas
# login: cria uma sessão de usuário autenticado no sistema

# Formulário padrão do Django para autenticação
from django.contrib.auth.forms import AuthenticationForm
# AuthenticationForm: formulário pré-construído do Django para login

# Importação do formulário customizado de usuário
from .forms import UsuarioForm
# UsuarioForm: formulário personalizado para cadastro de novos usuários
# O ponto (.) indica que estamos importando da mesma pasta (app)

# Sistema de mensagens do Django
from django.contrib import messages
# messages: permite exibir mensagens de sucesso, erro, aviso, etc. para o usuário

from django.contrib.auth.decorators import login_required


# ===== VIEW DE CADASTRO =====
def signup(request):
    """
    View responsável pelo cadastro de novos usuários.
    
    Fluxo:
    1. Se for GET: exibe formulário vazio
    2. Se for POST: processa dados do formulário
       - Se válido: cria usuário e redireciona para login
       - Se inválido: exibe erros no formulário
    
    Args:
        request: objeto HttpRequest contendo dados da requisição
        
    Returns:
        HttpResponse: página de cadastro renderizada
    """
    
    # Verifica se a requisição é do tipo POST (envio de formulário)
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados
        form = UsuarioForm(request.POST)
        # request.POST contém todos os dados enviados via formulário
        
        # Valida se todos os campos estão corretos
        if form.is_valid():
            # Salva o usuário mas não confirma no banco ainda (commit=False)
            usuario = form.save(commit=False)
            
            # Criptografa a senha antes de salvar no banco
            # cleaned_data contém os dados já validados e limpos
            usuario.set_password(form.cleaned_data['password'])
            
            # Agora salva definitivamente no banco de dados
            usuario.save()
            
            # Exibe mensagem de sucesso para o usuário
            messages.success(request, 'Cadastro realizado com sucesso. Faça login.')
            
            # Redireciona para a página de login após cadastro bem-sucedido
            return redirect('usuarios:login')
            
        else:
            # Se o formulário tem erros, exibe mensagem de erro
            messages.error(request, 'Há erros no formulário. Verifique os campos.')
    
    else:
        # Se a requisição é GET, cria um formulário vazio
        form = UsuarioForm()
    
    # Renderiza a página de cadastro passando o formulário como contexto
    # O formulário pode estar vazio (GET) ou com dados/erros (POST inválido)
    return render(request, 'usuarios/signup.html', {'form': form})


# ===== VIEW DE LOGIN =====
def login_view(request):
    """
    View responsável pela autenticação de usuários.
    
    Fluxo:
    1. Se for GET: exibe formulário de login vazio
    2. Se for POST: processa credenciais
       - Se válidas: autentica usuário e redireciona
       - Se inválidas: exibe erro no formulário
    
    Args:
        request: objeto HttpRequest contendo dados da requisição
        
    Returns:
        HttpResponse: página de login renderizada ou redirecionamento
    """
    
    # Verifica se a requisição é do tipo POST (envio de credenciais)
    if request.method == 'POST':
        # Cria formulário de autenticação com os dados enviados
        form = AuthenticationForm(request, data=request.POST)
        # O primeiro parâmetro é a requisição atual
        # data= contém os dados do formulário (username e password)
        
        # Valida se as credenciais estão corretas
        if form.is_valid():
            # Obtém o usuário autenticado do formulário
            usuario = form.get_user()
            
            # Efetua o login criando uma sessão para o usuário
            login(request, usuario)
            # Isso permite que o usuário seja reconhecido em outras páginas
            
            # Redireciona para a página principal após login bem-sucedido
            return redirect('usuarios:dashboard')
            
        else:
            # Se as credenciais são inválidas, exibe mensagem de erro
            messages.error(request, 'Usuário ou senha inválidos.')
    
    else:
        # Se a requisição é GET, cria um formulário de login vazio
        form = AuthenticationForm()
    
    # Renderiza a página de login passando o formulário como contexto
    # O formulário pode estar vazio (GET) ou com erros (POST inválido)
    return render(request, 'usuarios/login.html', {'form': form})


@login_required(login_url='/usuarios/login/')   
def dashboard(request):
    
    """
    View para a página inicial após o login.
    Apenas usuários autenticados podem acessar esta página.
    
    Args:
        request: objeto HttpRequest contendo dados da requisição
        
    Returns:
        HttpResponse: página de dashboard renderizada
    """
    
    # Renderiza a página de dashboard
    return render(request, 'usuarios/dashboard.html')