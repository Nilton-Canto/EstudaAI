# 🛠️ Utilitários do EstudaAI

Esta pasta contém scripts utilitários para desenvolvimento e manutenção do projeto.

## 📁 Arquivos Disponíveis

### 🔑 `test_gemini_key.py`
**Propósito**: Testa se a chave da API do Gemini está funcionando corretamente.

**Como usar**:
```bash
cd utils
python test_gemini_key.py
```

**Quando usar**:
- Após configurar uma nova chave da API
- Para debugar problemas de autenticação
- Para verificar se a API está respondendo

---

### 📋 `list_models.py`
**Propósito**: Lista todos os modelos disponíveis na API do Gemini.

**Como usar**:
```bash
cd utils
python list_models.py
```

**Quando usar**:
- Para descobrir novos modelos disponíveis
- Para verificar se um modelo específico está acessível
- Para documentar capacidades da API

---

### 🧪 `test_api_complete.py`
**Propósito**: Executa testes completos de integração da API (conectividade, performance, CORS).

**Como usar**:
```bash
# Certifique-se que o servidor Django está rodando
cd config
python manage.py runserver

# Em outro terminal
cd utils
python test_api_complete.py
```

**Quando usar**:
- Para testes de integração antes de deploy
- Para verificar performance da API
- Para debugar problemas de conectividade
- Para validar configurações de CORS

---

## 📝 Notas de Desenvolvimento

### Pré-requisitos
- Ambiente virtual ativado
- Arquivo `.env` configurado com `GEMINI_API_KEY`
- Django instalado e configurado

### Variáveis de Ambiente Necessárias
```env
GEMINI_API_KEY=sua_chave_aqui
```

### Dependências
Estes scripts usam:
- `requests` (para testes HTTP)
- `google-generativeai` (para API do Gemini)
- `python-dotenv` (para variáveis de ambiente)

---

## 🎯 Diferença dos Testes Unitários

**Testes Unitários** (`config/api_gemini/tests.py`):
- Executados via VS Code Testing
- Usam mocks para isolamento
- Focam em lógica individual
- Executados automaticamente

**Utilitários desta pasta**:
- Testam integração real com APIs externas
- Usam conexões HTTP reais
- Verificam configuração do ambiente
- Executados manualmente quando necessário

---

## 📞 Suporte

Se encontrar problemas com estes utilitários:

1. **Verifique o ambiente virtual**: `.venv\Scripts\activate`
2. **Confirme as variáveis de ambiente**: arquivo `.env` configurado
3. **Verifique as dependências**: `pip install -r ../requirements.txt`
4. **Para o script da API completa**: servidor Django deve estar rodando
