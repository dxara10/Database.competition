import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Bloquear uma tabela para leitura
cursor.execute("LOCK TABLES tabela READ")

# Execute operações de leitura aqui

cursor.execute("UNLOCK TABLES")

conexao.close()
