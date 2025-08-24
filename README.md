

## 📋 Cadastro de Clientes com Streamlit e SQLite

Este projeto é uma aplicação web simples e funcional para **cadastro de clientes**, desenvolvida com **Python**, utilizando o framework **Streamlit** para a interface e **SQLite** como banco de dados local. Ele é ideal para quem está começando com desenvolvimento de aplicações interativas e quer entender como integrar uma interface com persistência de dados.

---

### 🚀 Funcionalidades

- ✅ Adicionar novos clientes com nome, telefone e endereço
- 📄 Visualizar todos os clientes cadastrados em uma tabela
- 🔄 Atualizações futuras: edição e exclusão de registros

---

### 🛠 Tecnologias utilizadas

- **Python 3.10+**
- **Streamlit** – para criar a interface web
- **SQLite3** – banco de dados leve e local
- **Pandas** – para manipulação e exibição dos dados

---

### 📁 Estrutura do projeto

```
cadastro_clientes/
├── interface.py         # Interface principal com Streamlit
├── funcoes.py           # Funções para manipular o banco de dados
├── clientes.db          # Banco de dados SQLite (gerado automaticamente)
├── requirements.txt     # Lista de dependências
├── README.md            # Documentação do projeto
└── .gitignore           # Arquivos ignorados no Git
```

---

### ⚙️ Como executar o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/cadastro-clientes.git
cd cadastro-clientes
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Execute o aplicativo:**

```bash
streamlit run interface.py
```

---

### 🧠 Como funciona

- O usuário preenche os campos de nome, telefone e endereço.
- Ao clicar em "Cadastrar cliente", os dados são armazenados em um banco SQLite local.
- A tabela de clientes é atualizada automaticamente na interface.

---

### 📌 Observações

- O banco de dados `clientes.db` é criado automaticamente na primeira execução.
- O arquivo `.gitignore` impede que o banco seja versionado no GitHub, mantendo os dados locais protegidos.
- Este projeto pode ser facilmente expandido para incluir edição, exclusão e filtros de busca.

---

### 👤 Autor

**Anderson Azola**  


---

### 📷 Imagem de exemplo *(opcional)*


```

---


