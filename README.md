# 📚 EstudaAI

O **EstudaAI** é uma aplicação web desenvolvida para ajudar estudantes no **planejamento de estudos**, através da **recomendação de trilhas de aprendizagem**. O sistema permite ao aluno escolher entre **trilhas pré-definidas** ou criar **trilhas personalizadas com o apoio de um agente LLM (IA)**.

---

## 🚀 Projeto GitHub – Fluxo de Branches

👉 **Cada aluno deve criar uma branch própria para cada nova funcionalidade (feature branch).**

### Exemplo de criação de branch:
```bash
git checkout -b feature/criacao-de-trilhas
```

---

## 🔄 Fluxo de Trabalho (Pull Request Workflow)

1. ✅ **Criar a branch de feature** (exemplo: `feature/nome-da-feature`)
2. ✅ **Realizar commits frequentes e com mensagens claras**
3. ✅ **Enviar (push) sua branch para o GitHub**
4. ✅ **Abrir um Pull Request (PR)**
5. ✅ **Designar pelo menos 1 colega como revisor**

### 🎯 O que o revisor deve fazer:
- 👀 **Ler o código no GitHub**
- 💬 **Fazer comentários linha a linha (inline comments)**
- 🛠️ **Sugerir melhorias, correções ou ajustes**
- ✅ **Aprovar o PR após validação**

Após a aprovação ✅, o autor do PR realiza o **merge** para a branch principal (`main`).

---
## 🔄  Regras:

- ✅ Ninguém faz merge direto na main.
- ✅ Pull Requests para a main só podem vir da develop.
- ✅ Pull Requests para a develop só podem vir de feature branches (ex: feature/*).
- ✅ Proibido fazer PR de main → develop.
- ✅ Proibido fazer PR de develop → feature.

---

## 📝 Boas Práticas de Commit

- 🔁 **Commits pequenos e frequentes**
- ✏️ **Mensagens de commit claras e objetivas**
- ⚠️ **Antes de abrir o PR, sempre execute:**
```bash
git pull origin main
```
👉 Para garantir que sua branch está atualizada e evitar conflitos.

---

## 👀 Checklist para Revisores (Code Review)

Antes de aprovar um PR, verifique:

1. ✅ **Nome de variáveis** é adequado e expressivo.
2. ✅ **Clareza e legibilidade** do código.
3. ✅ **Divisão de responsabilidades** bem definida (nenhuma função fazendo "tudo").
4. ✅ **Cumprimento dos requisitos da issue relacionada**.
5. ✅ **Presença de testes**, se aplicável.
6. ✅ Só aprova PR se "base branch" correta (ex: feature/ para develop ou develop para main)

---

## 🚀 Configuração do Ambiente de Desenvolvimento

### 1. Clonar o Repositório
```bash
git clone https://github.com/Nilton-Canto/EstudaAI.git
cd EstudaAI
```

### 2. Criar Ambiente Virtual
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente
```bash
cd config
cp .env.example .env
```

Edite o arquivo `.env` e configure:
- **GEMINI_API_KEY**: Obtenha em [Google AI Studio](https://makersuite.google.com/app/apikey)
- **SECRET_KEY**: Gere uma chave segura para o Django
- **DEBUG**: `True` para desenvolvimento, `False` para produção

### 5. Executar Migrações
```bash
python manage.py migrate
```

### 6. Criar Superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 7. Executar o Servidor
```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

---

## 🔄 Pipeline CI/CD

Este projeto utiliza **GitHub Actions** para automação de CI/CD com três jobs principais:

### Triggers
- **Push** nas branches `main` e `develop`
- **Pull Requests** para `main` e `develop`

### Jobs Executados

#### 1. Test (Testes)
- ✅ Instala dependências
- ✅ Cria arquivo `.env` para testes
- ✅ Roda migrações do Django
- ✅ Executa pytest com cobertura mínima de 70%
- ✅ Upload de relatórios de cobertura como artifacts

#### 2. Lint (Qualidade de Código)
- ✅ **Black**: Verifica formatação do código
- ✅ **isort**: Verifica ordenação de imports
- ✅ **Flake8**: Análise de linting usando `setup.cfg`

#### 3. Security (Segurança)
- ✅ **Bandit**: Detecta vulnerabilidades de segurança
- ✅ Gera relatórios JSON
- ✅ Upload de relatórios como artifacts

---

## 🛠️ Testando CI/CD Localmente

### Opção 1: Script Automatizado
```bash
chmod +x run_ci_checks.sh
./run_ci_checks.sh
```

### Opção 2: Comandos Individuais

#### 1. Preparação
```bash
# Criar .env
cd config
cat > .env << EOF
GEMINI_API_KEY=test_key
DEBUG=True
SECRET_KEY=test-secret-key
EOF

# Instalar dependências
cd ..
pip install -r requirements.txt

# Migrações
cd config
python manage.py migrate
```

#### 2. Formatação
```bash
# Verificar
black --check --diff config/

# Corrigir automaticamente
black config/
```

#### 3. Imports
```bash
# Verificar
isort --check-only --diff config/

# Corrigir automaticamente
isort config/
```

#### 4. Linting
```bash
flake8 config/usuarios config/api_gemini config/config --config=setup.cfg
```

#### 5. Segurança
```bash
bandit -r config/usuarios config/api_gemini config/config --configfile .bandit
```

#### 6. Testes
```bash
cd config
pytest --cov=. --cov-report=html --cov-report=term-missing -v

# Ver relatório HTML
open htmlcov/index.html  # ou firefox/chrome htmlcov/index.html
```

---

## 📊 Cobertura de Testes

### Requisitos
- Cobertura mínima: **70%**
- Relatórios gerados:
  - `coverage.xml` - Para integrações
  - `htmlcov/` - Visualização interativa

### Visualizar Cobertura Local
```bash
cd config
pytest --cov=. --cov-report=html
python -m http.server 8000 --directory htmlcov
# Acesse: http://localhost:8000
```

---

## 🔧 Ferramentas Configuradas

### Arquivos de Configuração

| Ferramenta | Arquivo | Descrição |
|------------|---------|-----------|
| **pytest** | `pyproject.toml` | Configuração de testes |
| **coverage** | `pyproject.toml` | Relatórios de cobertura |
| **Black** | `pyproject.toml` | Formatação de código |
| **isort** | `pyproject.toml` | Ordenação de imports |
| **Flake8** | `setup.cfg` | Linting e PEP8 |
| **Bandit** | `.bandit` | Análise de segurança |

### Comandos Rápidos
```bash
# Formatar tudo
black config/ && isort config/

# Rodar todos os checks
flake8 config/usuarios config/api_gemini config/config --config=setup.cfg && \
bandit -r config/usuarios config/api_gemini config/config --configfile .bandit && \
cd config && pytest --cov=. -v

# Verificar vulnerabilidades em dependências
safety check
```

---

## 🐛 Troubleshooting

### Erro: "No module named 'X'"
```bash
pip install -r requirements.txt
```

### Erro: "DJANGO_SETTINGS_MODULE not set"
```bash
cd config
export DJANGO_SETTINGS_MODULE=config.settings
```

### Erro: "Database error"
```bash
cd config
python manage.py migrate
```

### Erro: "Pasta logs não encontrada"
A pasta `config/logs/` deve existir. Se não existir:
```bash
cd config
mkdir logs
```

### CI falha mas local funciona
- Certifique-se de estar usando Python 3.11
- Verifique se todos os arquivos estão commitados
- Rode `./run_ci_checks.sh` para simular o CI

### Black/isort falham
```bash
# Auto-corrigir
black config/
isort config/
git add .
git commit -m "style: auto-format code"
```

---

## 📦 Artifacts do CI

Após cada execução, os seguintes artifacts ficam disponíveis:

1. **coverage-report** - Relatórios de cobertura (XML + HTML)
2. **bandit-security-report** - Análise de segurança (JSON)

**Download**: GitHub Actions → Workflow Run → Artifacts (disponível por 90 dias)

---

## 🔐 Segurança

### Verificações Ativas
- ✅ Análise estática com Bandit
- ✅ Verificação de vulnerabilidades conhecidas
- ✅ Sem secrets hardcoded

### Recomendações
- Nunca commite `.env` (já está no `.gitignore`)
- Use GitHub Secrets para informações sensíveis
- Mantenha dependências atualizadas

---

## 📝 Adicionando Novos Testes

```python
# config/app/tests.py
import pytest
from django.test import TestCase

@pytest.mark.unit
class TestExample(TestCase):
    def test_something(self):
        assert True

@pytest.mark.integration
def test_api_integration():
    # Test code here
    pass
```

Rode testes específicos:
```bash
# Apenas testes unitários
pytest -m unit

# Apenas testes de integração
pytest -m integration

# Testes de uma app específica
pytest config/usuarios/tests.py
```

---

## 📚 Referências

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [pytest Documentation](https://docs.pytest.org/)
- [Black](https://black.readthedocs.io/)
- [Flake8](https://flake8.pycqa.org/)
- [Bandit](https://bandit.readthedocs.io/)
- [Django Documentation](https://docs.djangoproject.com/)
