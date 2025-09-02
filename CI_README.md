# 🚀 CI/CD - EstudaAI

## 📋 O que é o CI?

**CI (Continuous Integration)** é um processo automatizado que executa sempre que código é enviado para o repositório, garantindo qualidade e consistência.

## 🔄 Como funciona?

### **Triggers (Gatilhos):**
- ✅ Push para `main` ou `develop`
- ✅ Pull Request para `main` ou `develop`

### **Passos executados:**
1. **Setup do ambiente** - Python 3.11 + dependências
2. **Cache inteligente** - Acelera builds futuros
3. **Testes Django** - `python manage.py test`
4. **Verificação de código** - Flake8 + Black
5. **Análise de segurança** - Bandit

## 📁 Arquivos criados:

### **`.github/workflows/ci.yml`**
- Workflow principal do GitHub Actions
- Executa em Ubuntu Linux
- Cache otimizado para dependências

### **`setup.cfg`**
- Configuração do Flake8 (linter)
- Regras personalizadas para Django
- Exclusões para migrations e venv

### **`.bandit`**
- Configuração do Bandit (segurança)
- Análise de vulnerabilidades Python
- Foco nos diretórios principais

### **`.gitignore`**
- Atualizado com entradas para CI/CD
- Exclusão de relatórios de segurança
- Proteção de arquivos sensíveis

## 🚨 O que acontece se falhar?

- ❌ **Testes falharam** → Merge bloqueado
- ❌ **Formatação incorreta** → Merge bloqueado
- ❌ **Problemas de segurança** → Merge bloqueado
- ✅ **Tudo OK** → Merge permitido

## 🛠️ Como usar localmente?

### **Instalar ferramentas:**
```bash
pip install flake8 black bandit
```

### **Verificar formatação:**
```bash
black --check .
flake8 .
```

### **Verificar segurança:**
```bash
bandit -r .
```

### **Executar testes:**
```bash
python manage.py test
```

## 📊 Monitoramento:

- **GitHub Actions** → Aba "Actions" no repositório
- **Histórico completo** → Todas as execuções
- **Logs detalhados** → Para debug de problemas

## 🔮 Próximos passos (CD):

- **Deploy automático** para ambientes de teste
- **Rollback automático** em caso de falha
- **Notificações** de deploy
- **Ambiente de produção** automatizado

---

**Status:** ✅ CI implementado na Sprint 1  
**Próximo:** 🚀 CD na Sprint 2
