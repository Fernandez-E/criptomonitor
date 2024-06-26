import requests
import json
from time import sleep

# ENDPOINT DE TESTE DA API BINANCE
ping = 'https://api.binance.com/api/v3/ping' 

# TESTE DE CONEXAO COM A API
def connection_test():
    print("Testando conexao com a API Binance.")
    status = requests.get(ping)
    status = status.json()
    if status == {}:
        # TESTE POSITIVO 
        sleep(0.5)
        return 'Conexao realizada com sucesso.'
    else:
        # TESTE NEGATIVO
        sleep(0.5)
        return 'Falha de conexao com a Binance'

# REQUISICAO
    # Necessario saber os tickers disponiveis na api para passagem de parametro
    # Sempre em maiusculo
    # Três letras do nome da moeda + "USDT"
    # Bitcoin = "BTC" + "USDT" = 'BTCUSDT'
def get_coin_value(coin_ticker: str):
    endpoint = f'https://api.binance.com/api/v3/ticker/price?symbol={coin_ticker}'
    req = requests.get(endpoint)
    req = req.json()
    # Retorno em JSON 
    # req['symbol'] = nome da moeda
    # req['price']  = valor atual
    return req