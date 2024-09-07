CREATE DATABASE IF NOT EXISTS craftyspider;

USE craftyspider;

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR (255) NOT NULL,
    email VARCHAR (255) NOT NULL,
    registration_date DATE NOT NULL,
    country VARCHAR (255) NOT NULL,
    purchased_pattern_sku VARCHAR (255) NOT NULL
);

CREATE TABLE IF NOT EXISTS patterns (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR (255) NOT NULL,
    name VARCHAR (255) NOT NULL,
    category VARCHAR (255) NOT NULL,
    price FLOAT NOT NULL,
    dificulty_level VARCHAR (255) NOT NULL,
    publication_date DATE NOT NULL
);