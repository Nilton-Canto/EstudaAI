#!/bin/bash

# Script para rodar todas as verificações de CI localmente
# Execute: chmod +x run_ci_checks.sh && ./run_ci_checks.sh

set -e  # Para na primeira falha

echo "🚀 Iniciando verificações de CI/CD localmente..."
echo ""

# Cores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função para imprimir status
print_status() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✓ $2${NC}"
    else
        echo -e "${RED}✗ $2${NC}"
        exit 1
    fi
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_step() {
    echo -e "\n${YELLOW}▶ $1${NC}"
}

# 1. Verificar se estamos no diretório correto
print_step "Verificando diretório..."
if [ ! -f "requirements.txt" ]; then
    echo -e "${RED}Erro: Execute este script da raiz do projeto EstudaAI${NC}"
    exit 1
fi
print_status 0 "Diretório correto"

# 2. Verificar Python
print_step "Verificando Python 3.11..."
python3.11 --version > /dev/null 2>&1
print_status $? "Python 3.11 encontrado"

# 3. Criar .env se não existir
print_step "Verificando arquivo .env..."
if [ ! -f "config/.env" ]; then
    print_warning "Arquivo .env não encontrado. Criando..."
    cat > config/.env << EOF
GEMINI_API_KEY=test_key_for_local_ci
DEBUG=True
SECRET_KEY=local-test-secret-key-$(openssl rand -hex 32)
EOF
    print_status 0 "Arquivo .env criado"
else
    print_status 0 "Arquivo .env existe"
fi

# 4. Instalar dependências
print_step "Instalando dependências..."
pip install -q -r requirements.txt
print_status $? "Dependências instaladas"

# 5. Rodar migrações
print_step "Rodando migrações..."
cd config
python manage.py migrate --noinput > /dev/null 2>&1
print_status $? "Migrações executadas"

# 6. Formatação com Black
print_step "Verificando formatação com Black..."
black --check --diff . > /dev/null 2>&1
if [ $? -ne 0 ]; then
    print_warning "Black encontrou problemas de formatação"
    echo "Execute: black config/"
    black --check --diff .
    exit 1
fi
print_status 0 "Formatação OK"

# 7. Ordenação de imports com isort
print_step "Verificando ordenação de imports com isort..."
isort --check-only --diff . > /dev/null 2>&1
if [ $? -ne 0 ]; then
    print_warning "isort encontrou problemas"
    echo "Execute: isort config/"
    isort --check-only --diff .
    exit 1
fi
print_status 0 "Imports OK"

# 8. Linting com Flake8
print_step "Verificando código com Flake8..."
cd ..
flake8 config/usuarios config/api_gemini config/config --config=setup.cfg
print_status $? "Linting OK"

# 9. Segurança com Bandit
print_step "Verificando segurança com Bandit..."
bandit -r config/usuarios config/api_gemini config/config --configfile .bandit --severity-level medium
print_status $? "Segurança OK"

# 10. Testes com cobertura
print_step "Rodando testes com cobertura..."
cd config
pytest --cov=. --cov-report=term-missing --cov-fail-under=70 -v
print_status $? "Testes OK"

# 11. Verificar vulnerabilidades em dependências
print_step "Verificando vulnerabilidades em dependências..."
cd ..
safety check || print_warning "Safety encontrou algumas vulnerabilidades (não crítico)"

echo ""
echo -e "${GREEN}════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ Todas as verificações passaram!${NC}"
echo -e "${GREEN}  Seu código está pronto para commit.${NC}"
echo -e "${GREEN}════════════════════════════════════════${NC}"
echo ""
