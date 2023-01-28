# Projeto final - banco de dados : Livraria online

## Cadastro e visualização de dados de livros

### Ferramentas necessárias

- Python
- Mysql
- VsCode
- git

### Instalação do projeto

1. Clone este repositório usando o comando **_git clone <https://github.com/JoaoManoelFontes/Project-Trabalho_db.git>_**

1. Abra a pasta no seu vscode e crie sua virtual env com o comando **_python -m venv venv_**

1. Entre na sua venv usando **_venv\Scripts\activate_**

1. Instale todas as bibliotecas necessárias de uma vez usando o comando **_pip install -r requirements.txt_**

1. Crie um arquivo com o nome **_.env_** e nele adicione as suas configurações do mysql

   - USER="SEU_USUÁRIO" (geralmente é host)
   - PASSWORD="SUA_SENHA" (a senha que você criou ao instalar o mysql)
   - HOST="SEU-HOST" (geralmente é localhost)

1. Execute o arquivo connect.py que está na pasta database para criar o banco de dados

1. Execute o arquivo create_book_table.py que está na pasta database para criar a table de livros

1. Por fim, inicie o server rodando o comando flask --app .\app\_\_init\_\_.py run
