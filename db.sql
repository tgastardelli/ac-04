/* Criação do banco e tabela */

CREATE DATABASE db_ac4;

USE db_ac4;

CREATE TABLE first(
      id smallint AUTO_INCREMENT
    , nome varchar(150) NOT NULL
    , sobrenome varchar(255) NOT NULL
    , numero bit NOT NULL
    , PRIMARY KEY (id)
);

INSERT INTO first (nome,sobrenome,numero) VALUES
("Thiago", "Gastardelli", 0);


