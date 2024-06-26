import functions.database as database
import functions.binance_api as binance
import functions.brl_usd as brl

from time import sleep
import os

while True:
    os.system('cls')
    print('#'*50)
    print(f'{"Acompanhamento de criptomoedas":^50}')
    print('#'*50)

    print('1: Acompanhar cotacao atual')
    print('2: Acompanhamento continuo')
    print('3: Testar conexoes externas')
    print('4: Inserir compra')
    print('4: Inserir venda')

    option = int(input('>>> '))
    
    if option == 1:
        os.system('cls')
        btc = binance.get_coin_value('BTCUSDT')['price']
        brl_price = brl.brl_usd()['USDBRL']['bid']
        btc = float(btc) * float(brl_price)
        print(f'A cotacao atual para o BitCoin e de ${btc:.2f}')
        input('>>> Pressione ENTER para continuar <<<')

    elif option == 3:
        os.system('cls')
        print(binance.connection_test())
        input('>>> Pressione ENTER para continuar <<<')
