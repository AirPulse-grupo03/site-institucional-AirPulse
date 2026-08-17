CREATE TABLE empresa(
	id PRIMARY KEY AUTO_INCREMENT, 
	razaoSocial VARCHAR(100),
	nomeFantasia VARCHAR(100),
	cnpj CHAR(14),
	segmentoAtuacao (80),
	website VARCHAR(50),
	email VARCHAR(50),
	fkEndereco INT,
	CONSTRAINT ctFkEndereco
	FOREIGN KEY(fkEndereco)
	REFERENCES endereco(id)
);

CREATE TABLE endereco(
	endereco INT PRIMARY KEY AUTO_INCREMENT,
	cep CHAR(8),
	logradouro VARCHAR(30),
	nome VARCHAR(70),
	numero VARCHAR(20),
	estado CHAR(2),
	cidade VARCHAR(50)
);

CREATE TABLE funcionario(
	id PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(60),
	dtNascimento DATE,
	emailCorporativo VARCHAR(50),
	telefone VARCHAR()
	cpf CHAR(11),
	cargo VARCHAR(30),
	departamento VARCHAR(40),
	senha VARCHAR(40),
	
	fkEmpresa INT,
	CONSTRAINT ctFkEmpresa
	FOREIGN KEY (fkEmpresa)
	REFERENCES empresa(id),
	fkPermissao INT,
	CONSTRAINT ctFkPermissao
	FOREIGN KEY (fkPermissao)
	REFERENCES permissao(id)
);

CREATE TABLE permissao(
	id INT PRIMARY KEY AUTO_INCREMENT, 
	permissao VARCHAR(40),
	especificacao VARCHAR(100)
);

-- CREATE TABLE aviao(
-- 	id INT PRIMARY KEY AUTO_INCREMENT,
-- 	prefixo VARCHAR(50),
-- 	companhia VARCHAR(60),
-- );

-- CREATE TABLE componentes(
-- 	id INT PRIMARY KEY AUTO_INCREMENT,

-- 	fkAviao INT,
-- 	CONSTRAINT ctFkAviao
-- 	FOREIGN KEY (fkAviao)
-- 	REFERENCES aviao(id),
-- 	fkComputador INT,
-- 	CONSTRAINT ctFkComputador 
-- 	FOREIGN KEY (fkComputador)
-- 	REFERENCES computador(id),

-- );

-- CREATE TABLE computador(
-- 	id PRIMARY KEY AUTO_INCREMENT,


-- );

-- CREATE TABLE parametros(
-- 	id PRIMARY KEY AUTO_INCREMENT,

-- 	fkComponente INT<
-- 	CONSTRAINT ctFkComponente
-- 	FOREIGN KEY (fkComponente)
-- 	REFERENCES 
-- );

INSERT INTO permissao (permissao, especificacao) VALUES
("Acesso total", "Cadastros, permissões, relatórios, configurações"),
("Acesso operacional", "Sem gerenciamento de usuários"),
("Visualização e acompanhamento", "Visualização da dashboard e acompanhamento de alertas"),