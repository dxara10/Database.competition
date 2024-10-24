import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados",
    autocommit=False
)

cursor = conexao.cursor()

# Execute operações sem autocommit

conexao.commit()

conexao.close()
