#!/usr/bin/env python3
"""
Script de teste simples para a API do Gemini
Execute este script após iniciar o servidor Django
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_health_check():
    """Testa o endpoint de health check"""
    print("🔍 Testando Health Check...")
    try:
        response = requests.get(f"{BASE_URL}/api/gemini/health/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health Check OK: {data}")
        else:
            print(f"❌ Health Check falhou: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro no Health Check: {e}")

def test_chat_endpoint():
    """Testa o endpoint de chat"""
    print("\n💬 Testando Chat Endpoint...")
    try:
        payload = {
            "message": "Olá! Como você pode me ajudar com estudos?"
        }
        
        response = requests.post(
            f"{BASE_URL}/api/gemini/chat/",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Chat OK:")
            print(f"   Mensagem: {data['message']}")
            print(f"   Resposta: {data['response'][:100]}...")
        else:
            print(f"❌ Chat falhou: {response.status_code}")
            print(f"   Resposta: {response.text}")
    except Exception as e:
        print(f"❌ Erro no Chat: {e}")

def main():
    """Função principal"""
    print("🚀 Iniciando testes da API do Gemini...")
    print(f"📡 URL base: {BASE_URL}")
    print("=" * 50)
    
    test_health_check()
    test_chat_endpoint()
    
    print("\n" + "=" * 50)
    print("✨ Testes concluídos!")

if __name__ == "__main__":
    main()
