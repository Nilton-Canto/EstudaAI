# API REST com Gemini - EstudaAI

## Configuração

### 1. Configurar a chave da API
Crie um arquivo `.env` na raiz do projeto com sua chave da API do Gemini:

```env
GEMINI_API_KEY=sua_chave_api_aqui
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Executar migrações
```bash
python manage.py migrate
```

### 4. Iniciar o servidor
```bash
python manage.py runserver
```

## Endpoints da API

### 1. Health Check
- **URL**: `GET /api/gemini/health/`
- **Descrição**: Verifica o status da API e se o Gemini está configurado
- **Resposta**:
```json
{
    "status": "healthy",
    "service": "EstudaAI Gemini API",
    "gemini_configured": true
}
```

### 2. Chat com Gemini
- **URL**: `POST /api/gemini/chat/`
- **Descrição**: Envia uma mensagem para o Gemini AI e recebe a resposta
- **Corpo da requisição**:
```json
{
    "message": "Sua mensagem aqui"
}
```
- **Resposta de sucesso**:
```json
{
    "message": "Sua mensagem aqui",
    "response": "Resposta do Gemini AI",
    "status": "success"
}
```

## Exemplo de uso com cURL

### Health Check
```bash
curl -X GET http://localhost:8000/api/gemini/health/
```

### Chat com Gemini
```bash
curl -X POST http://localhost:8000/api/gemini/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Explique o que é inteligência artificial"}'
```

## Exemplo de uso com JavaScript

```javascript
// Health Check
fetch('http://localhost:8000/api/gemini/health/')
  .then(response => response.json())
  .then(data => console.log(data));

// Chat com Gemini
fetch('http://localhost:8000/api/gemini/chat/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: 'Explique o que é inteligência artificial'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Estrutura do Projeto

```
config/
├── api_gemini/          # App da API do Gemini
│   ├── views.py         # Views da API
│   ├── urls.py          # URLs da API
│   └── admin.py         # Configuração do admin
├── config/
│   ├── settings.py      # Configurações do Django
│   └── urls.py          # URLs principais
└── .env                 # Variáveis de ambiente (criar manualmente)
```

## Notas Importantes

1. **Segurança**: Em produção, configure adequadamente as permissões CORS
2. **Rate Limiting**: Considere implementar rate limiting para evitar abuso da API
3. **Autenticação**: Para uso em produção, considere adicionar autenticação
4. **Logs**: Implemente logging adequado para monitorar o uso da API
