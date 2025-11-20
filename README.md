Sistema de Gestão de Notas Escolar (Web)

Este é um sistema web completo para gestão escolar, desenvolvido em Python utilizando o microframework Flask e banco de dados PostgreSQL.

O sistema substitui a antiga interface de terminal por uma interface web amigável, permitindo o gerenciamento de usuários, disciplinas e notas com controle de acesso baseado em perfis.

🚀 Funcionalidades

Autenticação e Segurança: Login com criptografia de senhas (hash pbkdf2:sha256).

Controle de Acesso (Perfis):

ADMIN: Acesso total. Pode cadastrar novos usuários (Alunos/Professores) e criar disciplinas.

PROFESSOR: Pode lançar notas para os alunos nas disciplinas cadastradas.

ALUNO: Acesso de consulta ao seu próprio boletim de notas.

Interface Web: Dashboard responsivo com HTML5 e CSS3.

🛠️ Tecnologias Utilizadas

Backend: Python 3

Web Framework: Flask

Banco de Dados: PostgreSQL

Driver de Banco: Psycopg2

Segurança: Werkzeug Security

Frontend: Jinja2 Templates, HTML, CSS

⚙️ Guia de Instalação e Execução

1. Pré-requisitos

Certifique-se de ter o Python e o PostgreSQL instalados em sua máquina.

2. Configuração do Banco de Dados

Abra o pgAdmin ou seu cliente SQL preferido.

Crie um banco de dados chamado gestao_notas.

Abra a ferramenta de consulta (Query Tool) e execute o script contido no arquivo BANCO_DE_DADOS.sql (presente na raiz deste projeto) para criar as tabelas e relacionamentos.

3. Instalação das Dependências

Abra o terminal na pasta do projeto e execute:

pip install flask psycopg2-binary werkzeug


4. Configuração da Conexão Segura

Por segurança, as credenciais do banco de dados não são versionadas.
Você deve criar manualmente um arquivo chamado conexao.py dentro da pasta database/ com o seguinte conteúdo:

import psycopg2

# Substitua pelos seus dados locais
def conectar():
    try:
        return psycopg2.connect(
            database="gestao_notas",
            user="postgres",
            password="SUA_SENHA_AQUI",
            host="localhost",
            port="5432"
        )
    except Exception as e:
        print(f"Erro de conexão: {e}")
        return None


5. Executando o Sistema

Para iniciar o servidor web, execute o comando na raiz do projeto:

python app.py


O sistema estará acessível em seu navegador no endereço:
http://127.0.0.1:5000

👤 Primeiro Acesso (Admin)

Como o banco de dados inicia vazio, não haverá usuários para fazer login.
Para o primeiro acesso, você deve:

Rodar o script legado main.py (via terminal) para criar um usuário com perfil ADMIN.

Ou inserir manualmente um usuário na tabela usuario do banco de dados.

Após criar o primeiro Admin, os demais cadastros podem ser feitos diretamente pela interface web do sistema.
