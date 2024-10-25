-- Criando meu primeiro banco de dados
CREATE DATABASE senac_copacabana;
 

-- criando minha primeira tabela/entidade
CREATE TABLE alunos (
  matricula INTEGER PRIMARY KEY,
  none_aluno TEXT NOT NULL,
  genero TEXT NOT NULL
);
-- injeção de dados-teste
INSERT INTO alunos VALUES (1, 'Marina', 'F');
INSERT INTO alunos VALUES (2, 'Davi', 'M');

-- Consultando as injeções realizadas
SELECT * FROM alunos WHERE matricula=1;



