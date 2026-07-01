import requests
import os

    
def token():

    url = os.getenv('SECRET_URL')+ '/api/oauth2/v1/token'
    payload = {'grant_type': 'password'}
    headers = {'username': os.getenv('SECRET_USER'),'password': os.getenv('SECRET_PASS')}
    
    try:
    # Faz a requisição para a API
        resposta = requests.post(url, params=payload,headers=headers)

    # Verifica se a requisição foi bem-sucedida (status 200)
        if  resposta.status_code == 201:
            dados = resposta.json()  # Converte a resposta para um dicionário Python
            return  dados['access_token']
        
    except requests.exceptions.RequestException as erro:
        print(f"Erro de conexão: {erro}")
    