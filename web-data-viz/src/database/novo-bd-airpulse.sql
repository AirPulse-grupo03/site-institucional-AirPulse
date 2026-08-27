CREATE DATABASE airpulse;
USE airpulse;

CREATE TABLE endereco (
    id_endereco INT PRIMARY KEY AUTO_INCREMENT,
    cep CHAR(8) NOT NULL,
    logradouro VARCHAR(100) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    numero VARCHAR(20) NOT NULL,
    complemento VARCHAR(100),
    estado CHAR(2) NOT NULL,
    cidade VARCHAR(100) NOT NULL
);

-- fabricante dos computadores:
CREATE TABLE empresa_fabricante (
    id_empresa_fabricante INT PRIMARY KEY AUTO_INCREMENT,
    razao_social VARCHAR(100) NOT NULL,
    nome_fantasia VARCHAR(100),
    cnpj CHAR(14) UNIQUE NOT NULL,
    segmento_atuacao VARCHAR(80) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    status_sistema TINYINT NOT NULL, -- se a empresa está ativa no nosso sistema
    entrada_sistema DATETIME NOT NULL, -- quando foi cadastrada
    website VARCHAR(200),
    fk_endereco INT,
    FOREIGN KEY (fk_endereco) REFERENCES endereco(id_endereco)
);

CREATE TABLE funcionario (
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    email_corporativo VARCHAR(200) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    cpf CHAR(11) NOT NULL,
    adm TINYINT NOT NULL, -- ADM ou comum
    senha VARCHAR(200) NOT NULL,
    status_sistema TINYINT NOT NULL,
    entrada_sistema DATETIME NOT NULL,
    fk_empresa_fabricante INT,
    FOREIGN KEY (fk_empresa_fabricante) REFERENCES empresa_fabricante(id_empresa_fabricante)
);



CREATE TABLE aeronave (
    id_aeronave INT PRIMARY KEY AUTO_INCREMENT,
    prefixo VARCHAR(10) UNIQUE NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    fabricante_aeronave VARCHAR(100) NOT NULL,
    numero_serie VARCHAR(45) UNIQUE NOT NULL,
    status_aeronave VARCHAR(45) NOT NULL, -- se está ativa, em manutenção ou inativa
    entrada_sistema DATETIME NOT NULL,
    companhia_aerea VARCHAR(100)
);

CREATE TABLE computador (
    id_computador INT PRIMARY KEY AUTO_INCREMENT,
    numero_serie VARCHAR(45) UNIQUE NOT NULL, 
    modelo VARCHAR(100) NOT NULL,
    status_computador VARCHAR(45) NOT NULL, -- ATIVO, MANUTENCAO, INATIVO
    data_instalacao DATE NOT NULL, -- instalação no avião
    entrada_sistema DATETIME NOT NULL,
    fk_aeronave INT,
    fk_empresa_fabricante INT,
    FOREIGN KEY (fk_aeronave) REFERENCES aeronave(id_aeronave),
    FOREIGN KEY (fk_empresa_fabricante) REFERENCES empresa_fabricante(id_empresa_fabricante)
);

CREATE TABLE componente (
    id_componente INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(45) NOT NULL, -- cpu, ram, disco
    modelo VARCHAR(100),
    numero_serie VARCHAR(100), 
    capacidade_total DECIMAL(14,2),
    unidade_capacidade VARCHAR(45),
    status_monitoramento TINYINT,
    entrada_sistema DATETIME,
    fk_computador INT,
    FOREIGN KEY (fk_computador) REFERENCES computador(id_computador)
);

CREATE TABLE parametro_monitoramento (
    id_parametro_monitoramento INT PRIMARY KEY AUTO_INCREMENT,
    limite_atencao DECIMAL(14,2) NOT NULL,
    limite_critico DECIMAL(14,2) NOT NULL,
	fk_computador INT,
    FOREIGN KEY (fk_computador) REFERENCES computador(id_computador)
);

-- O que será monitorado em relação a qual componente
CREATE TABLE metrica (
    id_metrica INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    unidade_medida VARCHAR(45),
    descricao VARCHAR(200),
    fk_componente INT,
    fk_parametro_monitoramento INT,
    FOREIGN KEY (fk_componente) REFERENCES componente(id_componente),
    FOREIGN KEY (fk_parametro_monitoramento) REFERENCES parametro_monitoramento(id_parametro_monitoramento)
);


-- TESTE COM DADOS:

INSERT INTO endereco (cep, logradouro, bairro, numero, complemento, estado, cidade) VALUES 
('01001000', 'Praça da Sé', 'Sé', '100', 'Andar 5', 'SP', 'São Paulo'),
('20040020', 'Rua da Assembleia', 'Centro', '10', 'Sala 100', 'RJ', 'Rio de Janeiro');

INSERT INTO empresa_fabricante (razao_social, nome_fantasia, cnpj, segmento_atuacao, email, telefone, status_sistema, entrada_sistema, website, fk_endereco) VALUES 
('Honeywell International Inc.', 'Honeywell Aerospace', '12345678000199', 'Sistemas de Aviação', 'contato@honeywell.com', '11999999999', 1, NOW(), 'www.honeywell.com', 1),
('Thales Group Ltda', 'Thales Avionics', '98765432000188', 'Tecnologia Aeroespacial', 'suporte@thales.com', '21988888888', 1, NOW(), 'www.thalesgroup.com', 2);

INSERT INTO funcionario (nome, data_nascimento, email_corporativo, telefone, cpf, perfil, senha, status_sistema, entrada_sistema, fk_empresa_fabricante) VALUES 
('Carlos Engenheiro', '1985-05-10', 'carlos@honeywell.com', '11977777777', '12345678901', 1, 'senha_criptografada_1', 1, NOW(), 1),
('Ana Analista', '1990-08-20', 'ana@thales.com', '21966666666', '10987654321', 2, 'senha_criptografada_2', 1, NOW(), 2);

INSERT INTO aeronave (prefixo, modelo, fabricante_aeronave, numero_serie, status_aeronave, entrada_sistema, companhia_aerea) VALUES 
('PR-GOL', 'Boeing 737 MAX', 'Boeing', 'B737-SN001', 'ATIVO', NOW(), 'GOL Linhas Aéreas'),
('PT-TAM', 'Airbus A320neo', 'Airbus', 'A320-SN002', 'ATIVO', NOW(), 'LATAM Airlines');

INSERT INTO computador (numero_serie, modelo, status_computador, data_instalacao, entrada_sistema, fk_aeronave, fk_empresa_fabricante) VALUES 
('FMC-HW-9988', 'Pegasus FMC v1', 'ATIVO', '2023-01-15', NOW(), 1, 1), -- Computador da Honeywell no Boeing da GOL
('FMC-TH-7766', 'TopFlight FMC v2', 'ATIVO', '2023-02-20', NOW(), 2, 2); -- Computador da Thales no Airbus da LATAM

INSERT INTO componente (tipo, modelo, numero_serie, capacidade_total, unidade_capacidade, status_monitoramento, entrada_sistema, fk_computador) VALUES 
('CPU', 'Intel Core i7 Embarcado', 'CPU-HW-001', 3.50, 'GHz', 1, NOW(), 1), -- CPU do computador da Honeywell
('RAM', 'DDR4 ECC', 'RAM-TH-002', 16.00, 'GB', 1, NOW(), 2); -- RAM do computador da Thales

INSERT INTO parametro_monitoramento (limite_atencao, limite_critico, fk_computador) VALUES 
(80.00, 90.00, 1), -- Alertas para o computador Honeywell (Ex: 80% atenção, 90% crítico)
(75.00, 85.00, 2); -- Alertas para o computador Thales (Ex: 75% atenção, 85% crítico)

INSERT INTO metrica (nome, unidade_medida, descricao, fk_componente, fk_parametro_monitoramento) VALUES 
('Uso de Processamento CPU', '%', 'Percentual de carga da CPU do FMC em voo', 1, 1),
('Consumo de Memória RAM', '%', 'Percentual de uso da memória RAM do FMC', 2, 2);

SELECT 
    a.companhia_aerea AS 'Companhia',
    a.prefixo AS 'Prefixo Aeronave',
    emp.nome_fantasia AS 'Fabricante do FMC',
    comp.numero_serie AS 'Serial do Computador',
    c.tipo AS 'Componente',
    m.nome AS 'Métrica',
    pm.limite_critico AS 'Limite Crítico'
FROM metrica m
INNER JOIN componente c ON m.fk_componente = c.id_componente
INNER JOIN parametro_monitoramento pm ON m.fk_parametro_monitoramento = pm.id_parametro_monitoramento
INNER JOIN computador comp ON c.fk_computador = comp.id_computador
INNER JOIN aeronave a ON comp.fk_aeronave = a.id_aeronave
INNER JOIN empresa_fabricante emp ON comp.fk_empresa_fabricante = emp.id_empresa_fabricante;