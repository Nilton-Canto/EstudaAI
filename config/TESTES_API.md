# 🧪 Testes da API do Gemini

Este documento explica como executar e entender os testes da API do Gemini.

## 📋 Tipos de Testes

### 1. Testes Unitários (`api_gemini/tests.py`)
Testes automatizados que verificam funcionalidades específicas da API:

- **Health Check**: Verifica se o endpoint de status funciona
- **Validação de Entrada**: Testa mensagens vazias e dados inválidos
- **Configuração da API**: Verifica se a chave do Gemini está configurada
- **Resposta do Chat**: Testa integração com o Gemini (com mock)
- **Tratamento de Erros**: Verifica se erros são tratados corretamente

### 2. Testes de Integração (`test_api_complete.py`)
Testes que verificam o funcionamento completo da API:

- **Conectividade**: Verifica se o servidor está rodando
- **Performance**: Mede tempo de resposta
- **CORS**: Verifica headers de CORS
- **Chat Real**: Testa com chave real do Gemini

### 3. Teste de Chave (`test_gemini_key.py`)
Testa se a chave da API do Gemini está funcionando.

## 🚀 Como Executar os Testes

### Pré-requisitos
```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar chave da API (opcional para testes completos)
# Criar arquivo .env com:
# GEMINI_API_KEY=sua_chave_aqui
```

### 1. Testes Unitários
```bash
# Executar todos os testes unitários
python run_tests.py

# Executar teste específico
python run_tests.py GeminiAPITestCase.test_health_check_success
```

### 2. Testes de Integração
```bash
# Iniciar servidor Django
python manage.py runserver

# Em outro terminal, executar testes de integração
python test_api_complete.py
```

### 3. Teste de Chave do Gemini
```bash
python test_gemini_key.py
```

### 4. Teste Simples da API
```bash
# Com servidor rodando
python test_api.py
```

## 📊 Interpretando os Resultados

### ✅ Sucesso
- **Testes Unitários**: Todos os testes passam
- **Testes de Integração**: API responde corretamente
- **Teste de Chave**: Gemini responde às requisições

### ❌ Problemas Comuns

#### 1. Servidor não está rodando
```
❌ Conexão com servidor: Servidor não está rodando
```
**Solução**: Execute `python manage.py runserver`

#### 2. Chave da API não configurada
```
❌ Chat Test 1: Status: 500 - Chave da API do Gemini não configurada
```
**Solução**: Configure `GEMINI_API_KEY` no arquivo `.env`

#### 3. Timeout do Gemini
```
❌ Chat Test 1: Timeout - Gemini demorou muito para responder
```
**Solução**: Verifique sua conexão com a internet e a chave da API

#### 4. Erro de CORS
```
❌ CORS Headers: Poucos headers CORS
```
**Solução**: Verifique se `corsheaders` está instalado e configurado

## 🔧 Configuração de Logs

Os logs são salvos em `logs/django.log` e incluem:
- Requisições recebidas
- Erros da API
- Tempo de resposta
- Configuração do Gemini

## 📈 Métricas de Performance

### Tempos Esperados
- **Health Check**: < 1 segundo
- **Chat com Gemini**: 2-10 segundos
- **Validação**: < 0.5 segundos

### Taxa de Sucesso
- **Testes Unitários**: 100%
- **Testes de Integração**: > 90% (depende da chave da API)

## 🐛 Debugging

### 1. Verificar Logs
```bash
tail -f logs/django.log
```

### 2. Testar Endpoints Manualmente
```bash
# Health check
curl http://localhost:8000/api/gemini/health/

# Chat (com chave configurada)
curl -X POST http://localhost:8000/api/gemini/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Olá!"}'
```

### 3. Verificar Configuração
```python
python manage.py shell
>>> from django.conf import settings
>>> print(settings.GEMINI_API_KEY)
>>> print(settings.GEMINI_MODEL)
```

## 📝 Adicionando Novos Testes

### Teste Unitário
```python
def test_novo_caso(self):
    """Descrição do teste"""
    response = self.client.post(self.chat_url, data={'message': 'teste'})
    self.assertEqual(response.status_code, 200)
```

### Teste de Integração
```python
def test_nova_funcionalidade(self):
    """Testa nova funcionalidade"""
    # Implementar teste
    pass
```

## 🎯 Objetivos dos Testes

1. **Confiabilidade**: Garantir que a API funciona consistentemente
2. **Segurança**: Verificar validação de entrada e tratamento de erros
3. **Performance**: Monitorar tempos de resposta
4. **Integração**: Confirmar funcionamento com o Gemini
5. **Manutenibilidade**: Facilitar identificação de problemas

## 📞 Suporte

Se encontrar problemas:
1. Verifique os logs em `logs/django.log`
2. Execute `python test_gemini_key.py` para testar a chave
3. Verifique se todas as dependências estão instaladas
4. Confirme se o servidor Django está rodando
