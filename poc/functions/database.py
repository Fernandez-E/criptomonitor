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
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {tableName}(quantity double, BRLvalue double, coinPrice double, broker varchar(30)), date varchar(10)')
        return True
    except:
        return False
    
    
def insert_data():
    pass