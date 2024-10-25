--Primeiro Exercício
CREATE DATABASE professores;

-- criando tabela/entidade
CREATE TABLE alunos (
  matricula INTEGER PRIMARY KEY,
  nome_aluno TEXT NOT NULL,
  genero TEXT NOT NULL
);
-- injeção de dados-teste
INSERT INTO alunos VALUES (1, 'Luna', 'F');
INSERT INTO alunos VALUES (2, 'Davi', 'M');


-- consultando as injeções realizadas
SELECT * FROM alunos WHERE matricula=2