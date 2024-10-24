import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Começar uma transação
cursor.execute("START TRANSACTION")

# Execute operações dentro da transação aqui

conexao.commit()

conexao.close()
