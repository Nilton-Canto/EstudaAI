# 📊 Diagramas UML - EstudaAI

Esta pasta contém os diagramas conceituais e de modelagem do sistema EstudaAI.

## 📁 Arquivos Disponíveis

### 1. `diagrama-conceitual.puml`
**Diagrama de Classes Conceitual**
- Mostra a estrutura técnica das classes do sistema
- Inclui atributos, métodos e relacionamentos
- Organizado por domínios (Usuário, Conhecimento, Aprendizagem, IA)

### 2. `modelo-dominio.puml`
**Modelo de Domínio Conceitual**
- Foca nos conceitos de negócio
- Representa entidades do mundo real
- Mostra relacionamentos conceituais entre entidades

### 3. `casos-uso.puml`
**Diagrama de Casos de Uso**
- Funcionalidades do sistema
- Atores e suas interações
- Relacionamentos entre casos de uso

## 🛠️ Como Visualizar os Diagramas

### Opção 1: PlantUML Online
1. Acesse: https://www.plantuml.com/plantuml/uml/
2. Copie o conteúdo do arquivo `.puml`
3. Cole no editor online
4. Visualize o diagrama gerado

### Opção 2: VS Code + Extensão
1. Instale a extensão "PlantUML" no VS Code
2. Abra o arquivo `.puml`
3. Use `Ctrl+Shift+P` → "PlantUML: Preview Current Diagram"

### Opção 3: Linha de Comando (se tiver PlantUML instalado)
```bash
# Gerar PNG
plantuml diagrama-conceitual.puml

# Gerar SVG
plantuml -tsvg diagrama-conceitual.puml
```

## 📋 Descrição dos Diagramas

### Diagrama Conceitual
- **Domínio do Usuário**: Entidades relacionadas aos estudantes
- **Domínio do Conhecimento**: Áreas de estudo e categorização
- **Domínio da Aprendizagem**: Trilhas, progressos e acompanhamento
- **Domínio da IA**: Serviços de geração automática de conteúdo

### Modelo de Domínio
- **Estudante**: Usuário principal do sistema
- **TrilhaAprendizagem**: Conceito central de sequência de estudos
- **AgenteIA**: Responsável pela geração inteligente de trilhas
- **ProgressoEstudo**: Acompanhamento da evolução do estudante

### Casos de Uso
- **UC01-UC02**: Autenticação e cadastro
- **UC03-UC04**: Criação de trilhas (pré-definidas e personalizadas)
- **UC05-UC06**: Acompanhamento de progresso
- **UC07-UC08**: Funcionalidades administrativas
- **UC09-UC10**: Integração com IA

## 🔄 Atualizações

Para manter os diagramas atualizados:

1. **Após mudanças no modelo de dados**: Atualize `diagrama-conceitual.puml`
2. **Após mudanças nos requisitos**: Atualize `modelo-dominio.puml`
3. **Após novas funcionalidades**: Atualize `casos-uso.puml`

## 📚 Referências

- [PlantUML Documentation](https://plantuml.com/)
- [UML Class Diagrams](https://www.uml-diagrams.org/class-diagrams-overview.html)
- [Domain Modeling](https://martinfowler.com/bliki/DomainModel.html)