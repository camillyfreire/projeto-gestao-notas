Projeto de Gestão de Notas

Este projeto é um Sistema de Gestão de Notas em Python, desenvolvido para a disciplina de LP3, utilizando PostgreSQL como banco de dados.

1. Configuração do Banco de Dados

Crie um novo banco de dados no PostgreSQL (ex: gestao_notas).

Abra a "Query Tool" para este banco e execute o script contido no arquivo BANCO_DE_DADOS.sql para criar todas as tabelas e tipos necessários.

2. Configuração do Projeto

Para rodar o projeto, é necessário configurar a conexão com o banco e instalar as dependências.

Dependências

O projeto utiliza as bibliotecas psycopg2-binary (para a conexão) e werkzeug (para a segurança das senhas).

pip install psycopg2-binary werkzeug


Arquivo de Conexão

Por razões de segurança, o arquivo database/conexao.py não está no repositório. Crie este arquivo manualmente com a seguinte estrutura, substituindo pelas suas credenciais locais:

import psycopg2

# ATUALIZE COM OS DADOS DO SEU BANCO
DB_NAME = "gestao_notas"
DB_USER = "postgres"
DB_PASS = "sua_senha_aqui" # <-- MUDE AQUI
DB_HOST = "localhost"
DB_PORT = "5432"

def conectar():
    try:
        return psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


3. Execução

Após configurar o banco e o arquivo conexao.py, execute o programa principal:

python main.py
