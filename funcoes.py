import sqlite3

#criar funções para usar no codigo principal

#funcao para conectar as funcoes ao banco de dados
def conectaDB():
    conexao = sqlite3.connect("Clientes.db")
    return conexao

#funcao para receber os dados e inserir na tabela clientes
#O ? funciona como um placeholder: ele será substituído pelos valores passados na tupla (nome, telefone, endereco).
def insere_Dados(nome, telefone, endereco):
        conexao = conectaDB()
        try:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Cliente(nome, telefone, endereco) VALUES (?, ?, ?)", (nome, telefone, endereco))
            conexao.commit() #salva a alteração no banco de dados.
        finally:
            conexao.close() #fecha a conexão mesmo se ocorrer erros, liberando os recursos.
  
  
 # obs: Os '?' são placeholders, que são substituídos pelos valores (nome, telefone, endereco) 
        
        
#funcao para listar os dados

def listar_Dados():
    conexao = conectaDB()
    
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Cliente")
        dados = cursor.fetchall() # pega todos os resultados retornados pela consulta e os coloca em uma lista de tuplas.
        cursor.close()
        return dados
    finally:
        conexao.close() 
        
