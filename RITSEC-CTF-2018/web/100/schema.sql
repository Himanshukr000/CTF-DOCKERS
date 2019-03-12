CREATE DATABASE challenge;
USE challenge;

CREATE TABLE spaceships (
    name varchar(40),
    kills int,
    captain varchar(75),
    CONSTRAINT test_pk PRIMARY KEY(name)
);

INSERT INTO spaceships (name, kills, captain) VALUES
('Herminia', 2,'Ruben Dowling'),
('The Javelin', 32,'Asha Stark'),
('Thor', 0,'Jack Rankin'),
('Brotherhood', 5,'Reuben Mccaffrey'),
('Dagger', 4,'Raphael Rodriguez'),
('SSE Twilight', 10,'Ernest Durham'),
('LWSS Rampart', 21,'Austin Scott'),
('SS Roosevelt', 19,'Adnan Lam'),
('HWSS Defiance', 15,'Kyron Amos'),
('flag', 0,'lol it isnt that easy'),
('LbtebKe6yrU8vEnx', 9001,'RITSEC{hey_there_h4v3_s0me_point$_3ny2Lx}'),
('LWSS Valhalla', 26,'Derek Drummond');

CREATE USER 'webserver'@'%' IDENTIFIED BY 'PP6L43BZpGUi9zC5oaRTbKQT4XBm';
GRANT SELECT ON challenge.* to 'webserver'@'%';

FLUSH PRIVILEGES;