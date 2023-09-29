create database empresa;

CREATE TABLE empresa.employees (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    salary INT(10) NOT NULL
);

create user 'empresa'@'%' identified by 'empresa123';

grant all privileges on empresa.* to 'empresa'@'%';
