#!/usr/bin/env python3
"""
Script para listar os modelos disponíveis na API do Gemini
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

def list_available_models():
    """Lista os modelos disponíveis"""
    print("🔍 Listando modelos disponíveis...")
    
    # Carregar variáveis de ambiente
    load_dotenv(Path('.') / '.env')
    
    # Obter chave
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ Chave da API não encontrada")
        return
    
    try:
        # Configurar Gemini
        genai.configure(api_key=api_key)
        print("✅ Gemini configurado com sucesso")
        
        # Listar modelos
        models = list(genai.list_models())
        print(f"\n📋 Modelos disponíveis ({len(models)} encontrados):")
        
        for model in models:
            print(f"  • {model.name}")
            print(f"    - Display name: {model.display_name}")
            print(f"    - Description: {model.description}")
            print(f"    - Generation methods: {model.supported_generation_methods}")
            print()
        
        # Verificar se gemini-pro está disponível
        gemini_pro_available = any('gemini-pro' in model.name for model in models)
        if gemini_pro_available:
            print("✅ Modelo gemini-pro está disponível!")
        else:
            print("❌ Modelo gemini-pro NÃO está disponível")
            print("\n💡 Modelos alternativos que você pode usar:")
            for model in models:
                if 'gemini' in model.name.lower():
                    print(f"  • {model.name}")
        
    except Exception as e:
        print(f"❌ Erro ao listar modelos: {e}")

if __name__ == "__main__":
    print("🚀 Listando Modelos Disponíveis na API do Gemini")
    print("=" * 60)
    
    list_available_models()
