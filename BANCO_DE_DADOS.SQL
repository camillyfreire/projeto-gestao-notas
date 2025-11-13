CREATE TYPE perfil_usuario AS ENUM ('ALUNO', 'PROFESSOR', 'ADMIN');

-- Tabela de Usuários (unificada)
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    perfil perfil_usuario NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Disciplinas
CREATE TABLE disciplina (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    -- Usuário cadastrado prof
    professor_id INT,
    FOREIGN KEY (professor_id) REFERENCES usuario(id)
);

-- Tabela de Notas
CREATE TABLE nota (
    id SERIAL PRIMARY KEY,
    -- Chave estrangeira (FK) para o aluno
    aluno_id INT NOT NULL,
    -- Chave estrangeira (FK) para a disciplina
    disciplina_id INT NOT NULL,
    -- Descrição (ex: "Prova 1", "Trabalho Final")
    descricao VARCHAR(100) NOT NULL,
    valor DECIMAL(4, 2) NOT NULL, 
    data_lancamento DATE DEFAULT CURRENT_DATE,
    
    FOREIGN KEY (aluno_id) REFERENCES usuario(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplina(id),
    UNIQUE(aluno_id, disciplina_id, descricao)
);