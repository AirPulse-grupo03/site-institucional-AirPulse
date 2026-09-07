-- init_admin.sql
-- Run this script against the database defined in .env.dev (DB_DATABASE=airpulse)
-- It creates a dummy company record (if not existing) and an admin employee
-- with the required credentials for the admin portal.

USE airpulse;

-- Insert the AirPulse company (adjust CNPJ if needed)
INSERT INTO empresa (nome, cnpj)
VALUES ('AirPulse', '00.000.000/0001-00');
SET @empresa_id = LAST_INSERT_ID();

-- Insert the admin employee linked to the company
INSERT INTO funcionario (nome, email_corporativo, senha, fk_empresa_fabricante, cpf, cargo)
VALUES ('Admin AirPulse', 'air.pulse@airpulse.com', 'urubu100', @empresa_id, '00000000000', 'ADMIN');
