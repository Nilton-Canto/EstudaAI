# 🤝 Guia de Contribuição - EstudaAI

Obrigado por seu interesse em contribuir com o EstudaAI! Este guia te ajudará a começar.

## 🚀 Primeiros Passos

### 1. Fork e Clone
```bash
# Fork no GitHub, depois clone seu fork
git clone https://github.com/SEU-USUARIO/EstudaAI.git
cd EstudaAI
```

### 2. Configuração do Ambiente
```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou .\venv\Scripts\Activate.ps1  # Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar .env
cd config
cp .env.example .env
# Edite .env com suas configurações
```

### 3. Executar Projeto
```bash
cd config
python manage.py migrate
python manage.py runserver
```

## 🔄 Fluxo de Contribuição

### 1. Criar Branch Feature
```bash
git checkout develop
git pull origin develop
git checkout -b feature/sua-funcionalidade
```

### 2. Desenvolver
- Faça commits pequenos e frequentes
- Use mensagens descritivas
- Siga os padrões de código

### 3. Testar Localmente
```bash
# Rodar todos os checks
./run_ci_checks.sh

# Ou individualmente:
black config/
isort config/
flake8 config/ --config=setup.cfg
cd config && pytest --cov=. -v
```

### 4. Abrir Pull Request
- Base: `develop`
- Título claro e descritivo
- Descrição detalhada das mudanças
- Adicionar reviewers

## 📋 Padrões de Código

### Commits
```bash
# Formato: tipo(escopo): descrição
feat(api): adiciona endpoint de trilhas
fix(auth): corrige validação de login
docs(readme): atualiza instruções de setup
style(format): aplica black e isort
test(users): adiciona testes de usuário
```

### Python
- **Black** para formatação
- **isort** para imports
- **Flake8** para linting
- **Docstrings** em funções públicas
- **Type hints** quando possível

### Django
- Models em `models.py`
- Views em `views.py`
- URLs em `urls.py`
- Testes em `tests.py`

## 🧪 Testes

### Executar Testes
```bash
cd config
pytest -v                    # Todos os testes
pytest -m unit              # Apenas unitários
pytest -m integration       # Apenas integração
pytest --cov=. --cov-report=html  # Com cobertura
```

### Escrever Testes
```python
import pytest
from django.test import TestCase

@pytest.mark.unit
class TestModel(TestCase):
    def test_create_user(self):
        # Teste aqui
        pass

@pytest.mark.integration
def test_api_endpoint():
    # Teste de integração
    pass
```

## 🔍 Code Review

### Para Autores
- [ ] Código testado localmente
- [ ] CI passando (green)
- [ ] Descrição clara no PR
- [ ] Screenshots se necessário
- [ ] Documentação atualizada

### Para Reviewers
- [ ] Funcionalidade funciona
- [ ] Código legível e bem estruturado
- [ ] Testes adequados
- [ ] Sem vulnerabilidades
- [ ] Segue padrões do projeto

## 🐛 Reportar Bugs

### Template de Issue
```markdown
**Descrição do Bug**
Descrição clara do problema.

**Passos para Reproduzir**
1. Vá para '...'
2. Clique em '...'
3. Veja o erro

**Comportamento Esperado**
O que deveria acontecer.

**Screenshots**
Se aplicável, adicione screenshots.

**Ambiente**
- OS: [Windows/Mac/Linux]
- Python: [versão]
- Browser: [se aplicável]
```

## 💡 Sugerir Funcionalidades

### Template de Feature Request
```markdown
**Problema/Necessidade**
Qual problema esta funcionalidade resolve?

**Solução Proposta**
Descrição da funcionalidade desejada.

**Alternativas Consideradas**
Outras soluções que você considerou.

**Contexto Adicional**
Qualquer informação extra relevante.
```

## 📚 Recursos Úteis

- [Django Documentation](https://docs.djangoproject.com/)
- [Python PEP 8](https://pep8.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Conventional Commits](https://www.conventionalcommits.org/)

## ❓ Dúvidas?

- Abra uma [Issue](https://github.com/Nilton-Canto/EstudaAI/issues)
- Entre em contato com os maintainers
- Consulte a documentação existente

---

**Obrigado por contribuir! 🎉**