# API de Geração de Trilhas de Curso - EstudaAI

## Visão Geral

A API de Geração de Trilhas de Curso permite que alunos solicitem trilhas de aprendizado personalizadas baseadas em suas necessidades específicas. A API utiliza o LLM Gemini para gerar conteúdo estruturado e retorna respostas em formato JSON.

## Endpoints Disponíveis

### 1. Gerar Trilha de Curso
**POST** `/api/gemini/trilha/`

Gera uma trilha de curso personalizada baseada na solicitação do usuário.

#### Parâmetros de Entrada:
```json
{
    "solicitacao": "string (obrigatório) - Descrição do que o usuário quer aprender",
    "user_id": "integer (opcional) - ID do usuário para personalização"
}
```

#### Exemplo de Requisição:
```json
{
    "solicitacao": "Quero aprender Python para análise de dados",
    "user_id": 1
}
```

#### Exemplo de Resposta:
```json
{
    "solicitacao": "Quero aprender Python para análise de dados",
    "trilha": {
        "titulo": "Python para Análise de Dados",
        "descricao": "Trilha completa para aprender Python focado em análise de dados",
        "nivel": "Iniciante",
        "duracao_total": "12 semanas",
        "modulos": [
            {
                "numero": 1,
                "titulo": "Fundamentos do Python",
                "descricao": "Conceitos básicos da linguagem Python",
                "duracao": "3 semanas",
                "topicos": [
                    "Sintaxe básica",
                    "Variáveis e tipos de dados",
                    "Estruturas de controle"
                ],
                "recursos": [
                    {
                        "tipo": "video",
                        "titulo": "Python Basics",
                        "descricao": "Curso introdutório de Python"
                    }
                ],
                "atividades_praticas": [
                    "Exercícios de programação básica",
                    "Projeto: Calculadora simples"
                ]
            }
        ],
        "projeto_final": "Análise completa de um dataset real",
        "recursos_complementares": [
            "Documentação oficial do Python",
            "Comunidade Python Brasil"
        ]
    },
    "status": "success",
    "model_used": "gemini-2.0-flash",
    "personalizada": true,
    "trilha_id": 123,
    "data_criacao": "2025-09-22T10:30:00Z"
}
```

#### Códigos de Status:
- `200`: Trilha gerada com sucesso
- `400`: Dados de entrada inválidos
- `500`: Erro interno do servidor

### 2. Listar Trilhas do Usuário
**GET** `/api/gemini/trilhas/{user_id}/`

Lista todas as trilhas ativas de um usuário específico.

#### Parâmetros:
- `user_id`: ID do usuário (na URL)

#### Exemplo de Resposta:
```json
{
    "usuario": "joao_silva",
    "total_trilhas": 2,
    "trilhas": [
        {
            "id": 123,
            "titulo": "Python para Análise de Dados",
            "descricao": "Trilha completa para aprender Python focado em análise de dados",
            "data_criacao": "2025-09-22T10:30:00Z",
            "conteudo": {
                "titulo": "Python para Análise de Dados",
                "nivel": "Iniciante",
                "modulos": [...]
            }
        }
    ]
}
```

#### Códigos de Status:
- `200`: Lista retornada com sucesso
- `404`: Usuário não encontrado
- `500`: Erro interno do servidor

### 3. Chat com Gemini (Existente)
**POST** `/api/gemini/chat/`

Endpoint para chat direto com o LLM Gemini.

#### Parâmetros de Entrada:
```json
{
    "message": "string (obrigatório) - Mensagem para o LLM"
}
```

### 4. Health Check (Existente)
**GET** `/api/gemini/health/`

Verifica o status da API e configurações.

## Personalização

Quando um `user_id` é fornecido, a API personaliza a trilha baseada nos dados do usuário:
- Curso atual
- Universidade
- Ano de formatura
- Idade

Isso permite que o LLM crie trilhas mais adequadas ao perfil e contexto do estudante.

## Estrutura da Trilha

Cada trilha gerada segue uma estrutura padronizada:

- **titulo**: Nome da trilha
- **descricao**: Descrição geral e objetivos
- **nivel**: Iniciante/Intermediário/Avançado
- **duracao_total**: Tempo estimado total
- **modulos**: Lista de módulos sequenciais
  - **numero**: Ordem do módulo
  - **titulo**: Nome do módulo
  - **descricao**: O que será aprendido
  - **duracao**: Tempo estimado do módulo
  - **topicos**: Lista de tópicos abordados
  - **recursos**: Materiais recomendados
  - **atividades_praticas**: Exercícios e projetos
- **projeto_final**: Projeto integrador
- **recursos_complementares**: Materiais adicionais

## Tratamento de Erros

A API possui tratamento robusto de erros e retorna mensagens descritivas:

### Erros Comuns:
- **Chave API não configurada**: Configuração necessária no servidor
- **Solicitação vazia**: Campo `solicitacao` é obrigatório
- **Usuário não encontrado**: `user_id` inválido
- **JSON inválido**: Resposta do LLM não pôde ser parseada
- **Prompt bloqueado**: Conteúdo violou políticas de segurança
- **Limite de API**: Cota do Gemini excedida

## Configuração

### Variáveis de Ambiente Necessárias:
- `GEMINI_API_KEY`: Chave da API do Google Gemini
- `GEMINI_MODEL`: Modelo a ser usado (padrão: gemini-2.0-flash)

### Dependências:
- Django REST Framework
- google-generativeai
- Modelo de usuário customizado

## Logs

A API registra logs detalhados para monitoramento:
- Requisições recebidas
- Erros de processamento
- Tempo de resposta
- Uso da API do Gemini

## Limitações

- Dependente da disponibilidade da API do Gemini
- Sujeito aos limites de rate limiting do Gemini
- Qualidade da trilha depende da clareza da solicitação
- Requer internet para funcionar

## Exemplos de Uso

### Frontend JavaScript:
```javascript
// Gerar trilha
const response = await fetch('/api/gemini/trilha/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify({
        solicitacao: 'Quero aprender desenvolvimento web com React',
        user_id: 1
    })
});

const trilha = await response.json();
console.log(trilha);

// Listar trilhas do usuário
const trilhas = await fetch('/api/gemini/trilhas/1/');
const userTrilhas = await trilhas.json();
```

### Python/Django:
```python
import requests

# Gerar trilha
data = {
    'solicitacao': 'Quero aprender machine learning',
    'user_id': 1
}

response = requests.post('http://localhost:8000/api/gemini/trilha/', json=data)
trilha = response.json()
```

## Versionamento

Versão atual: 1.0.0

Mantemos compatibilidade com versões anteriores e documentamos mudanças no formato de resposta.