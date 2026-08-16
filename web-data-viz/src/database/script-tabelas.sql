CREATE DATABASE empresa(
	id PRIMARY KEY AUTO_INCREMENT, 
	razaoSocial VARCHAR(100),
	cnp CHAR(14)
);

CREATE DATABASE funcionario(
	id PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(60),
	dtNascimento DATE,
	cpf CHAR(11),
	cargo VARCHAR(30),
	fkEmpresa INT,
	CONSTRAINT ctFkEmpresa
	FOREIGN KEY (fkEmpresa)
	REFERENCES empresa(id)
);

CREATE DATABASE permissoes(
	permissao VARCHAR(40)
);

CREATE DATABASE funcionario_permissao(
	fkFuncionario INT,
	fkPermissao INT,
	CONSTRAINT ctFkFuncionario
	FOREIGN KEY (fkFuncionario)
	REFERENCES funcionario(id),
	CONSTRAINT ctFkPermissao
	FOREIGN KEY (fkPermissao)
	REFERENCES permissoes(id)
);
