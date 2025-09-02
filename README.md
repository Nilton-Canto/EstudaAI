# 📚 EstudaAI

O **EstudaAI** é uma aplicação web desenvolvida para ajudar estudantes no **planejamento de estudos**, através da **recomendação de trilhas de aprendizagem**. O sistema permite ao aluno escolher entre **trilhas pré-definidas** ou criar **trilhas personalizadas com o apoio de um agente LLM (IA)**.

---

## 🚀 Projeto GitHub – Fluxo de Branches

👉 **Cada aluno deve criar uma branch própria para cada nova funcionalidade (feature branch).**

### Exemplo de criação de branch:
```bash
git checkout -b feature/criacao-de-trilhas
```

---

## 🔄 Fluxo de Trabalho (Pull Request Workflow)

1. ✅ **Criar a branch de feature** (exemplo: `feature/nome-da-feature`)
2. ✅ **Realizar commits frequentes e com mensagens claras**
3. ✅ **Enviar (push) sua branch para o GitHub**
4. ✅ **Abrir um Pull Request (PR)**
5. ✅ **Designar pelo menos 1 colega como revisor**

### 🎯 O que o revisor deve fazer:
- 👀 **Ler o código no GitHub**
- 💬 **Fazer comentários linha a linha (inline comments)**
- 🛠️ **Sugerir melhorias, correções ou ajustes**
- ✅ **Aprovar o PR após validação**

Após a aprovação ✅, o autor do PR realiza o **merge** para a branch principal (`main`).

---
## 🔄  Regras:

- ✅ Ninguém faz merge direto na main.
- ✅ Pull Requests para a main só podem vir da develop.
- ✅ Pull Requests para a develop só podem vir de feature branches (ex: feature/*).
- ✅ Proibido fazer PR de main → develop.
- ✅ Proibido fazer PR de develop → feature.

---

## 📝 Boas Práticas de Commit

- 🔁 **Commits pequenos e frequentes**
- ✏️ **Mensagens de commit claras e objetivas**
- ⚠️ **Antes de abrir o PR, sempre execute:**
```bash
git pull origin main
```
👉 Para garantir que sua branch está atualizada e evitar conflitos.

---

## 👀 Checklist para Revisores (Code Review)

Antes de aprovar um PR, verifique:

1. ✅ **Nome de variáveis** é adequado e expressivo.
2. ✅ **Clareza e legibilidade** do código.
3. ✅ **Divisão de responsabilidades** bem definida (nenhuma função fazendo "tudo").
4. ✅ **Cumprimento dos requisitos da issue relacionada**.
5. ✅ **Presença de testes**, se aplicável.
6. ✅ Só aprova PR se "base branch" correta (ex: feature/ para develop ou develop para main)
