CREATE DATABASE airpulse;
USE airpulse;

CREATE TABLE empresa(
	id INT PRIMARY KEY AUTO_INCREMENT, 
	razaoSocial VARCHAR(100),
	nomeFantasia VARCHAR(100),
	cnpj CHAR(14),
	segmentoAtuacao VARCHAR(80),
	email VARCHAR(50),
	fkEndereco INT,
	CONSTRAINT ctFkEndereco
	FOREIGN KEY(fkEndereco)
	REFERENCES endereco(id)
);

CREATE TABLE endereco(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cep CHAR(8),
	logradouro VARCHAR(30),
	bairo VARCHAR(70),
	numero VARCHAR(20),
	estado CHAR(2),
	cidade VARCHAR(50)
);

CREATE TABLE funcionario(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(60),
	dtNascimento DATE,
	emailCorporativo VARCHAR(50),
	telefone VARCHAR(20),
	cpf CHAR(11),
	cargo VARCHAR(30),
	adm TINYINT,
	senha VARCHAR(40),
	
	fkEmpresa INT,
	CONSTRAINT ctFkEmpresa
	FOREIGN KEY (fkEmpresa)
	REFERENCES empresa(id)
);

CREATE TABLE aviao(
	id INT PRIMARY KEY AUTO_INCREMENT,
	prefixo VARCHAR(50),
	companhia VARCHAR(60)
);

-- CREATE TABLE componentes(
-- 	id INT PRIMARY KEY AUTO_INCREMENT,
	-- tipo VARCHAR(50),
	-- unidadeMedida VARCHAR(30),
	-- modelo VARCHAR(100),
	-- capacidadeMax VARCHAR(100),
-- 	fkAviao INT,
-- 	CONSTRAINT ctFkAviao
-- 	FOREIGN KEY (fkAviao)
-- 	REFERENCES aviao(id),
-- 	fkComputador INT,
-- 	CONSTRAINT ctFkComputador 
-- 	FOREIGN KEY (fkComputador)
-- 	REFERENCES computador(id),
	-- fkEmpresa INT,
	-- CONSTRAINT ctFkEmpresa
	-- FOREIGN KEY (fkEmpresa)
	-- REFERENCES empresa(id)
-- );

-- CREATE TABLE computador(
-- 	id PRIMARY KEY AUTO_INCREMENT,


-- );

-- CREATE TABLE parametros(
-- 	id PRIMARY KEY AUTO_INCREMENT,

-- 	fkComponente INT,
-- 	CONSTRAINT ctFkComponente
-- 	FOREIGN KEY (fkComponente)
-- 	REFERENCES 
-- );