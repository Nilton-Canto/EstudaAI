# ⚡ Quick Start - EstudaAI

Guia rápido para rodar o projeto em 5 minutos.

## Pré-requisitos

- Python 3.11+
- Git
- Chave API do Google Gemini ([obter aqui](https://makersuite.google.com/app/apikey))
﻿﻿
## Instalação Rápida

### 1. Clone e Entre no Diretório
```bash
git clone https://github.com/Nilton-Canto/EstudaAI.git
cd EstudaAI
```

### 2. Ambiente Virtual (Recomendado)
```bash
# Linux/Mac
python3 -m venv venv && source venv/bin/activate

# Windows
python -m venv venv && .\venv\Scripts\Activate.ps1
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar Ambiente
```bash
cd config
cp .env.example .env
```

**Edite o arquivo `.env`:**
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
GEMINI_API_KEY=sua-chave-gemini-aqui
```

### 5. Banco de Dados
```bash
python manage.py migrate
```

### 6. Rodar Servidor
```bash
python manage.py runserver
```

🎉 **Pronto!** Acesse: http://127.0.0.1:8000/

## 🔧 Comandos Úteis

```bash
# Criar superusuário
python manage.py createsuperuser

# Rodar testes
pytest

# Formatar código
black config/ && isort config/

# Verificar qualidade
flake8 config/ --config=../setup.cfg
```

## 🐛 Problemas Comuns

### "No module named django"
```bash
pip install -r requirements.txt
```

### "Database error"
```bash
python manage.py migrate
```

### "GEMINI_API_KEY not found"
- Verifique se o arquivo `.env` existe
- Confirme se a chave está correta

## Funcionalidades Principais

- **Login/Cadastro**: Sistema de autenticação
- **Trilhas IA**: Geração automática com Gemini
- **Progresso**: Acompanhamento de estudos
- **Admin**: Painel administrativo

## 🆘 Precisa de Ajuda?

- [Documentação Completa](README.md)
- [Guia de Contribuição](CONTRIBUTING.md)
- [Reportar Bug](https://github.com/Nilton-Canto/EstudaAI/issues)
