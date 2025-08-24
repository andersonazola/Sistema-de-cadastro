
![WhatsApp Image 2025-08-24 at 19 55 24](https://github.com/user-attachments/assets/9744fdd5-b10a-403d-ba29-b632cdd088b7)




## 📋 Cadastro de Clientes com Streamlit e SQLite

Este projeto é uma aplicação web simples e funcional para **cadastro de clientes**, desenvolvida com **Python**, utilizando o **Streamlit** para a interface e **SQLite** como banco de dados local. 

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



### ⚙️ Como executar o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/andersonazola/cadastro-clientes.git
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

### 📄 Licença

**Anderson Azola**  
Este projeto está licenciado sob a MIT License.

MIT License

Copyright (c) 2025 [Anderson Azola]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



