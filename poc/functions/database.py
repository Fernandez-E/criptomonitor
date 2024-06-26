import sqlite3

# CRIA OU CONECTA A UM BANCO DE DADOS
def connect(databaseName):
    try:
        con = sqlite3.connect(f'{databaseName}.db')
        # Retorna a conexao com o banco para realização de querys
        return con
    except:
        return False

# REALIZA A CRIAÇÃO DA TABELA DA MOEDA, CASO AINDA NAO EXISTA
def create_table(databaseName: str, tableName: str):
    # databaseName deve ser apenas o nome do banco, sem a extensao ".db"
    try:
        con = connect(f'{databaseName}')
        cursor = con.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {tableName}(operation_type char, quantity double, BRLvalue double, coinPrice double, broker varchar(30), date varchar(10))')
        print('Tabela localizada com sucesso')
    except sqlite3.DatabaseError as e:
        print(f'A execucao retornou o seguinte erro: {e}')
    except:
        print('Falha na execucao')
    
def insert_buy_sell(databaseName: str, tableName: str, op_type: str, quantity: float, brlValue: float, broker: str, date: str):
    coin_price = round(brlValue / quantity, 2)
    try:
        con = connect(f'{databaseName}')
        cursor = con.cursor()
        cursor.execute(f'INSERT INTO {tableName}(operation_type, quantity, BRLvalue, coinPrice, broker, date) VALUES ("{op_type}", {quantity}, {brlValue}, {coin_price}, "{broker}", "{date}")')
        con.commit()
        print('Dados inseridos com sucesso')
    except sqlite3.DatabaseError as e:
        print(f'A execucao de insercao retornou o seguinte erro: {e}')
    except:
        print('Falha de conexao com o banco de dados. Operacao nao executada')
    
    
connect('cripto')
create_table('cripto', 'bitcoin')    
insert_buy_sell('cripto', 'bitcoin', 's', 0.00024, 68, 'Binance', '26/06/2024')