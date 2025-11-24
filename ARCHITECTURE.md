# 📁 Estrutura do Projeto EstudaAI

Este documento descreve a organização do projeto e as responsabilidades de cada arquivo/diretório.

## 🏗️ Arquitetura do Projeto

O projeto segue o padrão **MTV (Model-Template-View)** do Django com uma camada de **Service** para lógica de negócios complexa.

```
EstudaAI/
├── config/                      # Diretório principal do Django
│   ├── config/                  # Configurações do projeto
│   │   ├── settings.py          # Configurações principais (organizado em seções)
│   │   ├── urls.py              # URLs principais
│   │   ├── wsgi.py              # WSGI para deploy
│   │   └── asgi.py              # ASGI para async
│   │
│   ├── usuarios/                # App de usuários
│   │   ├── models.py            # Modelo Usuario (AbstractUser)
│   │   ├── views.py             # Views de autenticação
│   │   ├── forms.py             # Formulários
│   │   ├── urls.py              # URLs do app
│   │   ├── admin.py             # Configuração do admin
│   │   ├── apps.py              # Configuração da app
│   │   └── templates/           # Templates HTML
│   │
│   ├── api/                     # App principal da API
│   │   ├── models.py            # Models: Area, Trilha, Progresso, TrilhaCurso
│   │   ├── serializers.py       # Serializers DRF
│   │   ├── views.py             # Views da API REST (Trilhas/Áreas)
│   │   ├── views_gemini.py      # Views de integração com Gemini AI
│   │   ├── gemini.py            # Serviço do Gemini (GeminiService)
│   │   ├── urls.py              # URLs da API (inclui rotas Gemini)
│   │   ├── services.py          # Lógica de negócios
│   │   ├── constants.py         # Constantes e choices
│   │   ├── exceptions.py        # Exceções customizadas
│   │   ├── validators.py        # Validadores customizados
│   │   ├── admin.py             # Configuração do admin
│   │   ├── apps.py              # Configuração da app
│   │   ├── templates/api/       # Templates de teste
│   │   │   └── test_gemini.html # Interface de teste da API
│   │   └── management/          # Comandos personalizados
│   │       └── commands/
│   │           ├── seed_db.py   # Popular banco com dados iniciais
│   │           └── populate_areas.py
│   │
│   ├── logs/                    # Logs da aplicação
│   │   └── django.log           # Log principal
│   │
│   ├── staticfiles/             # Arquivos estáticos coletados
│   ├── media/                   # Uploads de usuários
│   ├── db.sqlite3               # Banco de dados SQLite
│   └── manage.py                # Script de gerenciamento Django
│
├── .github/                     # Configurações do GitHub
│   └── workflows/               # CI/CD workflows
│       └── ci.yml               # Pipeline de testes e qualidade
│
├── .gitignore                   # Arquivos ignorados pelo Git
├── .env.example                 # Template de variáveis de ambiente
├── requirements.txt             # Dependências Python
├── pytest.ini                   # Configuração do pytest
├── pyproject.toml               # Configuração Black/isort/coverage
├── setup.cfg                    # Configuração Flake8
├── SETUP.md                     # Guia de configuração
├── README.md                    # Documentação principal
└── ARCHITECTURE.md              # Este arquivo
```

## 📦 Responsabilidades dos Módulos

### 🔧 config/config/settings.py

Configurações do projeto organizadas em seções:

- **Paths e Configurações Básicas**: Caminhos do projeto
- **Segurança**: SECRET_KEY, DEBUG, ALLOWED_HOSTS
- **Aplicações**: INSTALLED_APPS organizados
- **Middleware**: Middlewares em ordem correta
- **Templates**: Configuração de templates
- **Banco de Dados**: Configuração do SQLite
- **Autenticação**: Validadores de senha
- **Internacionalização**: Idioma e timezone
- **Arquivos Estáticos**: STATIC e MEDIA
- **Django REST Framework**: Configurações da API
- **CORS**: Configurações de cross-origin
- **Integrações Externas**: Gemini API
- **Logging**: Sistema de logs
- **Configurações Adicionais**: Segurança, sessões, etc.

### 👤 usuarios/

**Responsabilidade**: Gerenciamento de usuários e autenticação

- **models.py**: Modelo `Usuario` customizado (herda AbstractUser)
- **views.py**: Login, logout, signup, dashboard
- **forms.py**: Formulários de autenticação
- **templates/**: Templates HTML para páginas de usuário

### 🎓 api/

**Responsabilidade**: Gerenciamento de trilhas e áreas de conhecimento

#### Camadas:

1. **Models** (`models.py`):
   - `Area`: Áreas de conhecimento
   - `Trilha`: Trilhas de estudo
   - `Progresso`: Progresso do usuário

2. **Serializers** (`serializers.py`):
   - Conversão entre modelos e JSON
   - Validação de dados da API

3. **Views** (`views.py`):
   - Endpoints da API REST
   - Delegates lógica complexa para Services

4. **Services** (`services.py`):
   - `TrilhaService`: Lógica de negócios de trilhas
   - `AreaService`: Lógica de negócios de áreas
   - Transações, validações, regras de negócio

5. **Constants** (`constants.py`):
   - Choices (STATUS, DIFICULDADE)
   - Cores padrão
   - Limites e configurações

6. **Exceptions** (`exceptions.py`):
   - Exceções customizadas da API
   - Mensagens de erro padronizadas
   - Inclui exceções do Gemini AI

7. **Validators** (`validators.py`):
   - Validadores customizados
   - Validação de cores, JSON, etc.

8. **Gemini Integration**:
   - `gemini.py`: Serviço de integração com Gemini AI (GeminiService)
   - `views_gemini.py`: Endpoints de geração de trilhas com IA
   - `templates/api/test_gemini.html`: Interface de teste

## 🎯 Padrões de Código

### ✅ Boas Práticas Aplicadas

1. **Separação de Responsabilidades**:
   - Models: Apenas estrutura de dados
   - Views: Apenas controle de requisições
   - Services: Lógica de negócios
   - Serializers: Validação e transformação

2. **DRY (Don't Repeat Yourself)**:
   - Constants centralizados
   - Services reutilizáveis
   - Exceptions padronizadas

3. **Nomenclatura**:
   - Classes: PascalCase
   - Funções/métodos: snake_case
   - Constantes: UPPER_SNAKE_CASE
   - Arquivos: snake_case

4. **Docstrings**:
   - Todas as classes e métodos documentados
   - Formato Google docstring style

5. **Type Hints** (em implementação):
   - Parâmetros tipados
   - Retornos tipados

## 🔄 Fluxo de Dados

### Criação de Trilha:

```
1. Usuario faz POST /api/trilhas/
   ↓
2. TrilhaListCreateView recebe requisição
   ↓
3. TrilhaSerializer valida dados
   ↓
4. TrilhaService.criar_trilha() executa lógica
   ↓
5. Verifica limites e regras de negócio
   ↓
6. Cria Trilha no banco (transaction)
   ↓
7. Retorna serializado para o cliente
```

## 🧪 Testes

- **Unit Tests**: Testam services, validators, etc.
- **Integration Tests**: Testam views, APIs
- **Fixtures**: Dados de teste reutilizáveis

## 📝 Comandos Úteis

```bash
# Criar migrations
python manage.py makemigrations

# Aplicar migrations
python manage.py migrate

# Popular banco
python manage.py seed_db

# Criar superusuário
python manage.py createsuperuser

# Rodar servidor
python manage.py runserver

# Executar testes
pytest

# Verificar código
black config/
isort config/
flake8 config/
```

## 🔐 Segurança

- SECRET_KEY via variável de ambiente
- Senhas hasheadas com PBKDF2
- CSRF protection habilitado
- Session security configurado
- HTTPS redirect em produção

## 📊 Performance

- Select_related em queries de Foreign Keys
- Prefetch_related para Many-to-Many
- Paginação em todas as listas
- Índices nos campos frequentemente buscados

## 🚀 Deploy

Ver `SETUP.md` para instruções detalhadas de deploy.
