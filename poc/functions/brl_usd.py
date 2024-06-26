import requests
import json

# REQUISICAO
def brl_usd():
    req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    req = req.json()
    # Retorno em JSON 
    # req['USDBRL']['name'] = nome da conversao
    # req['USDBRL']['bid']  = cotação atualizada
    return req