import requests
import json
import os
from api.token import token
    
def get_cliente():
  
    try:
    # Faz a requisição para a API
        payload = {'filtro': "A1_COD ne '00' "}
        headers = {'Authorization': 'Bearer ' + token()}
        campos_envio = { "campos": json.loads(os.getenv('SECRET_ARRAY'))  }
        url = os.getenv('SECRET_URL')+"/api/v1/rest/client"
        resposta = requests.get(url, params=payload,headers=headers,json=campos_envio)

    # Verifica se a requisição foi bem-sucedida (status 200)
        if resposta.status_code == 200 or resposta.status_code == 201:
            dados = resposta.json()  # Converte a resposta para um dicionário Python
            return  dados
        else:
            print(f"Erro na API. Código: {resposta.status_code}")
    except requests.exceptions.RequestException as erro:
        print(f"Erro de conexão: {erro}")