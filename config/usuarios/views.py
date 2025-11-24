# ==== IMPORTAÇÕES =====
# Importações do Django para renderização de páginas e redirecionamentos
from datetime import timedelta

# Models
from api.models import Area, Trilha, TrilhaCurso

# Sistema de mensagens do Django
from django.contrib import messages

# Importações para autenticação de usuários
from django.contrib.auth import get_user_model, login, logout

# Decorators para proteção de views
from django.contrib.auth.decorators import login_required, user_passes_test

# Formulário padrão do Django para autenticação
from django.contrib.auth.forms import AuthenticationForm

# Paginação
from django.core.paginator import Paginator

# Database
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

# Importação do formulário customizado de usuário
from .forms import UsuarioForm

# render: função que gera e retorna uma página HTML para o usuário
# redirect: função que redireciona o usuário para outra URL após uma ação
# get_object_or_404: busca objeto ou retorna erro 404


# authenticate: verifica se as credenciais (usuário/senha) são válidas
# login: cria uma sessão de usuário autenticado no sistema
# get_user_model: retorna o modelo de usuário ativo


# AuthenticationForm: formulário pré-construído do Django para login


# UsuarioForm: formulário personalizado para cadastro de novos usuários
# O ponto (.) indica que estamos importando da mesma pasta (app)


# messages: permite exibir mensagens de sucesso, erro, aviso, etc. para o usuário


# login_required: exige que usuário esteja autenticado
# user_passes_test: testa condições customizadas (ex: é admin)


# Paginator: divide querysets em páginas


# Importa modelos de Área e Trilha


# Obter modelo de usuário
Usuario = get_user_model()


# ===== VIEW DA LANDING PAGE =====
def home(request):
    """
    View responsável pela página inicial (landing page) do sistema.
    
    Esta é a primeira página que o usuário vê ao acessar o site.
    Apresenta o sistema e oferece opções de login/cadastro.
    
    Args:
        request: objeto HttpRequest contendo dados da requisição
    
    Returns:
        HttpResponse: página inicial renderizada
    """
    return render(request, "usuarios/home.html")


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
    if request.method == "POST":
        # Cria uma instância do formulário com os dados enviados
        form = UsuarioForm(request.POST)
        # request.POST contém todos os dados enviados via formulário

        # Valida se todos os campos estão corretos
        if form.is_valid():
            # Salva o usuário mas não confirma no banco ainda (commit=False)
            usuario = form.save(commit=False)

            # Criptografa a senha antes de salvar no banco
            # cleaned_data contém os dados já validados e limpos
            usuario.set_password(form.cleaned_data["password"])

            # Agora salva definitivamente no banco de dados
            usuario.save()

            # Exibe mensagem de sucesso para o usuário
            messages.success(request, "Cadastro realizado com sucesso. Faça login.")

            # Redireciona para a página de login após cadastro bem-sucedido
            return redirect("login")

        else:
            # Se o formulário tem erros, exibe mensagem de erro
            messages.error(request, "Há erros no formulário. Verifique os campos.")

    else:
        # Se a requisição é GET, cria um formulário vazio
        form = UsuarioForm()

    # Renderiza a página de cadastro passando o formulário como contexto
    # O formulário pode estar vazio (GET) ou com dados/erros (POST inválido)
    return render(request, "usuarios/signup.html", {"form": form})


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
    if request.method == "POST":
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
            return redirect("dashboard")

        else:
            # Se as credenciais são inválidas, exibe mensagem de erro
            messages.error(request, "Usuário ou senha inválidos.")

    else:
        # Se a requisição é GET, cria um formulário de login vazio
        form = AuthenticationForm()

    # Renderiza a página de login passando o formulário como contexto
    # O formulário pode estar vazio (GET) ou com erros (POST inválido)
    return render(request, "usuarios/login.html", {"form": form})


# ===== VIEW DE LOGOUT =====
def logout_view(request):
    """
    View responsável por deslogar o usuário.

    Destrói a sessão do usuário e redireciona para a página de login.

    Args:
        request: objeto HttpRequest contendo dados da requisição

    Returns:
        HttpResponse: redirecionamento para página de login
    """
    logout(request)
    messages.success(request, "Você saiu da sua conta com sucesso.")
    return redirect("login")


@login_required(login_url="login")
def dashboard(request):
    """
    View para a página inicial após o login.
    Apenas usuários autenticados podem acessar esta página.

    Args:
        request: objeto HttpRequest contendo dados da requisição

    Returns:
        HttpResponse: página de dashboard renderizada
    """
    # Consumir e limpar mensagens de autenticação para que não apareçam em outras páginas
    from django.contrib.messages import get_messages

    storage = get_messages(request)
    for message in storage:
        pass  # Apenas consome as mensagens sem fazer nada com elas

    # Buscar trilhas personalizadas do usuário
    trilhas_curso = TrilhaCurso.objects.filter(
        usuario=request.user, ativa=True
    ).order_by("-data_criacao")

    # Buscar trilhas pré-definidas do usuário (se houver lógica para isso)
    trilhas_predefinidas = Trilha.objects.filter(
        usuario=request.user, ativa=True
    ).order_by("-data_criacao")

    # Combinar ou passar separadamente. Por enquanto, vamos focar nas trilhas de curso (personalizadas)
    # pois é o foco da integração com LLM.

    context = {
        "trilhas_curso": trilhas_curso,
        "trilhas_predefinidas": trilhas_predefinidas,
        "total_trilhas": trilhas_curso.count() + trilhas_predefinidas.count(),
    }

    # Renderiza a página de dashboard
    return render(request, "usuarios/dashboard.html", context)


# ===== HELPERS =====
def user_is_staff(user):
    """Verifica se o usuário é administrador"""
    return user.is_staff


# ===== VIEWS ADMINISTRATIVAS =====


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_dashboard(request):
    """Dashboard administrativo com estatísticas"""

    # Estatísticas gerais
    total_usuarios = Usuario.objects.count()
    total_areas = Area.objects.count()
    total_trilhas = Trilha.objects.filter(ativa=True).count()

    # Usuários ativos hoje (que fizeram login nas últimas 24h)
    hoje = timezone.now()
    ontem = hoje - timedelta(days=1)
    usuarios_ativos_hoje = Usuario.objects.filter(last_login__gte=ontem).count()

    # Últimos usuários cadastrados
    ultimos_usuarios = Usuario.objects.order_by("-date_joined")[:5]

    # Últimas trilhas criadas
    ultimas_trilhas = Trilha.objects.select_related("usuario", "area").order_by(
        "-data_criacao"
    )[:5]

    context = {
        "total_usuarios": total_usuarios,
        "total_areas": total_areas,
        "total_trilhas": total_trilhas,
        "usuarios_ativos_hoje": usuarios_ativos_hoje,
        "ultimos_usuarios": ultimos_usuarios,
        "ultimas_trilhas": ultimas_trilhas,
    }

    return render(request, "usuarios/admin/admin_dashboard.html", context)


# ===== CRUD USUÁRIOS =====


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_usuarios_list(request):
    """Lista todos os usuários com paginação e filtros"""

    # Query base
    usuarios = Usuario.objects.all().order_by("-date_joined")

    # Filtro de busca
    query = request.GET.get("q")
    if query:
        usuarios = usuarios.filter(
            Q(nome__icontains=query)
            | Q(email__icontains=query)
            | Q(username__icontains=query)
            | Q(universidade__icontains=query)
            | Q(curso__icontains=query)
        )

    # Filtro de status
    filtro = request.GET.get("filtro")
    if filtro == "ativos":
        usuarios = usuarios.filter(is_active=True)
    elif filtro == "inativos":
        usuarios = usuarios.filter(is_active=False)
    elif filtro == "staff":
        usuarios = usuarios.filter(is_staff=True)

    # Paginação
    paginator = Paginator(usuarios, 15)  # 15 por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "usuarios/admin/usuarios_list.html", {"page_obj": page_obj})


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_usuario_create(request):
    """Cria um novo usuário"""

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        nome = request.POST.get("nome")
        idade = request.POST.get("idade") or None
        universidade = request.POST.get("universidade")
        curso = request.POST.get("curso")
        ano_formatura = request.POST.get("ano_formatura") or None
        is_staff = request.POST.get("is_staff") == "on"
        is_active = request.POST.get("is_active") == "on"

        try:
            usuario = Usuario.objects.create_user(
                username=username,
                email=email,
                password=password,
                nome=nome,
                idade=idade,
                universidade=universidade,
                curso=curso,
                ano_formatura=ano_formatura,
                is_staff=is_staff,
                is_active=is_active,
            )
            messages.success(request, f"Usuário {usuario.nome} criado com sucesso!")
            return redirect("admin_usuarios_list")
        except Exception as e:
            messages.error(request, f"Erro ao criar usuário: {str(e)}")

    return render(request, "usuarios/admin/usuario_form.html")


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_usuario_edit(request, pk):
    """Edita um usuário existente"""

    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == "POST":
        usuario.username = request.POST.get("username")
        usuario.email = request.POST.get("email")
        usuario.nome = request.POST.get("nome")
        usuario.idade = request.POST.get("idade") or None
        usuario.universidade = request.POST.get("universidade")
        usuario.curso = request.POST.get("curso")
        usuario.ano_formatura = request.POST.get("ano_formatura") or None
        usuario.is_staff = request.POST.get("is_staff") == "on"
        usuario.is_active = request.POST.get("is_active") == "on"

        try:
            usuario.save()
            messages.success(request, f"Usuário {usuario.nome} atualizado com sucesso!")
            return redirect("admin_usuarios_list")
        except Exception as e:
            messages.error(request, f"Erro ao atualizar usuário: {str(e)}")

    return render(request, "usuarios/admin/usuario_form.html", {"usuario": usuario})


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_usuario_delete(request, pk):
    """Exclui um usuário"""

    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == "POST":
        nome = usuario.nome
        usuario.delete()
        messages.success(request, f"Usuário {nome} excluído com sucesso!")

    return redirect("admin_usuarios_list")


# ===== CRUD ÁREAS =====


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_areas_list(request):
    """Lista todas as áreas"""

    areas = Area.objects.all().order_by("nome")

    # Paginação
    paginator = Paginator(areas, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "usuarios/admin/areas_list.html", {"page_obj": page_obj})


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_area_create(request):
    """Cria uma nova área"""

    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        icone = request.POST.get("icone")
        cor = request.POST.get("cor")
        ativa = request.POST.get("ativa") == "on"

        try:
            area = Area.objects.create(
                nome=nome, descricao=descricao, icone=icone, cor=cor, ativa=ativa
            )
            messages.success(request, f"Área {area.nome} criada com sucesso!")
            return redirect("admin_areas_list")
        except Exception as e:
            messages.error(request, f"Erro ao criar área: {str(e)}")

    return render(request, "usuarios/admin/area_form.html")


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_area_edit(request, pk):
    """Edita uma área existente"""

    area = get_object_or_404(Area, pk=pk)

    if request.method == "POST":
        area.nome = request.POST.get("nome")
        area.descricao = request.POST.get("descricao")
        area.icone = request.POST.get("icone")
        area.cor = request.POST.get("cor")
        area.ativa = request.POST.get("ativa") == "on"

        try:
            area.save()
            messages.success(request, f"Área {area.nome} atualizada com sucesso!")
            return redirect("admin_areas_list")
        except Exception as e:
            messages.error(request, f"Erro ao atualizar área: {str(e)}")

    return render(request, "usuarios/admin/area_form.html", {"area": area})


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_area_delete(request, pk):
    """Exclui uma área"""

    area = get_object_or_404(Area, pk=pk)

    if request.method == "POST":
        nome = area.nome
        area.delete()
        messages.success(request, f"Área {nome} excluída com sucesso!")

    return redirect("admin_areas_list")


# ===== CRUD TRILHAS =====


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_trilhas_list(request):
    """Lista todas as trilhas"""

    trilhas = Trilha.objects.select_related("usuario", "area").order_by("-data_criacao")

    # Filtro de busca
    query = request.GET.get("q")
    if query:
        trilhas = trilhas.filter(
            Q(titulo__icontains=query) | Q(usuario__nome__icontains=query)
        )

    # Filtro de status
    filtro = request.GET.get("filtro")
    if filtro == "ativas":
        trilhas = trilhas.filter(ativa=True)
    elif filtro == "inativas":
        trilhas = trilhas.filter(ativa=False)

    # Paginação
    paginator = Paginator(trilhas, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "usuarios/admin/trilhas_list.html", {"page_obj": page_obj})


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_trilha_create(request):
    """Cria uma nova trilha"""

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao", "")  # Vazio por padrão
        usuario_id = request.POST.get("usuario")
        area_id = request.POST.get("area") or None
        conteudo = request.POST.get("conteudo", "")
        ativa = request.POST.get("ativa") == "on"

        try:
            trilha = Trilha.objects.create(
                titulo=titulo,
                descricao=descricao if descricao else "",  # Garantir string vazia
                usuario_id=usuario_id,
                area_id=area_id,
                conteudo=conteudo,
                ativa=ativa,
            )
            messages.success(request, f"Trilha {trilha.titulo} criada com sucesso!")
            return redirect("admin_trilhas_list")
        except Exception as e:
            messages.error(request, f"Erro ao criar trilha: {str(e)}")

    usuarios = Usuario.objects.filter(is_active=True).order_by("nome")
    areas = Area.objects.filter(ativa=True).order_by("nome")

    return render(
        request,
        "usuarios/admin/trilha_form.html",
        {"usuarios": usuarios, "areas": areas},
    )


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_trilha_edit(request, pk):
    """Edita uma trilha existente"""

    trilha = get_object_or_404(Trilha, pk=pk)

    if request.method == "POST":
        # Capturar valores do POST
        titulo = request.POST.get("titulo", "").strip()
        descricao = request.POST.get("descricao", "").strip()
        usuario_id = request.POST.get("usuario")
        area_id = request.POST.get("area")
        conteudo = request.POST.get("conteudo", "").strip()
        ativa = request.POST.get("ativa") == "on"

        # Validar campos obrigatórios
        if not titulo:
            messages.error(request, "O título é obrigatório!")
        elif not usuario_id:
            messages.error(request, "Selecione um usuário!")
        elif not conteudo:
            messages.error(request, "O conteúdo é obrigatório!")
        else:
            try:
                # Atualizar campos
                trilha.titulo = titulo
                trilha.descricao = descricao
                trilha.usuario_id = usuario_id
                trilha.area_id = area_id if area_id else None
                trilha.conteudo = conteudo
                trilha.ativa = ativa

                # Salvar no banco
                trilha.save()

                messages.success(
                    request, f'✅ Trilha "{trilha.titulo}" atualizada com sucesso!'
                )
                return redirect("admin_trilhas_list")

            except Exception as e:
                messages.error(request, f"❌ Erro ao atualizar trilha: {str(e)}")

    usuarios = Usuario.objects.filter(is_active=True).order_by("nome")
    areas = Area.objects.filter(ativa=True).order_by("nome")

    return render(
        request,
        "usuarios/admin/trilha_form.html",
        {"trilha": trilha, "usuarios": usuarios, "areas": areas},
    )


@login_required(login_url="login")
@user_passes_test(user_is_staff, login_url="dashboard")
def admin_trilha_delete(request, pk):
    """Exclui uma trilha"""

    trilha = get_object_or_404(Trilha, pk=pk)

    if request.method == "POST":
        titulo = trilha.titulo
        trilha.delete()
        messages.success(request, f"Trilha {titulo} excluída com sucesso!")

    return redirect("admin_trilhas_list")


@login_required
def chat_ia(request):
    """Página de chat com IA"""
    return render(request, "usuarios/chat_ia.html")


@login_required
def minhas_trilhas(request):
    """Exibe as trilhas do usuário logado"""

    trilhas = Trilha.objects.filter(usuario=request.user).order_by("-data_criacao")

    return render(request, "usuarios/minhastrilhas.html", {"trilhas": trilhas})


@login_required
def criar_trilha(request):
    """Permite ao usuário criar uma nova trilha"""

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao", "")
        conteudo = request.POST.get("conteudo", "")
        ativa = request.POST.get("ativa") == "on"

        try:
            trilha = Trilha.objects.create(
                titulo=titulo,
                descricao=descricao if descricao else "",
                usuario=request.user,
                conteudo=conteudo,
                ativa=ativa,
            )
            messages.success(request, f"Trilha {trilha.titulo} criada com sucesso!")
            return redirect("minhas_trilhas")
        except Exception as e:
            messages.error(request, f"Erro ao criar trilha: {str(e)}")

    return render(request, "usuarios/criartrilha.html")
