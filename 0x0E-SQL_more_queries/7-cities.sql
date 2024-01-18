-- Script to create database and put in cities table having
-- a primary key "id" and foreign key from states.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id));
