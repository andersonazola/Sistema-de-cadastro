import streamlit as st 
import pandas as pd
import funcoes

st.title("Cadastro de clientes")
nome = st.text_input('Insira seu nome: ')
telefone = st.text_input('Insira seu telefone: ')
endereco = st.text_input('Insira seu endereço: ')

if st.button("Adicionar clientes"):
    funcoes.insere_Dados(nome, telefone, endereco)
    st.success("Cliente adicionado")
    

if st.button("Listar clientes"):
    dados = funcoes.listar_Dados()
    tb = pd.DataFrame(dados, columns=["ID", "Nome", "Telefone", "Endereço"])
    st.header("Lista de clientes")
    st.table(tb)
    
