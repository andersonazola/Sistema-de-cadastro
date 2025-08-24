import sqlite3

# Fazer a conexão com o banco de dados
conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criar tabela com segurança
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cliente(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Telefone TEXT NOT NULL,
        Endereco TEXT NOT NULL
    )
""")

# Fechar cursor e conexão
cursor.close()
conexao.close()

print("Tabela criada com sucesso!")