# ==== IMPORTAÇÕES =====
# Importações do Django para renderização de páginas e redirecionamentos
from datetime import timedelta

# Models
from api.models import Area, Trilha, TrilhaCurso, ProgressoTrilhaCurso

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

    # Buscar todas as trilhas do usuário (modelo unificado)
    trilhas = TrilhaCurso.objects.filter(
        usuario=request.user, ativa=True
    ).order_by("-data_criacao")
    
    # Calcular progresso para cada trilha
    trilhas_com_progresso = []
    total_atividades_geral = 0
    total_concluidas_geral = 0
    tempo_estudo_total = 0  # em minutos
    
    for trilha in trilhas:
        progressos = ProgressoTrilhaCurso.objects.filter(trilha=trilha)
        
        total_atividades = 0
        atividades_concluidas = 0
        
        # Contar atividades no JSON e somar tempo
        if isinstance(trilha.conteudo_json, dict):
            modulos = trilha.conteudo_json.get('modulos', [])
            for modulo in modulos:
                aulas = modulo.get('aulas', [])
                total_atividades += len(aulas)
                
                # Somar tempo de estudo das aulas concluídas
                for idx, aula in enumerate(aulas):
                    # Verificar se aula está concluída
                    modulo_idx = modulos.index(modulo)
                    identificador = f"mod_{modulo_idx}_aula_{idx}"
                    progresso = progressos.filter(identificador=identificador, concluida=True).first()
                    
                    if progresso:
                        # Extrair tempo de duração (formato: "45 min", "1h", "1h 30min", etc)
                        duracao = aula.get('duracao', '')
                        if duracao:
                            tempo_minutos = extrair_minutos_de_duracao(duracao)
                            tempo_estudo_total += tempo_minutos
        
        # Contar concluídas
        atividades_concluidas = progressos.filter(concluida=True).count()
        
        # Acumular para média geral
        total_atividades_geral += total_atividades
        total_concluidas_geral += atividades_concluidas
        
        # Calcular percentual
        percentual = 0
        if total_atividades > 0:
            percentual = int((atividades_concluidas / total_atividades) * 100)
        
        trilhas_com_progresso.append({
            'trilha': trilha,
            'percentual': percentual,
        })
    
    # Calcular média de conclusão geral
    media_conclusao = 0
    if total_atividades_geral > 0:
        media_conclusao = int((total_concluidas_geral / total_atividades_geral) * 100)
    
    # Formatar tempo de estudo
    if tempo_estudo_total >= 60:
        horas = tempo_estudo_total // 60
        minutos = tempo_estudo_total % 60
        if minutos > 0:
            tempo_estudo_formatado = f"{horas}h {minutos}min"
        else:
            tempo_estudo_formatado = f"{horas}h"
    else:
        tempo_estudo_formatado = f"{tempo_estudo_total}min"

    context = {
        "trilhas_com_progresso": trilhas_com_progresso,
        "total_trilhas": trilhas.count(),
        "media_conclusao": media_conclusao,
        "tempo_estudo": tempo_estudo_formatado,
    }

    # Renderiza a página de dashboard
    return render(request, "usuarios/dashboard.html", context)


def extrair_minutos_de_duracao(duracao_str):
    """
    Extrai minutos de strings de duração como "45 min", "1h", "1h 30min", etc.
    
    Args:
        duracao_str: String com a duração (ex: "45 min", "1h", "1h 30min")
    
    Returns:
        int: Total de minutos
    """
    import re
    
    duracao_str = duracao_str.lower().strip()
    total_minutos = 0
    
    # Extrair horas
    horas_match = re.search(r'(\d+)\s*h', duracao_str)
    if horas_match:
        total_minutos += int(horas_match.group(1)) * 60
    
    # Extrair minutos
    minutos_match = re.search(r'(\d+)\s*min', duracao_str)
    if minutos_match:
        total_minutos += int(minutos_match.group(1))
    
    return total_minutos


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
    total_trilhas = TrilhaCurso.objects.filter(ativa=True).count()

    # Usuários ativos hoje (que fizeram login nas últimas 24h)
    hoje = timezone.now()
    ontem = hoje - timedelta(days=1)
    usuarios_ativos_hoje = Usuario.objects.filter(last_login__gte=ontem).count()

    # Últimos usuários cadastrados
    ultimos_usuarios = Usuario.objects.order_by("-date_joined")[:5]

    # Últimas trilhas criadas
    ultimas_trilhas = TrilhaCurso.objects.select_related("usuario", "area").order_by(
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

    trilhas = TrilhaCurso.objects.select_related("usuario", "area").order_by("-data_criacao")

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
            import json
            # Tentar parsear como JSON, se falhar usar string vazia
            try:
                conteudo_json = json.loads(conteudo) if conteudo else {}
            except json.JSONDecodeError:
                conteudo_json = {"conteudo_texto": conteudo}
            
            trilha = TrilhaCurso.objects.create(
                titulo=titulo,
                descricao=descricao if descricao else "",
                usuario_id=usuario_id,
                area_id=area_id,
                solicitacao_original="Criado pelo admin",
                conteudo_json=conteudo_json,
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

    trilha = get_object_or_404(TrilhaCurso, pk=pk)

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
                import json
                # Tentar parsear como JSON
                try:
                    conteudo_json = json.loads(conteudo) if conteudo else {}
                except json.JSONDecodeError:
                    conteudo_json = {"conteudo_texto": conteudo}
                
                # Atualizar campos
                trilha.titulo = titulo
                trilha.descricao = descricao
                trilha.usuario_id = usuario_id
                trilha.area_id = area_id if area_id else None
                trilha.conteudo_json = conteudo_json
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
    """Desativa uma trilha (soft delete)"""

    trilha = get_object_or_404(TrilhaCurso, pk=pk)

    if request.method == "POST":
        titulo = trilha.titulo
        # Soft delete: apenas marca como inativa ao invés de deletar
        trilha.ativa = False
        trilha.save()
        messages.success(request, f"Trilha '{titulo}' desativada com sucesso!")

    return redirect("admin_trilhas_list")


@login_required
def chat_ia(request):
    """Página de chat com IA"""
    return render(request, "usuarios/chat_ia.html")


@login_required
def minhas_trilhas(request):
    """Exibe as trilhas ativas do usuário logado"""

    # Buscar apenas trilhas ATIVAS (modelo unificado)
    trilhas = TrilhaCurso.objects.filter(
        usuario=request.user, 
        ativa=True
    ).order_by("-data_criacao")

    context = {
        "trilhas": trilhas,
    }

    return render(request, "usuarios/minhastrilhas.html", context)


@login_required
def criar_trilha(request):
    """Permite ao usuário criar uma nova trilha com IA ou manualmente"""

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        descricao = request.POST.get("descricao", "").strip()
        conteudo = request.POST.get("conteudo", "").strip()
        ativa = request.POST.get("ativa") == "on"
        ai_prompt = request.POST.get("ai_prompt", "").strip()

        # Validar campos obrigatórios
        if not titulo:
            messages.error(request, "O título é obrigatório!")
            return render(request, "usuarios/criartrilha.html")

        if not conteudo:
            messages.error(request, "O conteúdo é obrigatório! Use a IA para gerar.")
            return render(request, "usuarios/criartrilha.html")

        try:
            # Tentar parsear o conteúdo como JSON
            import json
            try:
                conteudo_json = json.loads(conteudo)
            except json.JSONDecodeError:
                messages.error(request, "O conteúdo deve ser um JSON válido!")
                return render(request, "usuarios/criartrilha.html")

            # Criar trilha no modelo TrilhaCurso (para trilhas com IA)
            trilha = TrilhaCurso.objects.create(
                titulo=titulo,
                descricao=descricao if descricao else "",
                usuario=request.user,
                solicitacao_original=ai_prompt if ai_prompt else "Criação manual",
                conteudo_json=conteudo_json,
                ativa=ativa,
            )
            messages.success(request, f"✅ Trilha '{trilha.titulo}' criada com sucesso!")
            return redirect("minhas_trilhas")
        except Exception as e:
            messages.error(request, f"Erro ao criar trilha: {str(e)}")

    return render(request, "usuarios/criartrilha.html")


@login_required
def excluir_trilha(request, pk):
    """Permite ao usuário desativar (excluir) sua própria trilha"""
    
    if request.method == "POST":
        try:
            trilha = get_object_or_404(TrilhaCurso, pk=pk, usuario=request.user)
            
            titulo = trilha.titulo
            trilha.ativa = False
            trilha.save()
            
            messages.success(request, f"✅ Trilha '{titulo}' removida com sucesso!")
        except Exception as e:
            messages.error(request, f"❌ Erro ao remover trilha: {str(e)}")
    
    return redirect("minhas_trilhas")


@login_required
def ver_trilha(request, pk):
    """Exibe os detalhes completos de uma trilha com progresso"""
    
    trilha = get_object_or_404(TrilhaCurso, pk=pk, usuario=request.user)
    
    # Buscar progresso existente
    progressos = ProgressoTrilhaCurso.objects.filter(trilha=trilha)
    progresso_dict = {p.identificador: p for p in progressos}
    
    # Calcular estatísticas
    total_atividades = 0
    atividades_concluidas = 0
    
    # Processar o conteúdo JSON da trilha e enriquecer com progresso
    conteudo = trilha.conteudo_json
    modulos_enriquecidos = []
    
    if isinstance(conteudo, dict):
        modulos = conteudo.get('modulos', [])
        
        # Enriquecer cada módulo e aula com informações de progresso
        for mod_idx, modulo in enumerate(modulos):
            aulas_enriquecidas = []
            aulas = modulo.get('aulas', [])
            modulo_concluido = True  # Assume verdadeiro até encontrar aula não concluída
            aulas_concluidas_modulo = 0
            
            for aula_idx, aula in enumerate(aulas):
                total_atividades += 1
                identificador = f"mod_{mod_idx}_aula_{aula_idx}"
                progresso = progresso_dict.get(identificador)
                concluida = progresso.concluida if progresso else False
                
                if concluida:
                    atividades_concluidas += 1
                    aulas_concluidas_modulo += 1
                else:
                    modulo_concluido = False  # Se alguma aula não está concluída, módulo não está
                
                # Criar cópia da aula com informações extras
                aula_enriquecida = dict(aula)
                aula_enriquecida['identificador'] = identificador
                aula_enriquecida['concluida'] = concluida
                aula_enriquecida['modulo_indice'] = mod_idx
                aula_enriquecida['aula_indice'] = aula_idx
                aulas_enriquecidas.append(aula_enriquecida)
            
            # Calcular progresso do módulo
            percentual_modulo = 0
            if len(aulas) > 0:
                percentual_modulo = int((aulas_concluidas_modulo / len(aulas)) * 100)
            
            # Criar cópia do módulo com aulas enriquecidas
            modulo_enriquecido = dict(modulo)
            modulo_enriquecido['aulas'] = aulas_enriquecidas
            modulo_enriquecido['modulo_indice'] = mod_idx
            modulo_enriquecido['concluido'] = modulo_concluido
            modulo_enriquecido['total_aulas'] = len(aulas)
            modulo_enriquecido['aulas_concluidas'] = aulas_concluidas_modulo
            modulo_enriquecido['percentual'] = percentual_modulo
            modulos_enriquecidos.append(modulo_enriquecido)
    
    # Calcular percentual
    percentual_conclusao = 0
    if total_atividades > 0:
        percentual_conclusao = int((atividades_concluidas / total_atividades) * 100)
    
    context = {
        'trilha': trilha,
        'modulos': modulos_enriquecidos,
        'total_atividades': total_atividades,
        'atividades_concluidas': atividades_concluidas,
        'percentual_conclusao': percentual_conclusao,
    }
    
    return render(request, 'usuarios/ver_trilha.html', context)


@login_required
def marcar_atividade(request, pk):
    """Marca/desmarca uma atividade como concluída"""
    
    if request.method == "POST":
        trilha = get_object_or_404(TrilhaCurso, pk=pk, usuario=request.user)
        
        modulo_indice = int(request.POST.get('modulo_indice', 0))
        aula_indice = int(request.POST.get('aula_indice', 0))
        identificador = request.POST.get('identificador', '')
        concluida = request.POST.get('concluida', 'false') == 'true'
        
        # Buscar ou criar progresso
        progresso, created = ProgressoTrilhaCurso.objects.get_or_create(
            trilha=trilha,
            identificador=identificador,
            defaults={
                'modulo_indice': modulo_indice,
                'aula_indice': aula_indice,
                'concluida': concluida,
            }
        )
        
        # Se já existe, atualizar
        if not created:
            progresso.concluida = concluida
            if concluida:
                progresso.data_conclusao = timezone.now()
            else:
                progresso.data_conclusao = None
            progresso.save()
        else:
            if concluida:
                progresso.data_conclusao = timezone.now()
                progresso.save()
        
        return redirect('ver_trilha', pk=pk)
    
    return redirect('minhas_trilhas')


@login_required
def marcar_modulo(request, pk):
    """Marca/desmarca todas as atividades de um módulo como concluídas"""
    
    if request.method == "POST":
        trilha = get_object_or_404(TrilhaCurso, pk=pk, usuario=request.user)
        
        modulo_indice = int(request.POST.get('modulo_indice', 0))
        marcar_como = request.POST.get('marcar_como', 'marcar')
        concluir = (marcar_como == 'marcar')
        
        # Buscar todas as aulas do módulo no JSON
        conteudo = trilha.conteudo_json
        if isinstance(conteudo, dict):
            modulos = conteudo.get('modulos', [])
            if modulo_indice < len(modulos):
                modulo = modulos[modulo_indice]
                aulas = modulo.get('aulas', [])
                
                # Marcar/desmarcar todas as aulas do módulo
                for aula_idx in range(len(aulas)):
                    identificador = f"mod_{modulo_indice}_aula_{aula_idx}"
                    
                    progresso, created = ProgressoTrilhaCurso.objects.get_or_create(
                        trilha=trilha,
                        identificador=identificador,
                        defaults={
                            'modulo_indice': modulo_indice,
                            'aula_indice': aula_idx,
                            'concluida': concluir,
                            'data_conclusao': timezone.now() if concluir else None,
                        }
                    )
                    
                    if not created:
                        progresso.concluida = concluir
                        if concluir:
                            progresso.data_conclusao = timezone.now()
                        else:
                            progresso.data_conclusao = None
                        progresso.save()
        
        return redirect('ver_trilha', pk=pk)
    
    return redirect('minhas_trilhas')


# ===== VIEWS PARA TRILHAS PRÉ-DEFINIDAS =====

@login_required
def trilhas_disponiveis(request):
    """
    Exibe trilhas pré-definidas disponíveis para o aluno escolher.
    
    Funcionalidades:
    - Lista trilhas criadas por admin
    - Filtra por área de conhecimento
    - Mostra apenas trilhas ativas
    - Exclui trilhas já iniciadas pelo aluno
    """
    # Buscar usuário admin que criou as trilhas pré-definidas
    try:
        admin_user = Usuario.objects.get(username="admin_trilhas")
    except Usuario.DoesNotExist:
        admin_user = None
        messages.warning(
            request,
            "Nenhuma trilha pré-definida disponível. Execute: python manage.py populate_trilhas"
        )
    
    # Buscar todas as trilhas pré-definidas (criadas pelo admin)
    trilhas = TrilhaCurso.objects.filter(
        ativa=True
    ).select_related('area')
    
    if admin_user:
        trilhas = trilhas.filter(usuario=admin_user)
    
    # Filtrar por área se solicitado
    area_id = request.GET.get('area')
    if area_id:
        trilhas = trilhas.filter(area_id=area_id)
    
    # Buscar trilhas já iniciadas pelo usuário atual
    trilhas_iniciadas_ids = TrilhaCurso.objects.filter(
        usuario=request.user
    ).values_list('id', flat=True)
    
    # Marcar quais trilhas já foram iniciadas
    for trilha in trilhas:
        trilha.ja_iniciada = trilha.id in trilhas_iniciadas_ids
    
    # Buscar áreas ativas para filtro
    areas = Area.objects.filter(ativa=True).order_by('nome')
    
    contexto = {
        'trilhas': trilhas,
        'areas': areas,
        'area_selecionada': area_id,
    }
    
    return render(request, 'usuarios/trilhas_disponiveis.html', contexto)


@login_required
def trilha_detalhes_predefinida(request, pk):
    """
    Exibe detalhes completos de uma trilha pré-definida.
    """
    trilha = get_object_or_404(TrilhaCurso, pk=pk, ativa=True)
    
    # Verificar se usuário já iniciou esta trilha
    ja_iniciada = TrilhaCurso.objects.filter(
        usuario=request.user,
        titulo=trilha.titulo  # Mesma trilha baseada no título
    ).exists()
    
    # Calcular total de etapas (suporta 'aulas' e 'etapas')
    total_etapas = 0
    conteudo = trilha.conteudo_json
    if isinstance(conteudo, dict) and 'modulos' in conteudo:
        for modulo in conteudo['modulos']:
            aulas = modulo.get('aulas', modulo.get('etapas', []))
            total_etapas += len(aulas)
    
    contexto = {
        'trilha': trilha,
        'ja_iniciada': ja_iniciada,
        'total_etapas': total_etapas,
    }
    
    return render(request, 'usuarios/trilha_detalhes.html', contexto)


@login_required
def iniciar_trilha_predefinida(request, pk):
    """
    Copia uma trilha pré-definida para o aluno e cria registros de progresso.
    
    Validações:
    - Verifica se trilha existe e está ativa
    - Impede duplicação (aluno já tem esta trilha)
    - Cria cópia da trilha vinculada ao aluno
    - Cria registros de progresso para todas as etapas
    """
    if request.method != 'POST':
        messages.error(request, "Método inválido.")
        return redirect('trilhas_disponiveis')
    
    # Buscar trilha pré-definida (template)
    trilha_template = get_object_or_404(TrilhaCurso, pk=pk, ativa=True)
    
    # Verificar se aluno já possui esta trilha
    trilha_existente = TrilhaCurso.objects.filter(
        usuario=request.user,
        titulo=trilha_template.titulo
    ).first()
    
    if trilha_existente:
        messages.warning(
            request,
            f'Você já está seguindo a trilha "{trilha_template.titulo}". '
            f'Acesse "Minhas Trilhas" para continuar.'
        )
        return redirect('minhas_trilhas')
    
    # Criar cópia da trilha para o aluno
    nova_trilha = TrilhaCurso.objects.create(
        usuario=request.user,
        titulo=trilha_template.titulo,
        descricao=trilha_template.descricao,
        area=trilha_template.area,
        conteudo_json=trilha_template.conteudo_json,
        solicitacao_original="",  # Trilha pré-definida, não veio de IA
        ativa=True,
    )
    
    # Criar registros de progresso para todas as etapas
    conteudo = trilha_template.conteudo_json
    if isinstance(conteudo, dict) and 'modulos' in conteudo:
        for modulo_idx, modulo in enumerate(conteudo['modulos']):
            # Suporta tanto 'aulas' quanto 'etapas' para compatibilidade
            aulas = modulo.get('aulas', modulo.get('etapas', []))
            for aula_idx, aula in enumerate(aulas):
                # Criar identificador único seguindo o padrão do sistema
                identificador = f"mod_{modulo_idx}_aula_{aula_idx}"
                
                ProgressoTrilhaCurso.objects.create(
                    trilha=nova_trilha,
                    modulo_indice=modulo_idx,
                    aula_indice=aula_idx,
                    identificador=identificador,
                    concluida=False,
                )
    
    messages.success(
        request,
        f'Trilha "{nova_trilha.titulo}" adicionada com sucesso! Comece seus estudos agora.'
    )
    
    return redirect('ver_trilha', pk=nova_trilha.id)

