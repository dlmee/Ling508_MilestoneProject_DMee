DROP DATABASE IF EXISTS mcdonald;
CREATE DATABASE mcdonald;
USE mcdonald;

CREATE TABLE lexicon (
    id INT NOT NULL AUTO_INCREMENT,
    wform VARCHAR(30) NOT NULL,
    sense INT,
    definition VARCHAR(300),
    examplesents VARCHAR(450),
    PRIMARY KEY (id)
);

INSERT INTO lexicon
    (wform, sense, definition, examplesents)
VALUE ('bug', 1, 'example, test, initializing', 'programmers least favorite creatures are bugs!');

CREATE TABLE lemma (
    id INT NOT NULL AUTO_INCREMENT,
    lform VARCHAR(15) NOT NULL,
    wforms VARCHAR(270),
    PRIMARY KEY (id)
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

CREATE TABLE context_sentences (
    id INT NOT NULL AUTO_INCREMENT,
    chapter INT,
    sentence VARCHAR(400),
    vecfriendly VARCHAR(350),
    PRIMARY KEY (id)
);

INSERT INTO context_sentences
    (chapter, sentence, vecfriendly)
VALUE (1, 'Curdie was the son of Peter the miner.', '(curdie, 1), (was, 1), (the, 2), (son, 1), (of, 1), (peter, 1), (miner, 1)');