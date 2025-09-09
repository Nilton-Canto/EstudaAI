# Configuração do Ambiente

## Configuração da API Key

Para usar este projeto, você precisa configurar sua própria chave da API do Google Gemini.

### Passos para configuração:

1. **Copie o arquivo de exemplo:**
   ```bash
   cp .env.example .env
   ```

2. **Configure sua chave da API:**
   - Abra o arquivo `.env` 
   - Substitua `sua_chave_aqui` pela sua chave real da API do Google Gemini
   - Substitua `sua_secret_key_aqui` por uma SECRET_KEY do Django segura

3. **Obtenha sua chave da API do Google Gemini:**
   - Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Faça login com sua conta Google
   - Crie uma nova chave de API
   - Copie a chave gerada

### Exemplo de arquivo .env:
```
# Chave da API do Google Gemini
GEMINI_API_KEY=AIzaSyC...sua_chave_real_aqui

# Configurações do Django
DEBUG=True
SECRET_KEY=sua_secret_key_django_aqui
```

### ⚠️ Importante:
- **NUNCA** commite o arquivo `.env` com suas chaves reais
- O arquivo `.env` está no `.gitignore` para proteção
- Use sempre o arquivo `.env.example` como referência
