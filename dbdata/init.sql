DROP DATABASE IF EXISTS mcdonald;
CREATE DATABASE mcdonald;
USE mcdonald;

CREATE TABLE lexicon (
    id INT NOT NULL AUTO_INCREMENT,
    wform VARCHAR(30) NOT NULL,
    sense INT,
    sbvect VARCHAR(300),
    PRIMARY KEY (id)
);

INSERT INTO lexicon
    (wform, sense, sbvect)
VALUE ('bug', 1, 'example, test, initializing');

CREATE TABLE lemma (
    lform VARCHAR(15) NOT NULL,
    wforms VARCHAR(270),
    PRIMARY KEY (lform)
);

INSERT INTO lemma
    (lform, wforms)
VALUE ('bug', 'bug, bugging, bugged');

CREATE TABLE vectors (
    wform VARCHAR(30) NOT NULL,
    lform VARCHAR(15),
    vecform VARCHAR(450),
    PRIMARY KEY (wform)
);

INSERT INTO vectors
    (wform, lform, vecform)
VALUE ('bug', 'bug', 'programmer, exterminator, pest, insanity');

