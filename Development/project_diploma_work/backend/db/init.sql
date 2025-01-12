CREATE DATABASE IF NOT EXISTS parser;
USE parser;

CREATE TABLE IF NOT EXISTS initial_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO initial_table (name) VALUES ('Test Entry');
