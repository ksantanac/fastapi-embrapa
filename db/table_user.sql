-- Script para criar tabela usuarios MySQL
-- CREATE TABLE usuarios (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     username VARCHAR(50) NOT NULL,
--     password VARCHAR(255) NOT NULL
-- );

-- Script para criar tabela usuarios PostgreSQL
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);