# 📚 EstudaAI

> **Sistema inteligente de planejamento de estudos com IA**

O **EstudaAI** é uma aplicação web que ajuda estudantes a criar e acompanhar **trilhas de aprendizagem personalizadas**. Utilizando **Inteligência Artificial (Google Gemini)**, o sistema gera trilhas estruturadas baseadas nas necessidades específicas de cada estudante.

## ✨ Funcionalidades

- 🤖 **Geração de trilhas com IA** - Trilhas personalizadas via Google Gemini
- 📋 **Trilhas pré-definidas** - Conteúdo curado por especialistas
- 📊 **Acompanhamento de progresso** - Visualização do desenvolvimento
- 👥 **Sistema de usuários** - Perfis acadêmicos personalizados
- 🎯 **Categorização por áreas** - Organização por domínios de conhecimento
- 📱 **Interface responsiva** - Funciona em desktop e mobile

## 🚀 Quick Start

**Quer testar rapidamente?** Siga o [**Guia de 5 minutos**](QUICKSTART.md)

```bash
git clone https://github.com/Nilton-Canto/EstudaAI.git
cd EstudaAI
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cd config && cp .env.example .env
# Configure GEMINI_API_KEY no .env
python manage.py migrate && python manage.py runserver
```

## 📋 Índice

- [🛠️ Instalação Completa](#️-instalação-completa)
- [🏗️ Arquitetura](#️-arquitetura)
- [🤝 Contribuição](#-contribuição)
- [🔄 Workflow Git](#-workflow-git)
- [🧪 Testes e CI/CD](#-testes-e-cicd)
- [📊 Diagramas UML](#-diagramas-uml)
- [🔐 Segurança](#-segurança)

## 🛠️ Instalação Completa

### Pré-requisitos
- **Python 3.11+**
- **Git**
- **Chave API Google Gemini** ([obter aqui](https://makersuite.google.com/app/apikey))

### 1. Clone do Repositório
```bash
git clone https://github.com/Nilton-Canto/EstudaAI.git
cd EstudaAI
```

### 2. Ambiente Virtual
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Dependências
```bash
pip install -r requirements.txt
```

### 4. Configuração
```bash
cd config
cp .env.example .env
```

**Configure o arquivo `.env`:**
```env
# Segurança
SECRET_KEY=sua-chave-secreta-django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Google Gemini IA
GEMINI_API_KEY=sua-chave-gemini-aqui
GEMINI_MODEL=gemini-2.0-flash

# CORS
CORS_ALLOW_ALL_ORIGINS=True
```

### 5. Banco de Dados
```bash
python manage.py migrate
```

### 6. Superusuário (Opcional)
```bash
python manage.py createsuperuser
```

### 7. Executar
```bash
python manage.py runserver
```

**🎉 Acesse:** http://127.0.0.1:8000/

## 🏗️ Arquitetura

### Estrutura do Projeto
```
EstudaAI/
├── config/                 # Configurações Django
│   ├── api/               # API e integração IA
│   ├── usuarios/          # Sistema de usuários
│   ├── config/            # Settings Django
│   └── manage.py
├── docs/                  # Documentação
│   ├── diagramas/         # UML e diagramas
│   └── casos-de-uso/      # Especificações
├── requirements.txt       # Dependências Python
└── README.md
```

### Tecnologias
- **Backend**: Django 5.2 + Django REST Framework
- **IA**: Google Gemini API
- **Banco**: SQLite (dev) / PostgreSQL (prod)
- **Frontend**: HTML, CSS, JavaScript
- **CI/CD**: GitHub Actions
- **Testes**: pytest + coverage

## 🤝 Contribuição

**Quer contribuir?** Leia o [**Guia de Contribuição**](CONTRIBUTING.md)

### Fluxo Rápido
```bash
# 1. Fork e clone seu fork
git clone https://github.com/SEU-USUARIO/EstudaAI.git

# 2. Criar branch feature
git checkout -b feature/sua-funcionalidade

# 3. Desenvolver e testar
./run_ci_checks.sh

# 4. Commit e push
git commit -m "feat: adiciona nova funcionalidade"
git push origin feature/sua-funcionalidade

# 5. Abrir Pull Request para develop
```

## 🔄 Workflow Git

### Branches
- **`main`** - Produção (apenas via develop)
- **`develop`** - Desenvolvimento (apenas via features)
- **`feature/*`** - Novas funcionalidades

### Regras
- ✅ PRs para `main` só de `develop`
- ✅ PRs para `develop` só de `feature/*`
- ✅ Pelo menos 1 revisor por PR
- ✅ CI deve passar (green)

### Commits
```bash
feat(api): adiciona endpoint de trilhas
fix(auth): corrige validação de login
docs(readme): atualiza documentação
style: aplica formatação black/isort
test(users): adiciona testes unitários
```

## 🧪 Testes e CI/CD

### Executar Testes Localmente
```bash
# Script automatizado
./run_ci_checks.sh

# Comandos individuais
black config/                              # Formatação
isort config/                              # Imports
flake8 config/ --config=setup.cfg          # Linting
bandit -r config/ --configfile .bandit     # Segurança
cd config && pytest --cov=. -v             # Testes
```

### Pipeline CI/CD
**Triggers:** Push/PR para `main` e `develop`

- **🧪 Tests**: pytest com 70% cobertura mínima
- **🎨 Lint**: Black, isort, Flake8
- **🔒 Security**: Bandit para vulnerabilidades

### Cobertura de Testes
```bash
cd config
pytest --cov=. --cov-report=html
python -m http.server 8000 --directory htmlcov
# Acesse: http://localhost:8000
```

## 📊 Diagramas UML

Documentação visual completa em [`docs/diagramas/`](docs/diagramas/):

- **Diagrama Conceitual** - Classes técnicas por domínios
- **Modelo de Domínio** - Conceitos de negócio
- **Casos de Uso** - Funcionalidades do sistema

**Visualizar:** https://www.plantuml.com/plantuml/uml/

## 🔐 Segurança

### Verificações Ativas
- ✅ **Bandit** - Análise estática de segurança
- ✅ **Safety** - Vulnerabilidades em dependências
- ✅ **Secrets** - Sem credenciais hardcoded

### Boas Práticas
- 🔑 Use `.env` para configurações sensíveis
- 🚫 Nunca commite `.env` (já no `.gitignore`)
- 🔄 Mantenha dependências atualizadas
- 🛡️ Use GitHub Secrets para CI/CD

## 🐛 Troubleshooting

### Problemas Comuns

**"No module named django"**
```bash
pip install -r requirements.txt
```

**"Database error"**
```bash
cd config && python manage.py migrate
```

**"GEMINI_API_KEY not found"**
- Verifique se `.env` existe em `config/`
- Confirme se a chave está correta

**CI falha mas local funciona**
```bash
# Simule o CI localmente
./run_ci_checks.sh
```

### Logs e Debug
```bash
# Logs do Django
tail -f config/logs/django.log

# Debug mode
# No .env: DEBUG=True
```

## 📚 Recursos

### Documentação
- 📖 [Django Docs](https://docs.djangoproject.com/)
- 🤖 [Google Gemini API](https://ai.google.dev/)
- 🧪 [pytest Docs](https://docs.pytest.org/)

### Ferramentas
- 🎨 [Black](https://black.readthedocs.io/) - Formatação
- 📦 [isort](https://pycqa.github.io/isort/) - Imports
- 🔍 [Flake8](https://flake8.pycqa.org/) - Linting
- 🛡️ [Bandit](https://bandit.readthedocs.io/) - Segurança

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Equipe

Desenvolvido com ❤️ pela equipe EstudaAI

---

**⭐ Se este projeto te ajudou, considere dar uma estrela!**
