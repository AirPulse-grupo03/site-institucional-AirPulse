-- seed_admin.sql
-- Run this after the base schema (novo-bd-airpulse.sql) is loaded.
-- It creates the AirPulse company (if not present) and an admin employee
-- with the credentials required for the admin portal.

USE airpulse;

-- Insert the AirPulse company (you can adjust CNPJ if needed)
INSERT INTO empresa_fabricante (razao_social, nome_fantasia, cnpj, segmento_atuacao, email, telefone, status_sistema, entrada_sistema, website, fk_endereco)
VALUES ('AirPulse', 'AirPulse', '00000000000100', 'Gestão Interna', 'air.pulse@airpulse.com', '11999999999', 1, NOW(), NULL, NULL);
SET @empresa_id = LAST_INSERT_ID();

-- Insert the admin employee linked to the company
INSERT INTO funcionario (
    nome,
    data_nascimento,
    email_corporativo,
    telefone,
    cpf,
    cargo,
    adm,
    senha,
    status_sistema,
    entrada_sistema,
    fk_empresa_fabricante
) VALUES (
    'Admin AirPulse',
    '1990-01-01',
    'air.pulse@airpulse.com',
    '11999999999',
    '00000000000',
    'ADMIN',
    1,               -- adm = 1 (true)
    'urubu100',
    1,
    NOW(),
    @empresa_id
);
