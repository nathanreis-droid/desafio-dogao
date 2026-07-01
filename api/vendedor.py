import requests
import json
import os
from api.token import token

def get_vendedor():
  
    try:
    # Faz a requisição para a API
        payload = {'filtro': "A3_COD ne '000001' "}
        headers = {'Authorization': 'Bearer ' + token()}
        campos_envio = { "campos": json.loads(os.getenv('SECRET_ARRAY_REPRESENT'))  }
        url = os.getenv('SECRET_URL')+"/api/v1/rest/representante"
        resposta = requests.get(url, params=payload,headers=headers,json=campos_envio)

    # Verifica se a requisição foi bem-sucedida (status 200)
        if resposta.status_code == 200 or resposta.status_code == 201:
            dados = resposta.json()  # Converte a resposta para um dicionário Python
            return  dados
        else:
            print(f"Erro na API. Código: {resposta.status_code}")
    except requests.exceptions.RequestException as erro:
        print(f"Erro de conexão: {erro}")