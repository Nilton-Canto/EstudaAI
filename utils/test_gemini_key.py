#!/usr/bin/env python3
"""
Script para testar a chave da API do Gemini diretamente
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

def test_gemini_key():
    """Testa a chave da API do Gemini diretamente"""
    print("🔑 Testando chave da API do Gemini...")
    
    # Carregar variáveis de ambiente
    # Procura o .env na pasta config primeiro, depois na raiz
    env_paths = [
        Path('config') / '.env',
        Path('.') / '.env'
    ]
    
    env_loaded = False
    for env_path in env_paths:
        if env_path.exists():
            load_dotenv(env_path)
            print(f"📁 Arquivo .env carregado de: {env_path}")
            env_loaded = True
            break
    
    if not env_loaded:
        print("❌ Nenhum arquivo .env encontrado")
    
    # Obter chave
    api_key = os.getenv('GEMINI_API_KEY')
    print(f"📝 Chave carregada: {api_key[:20]}..." if api_key else "❌ Chave não encontrada")
    
    if not api_key:
        print("❌ Chave da API não encontrada no arquivo .env")
        return False
    
    try:
        # Configurar Gemini
        genai.configure(api_key=api_key)
        print("✅ Gemini configurado com sucesso")
        
        # Testar modelo
        model = genai.GenerativeModel('gemini-2.0-flash')
        print("✅ Modelo carregado com sucesso")
        
        # Testar geração
        response = model.generate_content("Olá! Teste simples.")
        print("✅ Geração de conteúdo funcionando!")
        print(f"📝 Resposta: {response.text[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar Gemini: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Teste da Chave da API do Gemini")
    print("=" * 50)
    
    success = test_gemini_key()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Chave da API funcionando perfeitamente!")
    else:
        print("❌ Problema com a chave da API")
        print("\n💡 Possíveis soluções:")
        print("1. Verifique se a chave está correta")
        print("2. Acesse: https://makersuite.google.com/app/apikey")
        print("3. Crie uma nova chave para o Gemini")
        print("4. Verifique se as APIs estão habilitadas")
