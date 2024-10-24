import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

try:
    # Começar uma transação
    cursor.execute("START TRANSACTION")

    # Execute operações dentro da transação aqui

    # Se algo der errado, faça rollback da transação
    conexao.rollback()

except Exception as e:
    print("Erro:", e)
    conexao.rollback()

finally:
    conexao.close()
