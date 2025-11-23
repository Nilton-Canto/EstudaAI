# EstudaAI - Guia de CI/CD

## 📋 Visão Geral

Este projeto utiliza **GitHub Actions** para automação de CI/CD com três jobs principais:

1. **Test** - Testes automatizados com cobertura
2. **Lint** - Verificação de qualidade de código
3. **Security** - Análise de segurança

## 🚀 Pipeline CI/CD

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

## 🛠️ Testando Localmente

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

## 📦 Artifacts do CI

Após cada execução, os seguintes artifacts ficam disponíveis:

1. **coverage-report** - Relatórios de cobertura (XML + HTML)
2. **bandit-security-report** - Análise de segurança (JSON)

**Download**: GitHub Actions → Workflow Run → Artifacts (disponível por 90 dias)

## 🔐 Segurança

### Verificações Ativas
- ✅ Análise estática com Bandit
- ✅ Verificação de vulnerabilidades conhecidas (Safety)
- ✅ Sem secrets hardcoded

### Recomendações
- Nunca commite `.env` (já está no `.gitignore`)
- Use GitHub Secrets para informações sensíveis
- Mantenha dependências atualizadas

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

## 🎯 Próximos Passos

1. **Codecov Integration** - Para tracking de cobertura visual
2. **Pre-commit Hooks** - Rodar checks antes de commit
3. **CD Pipeline** - Deploy automático após CI passar
4. **Docker** - Containerização para consistência

## 📚 Referências

- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [pytest Documentation](https://docs.pytest.org/)
- [Black](https://black.readthedocs.io/)
- [Flake8](https://flake8.pycqa.org/)
- [Bandit](https://bandit.readthedocs.io/)
