# 🔑 CONFIGURAÇÃO DO ARQUIVO .ENV

## ⚠️ IMPORTANTE: Você precisa criar o arquivo .env manualmente!

### 1. Crie um arquivo chamado `.env` na pasta `config/` (mesmo nível do `manage.py`)

### 2. Adicione o seguinte conteúdo ao arquivo:

```env
# Chave da API do Google Gemini
GEMINI_API_KEY=sua_chave_api_aqui

# Configurações do Django
DEBUG=True
SECRET_KEY=django-insecure-v3m)v%l7gm$s43!+$h^in&(j%7rz*7-qhod^tagetu!j^=3@0k
```

### 3. Substitua `sua_chave_api_aqui` pela sua chave real da API do Gemini

### 4. Salve o arquivo

## 🚀 Como usar a API

### 1. Inicie o servidor:
```bash
python manage.py runserver
```

### 2. Teste os endpoints:

**Health Check:**
```
GET http://localhost:8000/api/gemini/health/
```

**Chat com Gemini:**
```
POST http://localhost:8000/api/gemini/chat/
Content-Type: application/json

{
    "message": "Sua mensagem aqui"
}
```

### 3. Execute o script de teste:
```bash
python test_api.py
```

## 📝 Exemplo de arquivo .env completo:
```env
GEMINI_API_KEY=AIzaSyC_exemplo_de_chave_api_aqui
DEBUG=True
SECRET_KEY=django-insecure-v3m)v%l7gm$s43!+$h^in&(j%7rz*7-qhod^tagetu!j^=3@0k
```
