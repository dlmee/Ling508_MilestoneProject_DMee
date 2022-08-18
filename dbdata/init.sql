DROP DATABASE IF EXISTS mcdonald;
CREATE DATABASE mcdonald;
USE mcdonald;

CREATE TABLE lexicon (
    id INT NOT NULL AUTO_INCREMENT,
    wform VARCHAR(50) NOT NULL,
    indexed_sents VARCHAR(800),
    PRIMARY KEY (id)
);

INSERT INTO lexicon
    (wform, indexed_sents)
VALUE ('buzzwole', 'these would be indexed sentences e.g. 1,17,542,1091');

CREATE TABLE sensicon (
    id INT NOT NULL AUTO_INCREMENT,
    wform VARCHAR(50) NOT NULL,
    sense INT,
    definition VARCHAR(200),
    indexed_sents VARCHAR(200),
    PRIMARY KEY (id)
);

INSERT INTO sensicon
    (wform, sense, definition, indexed_sents)
VALUE ('buzzwole', 1, 'a pokemon that is every programmers nightmare', 'example indices 3,5,900');

CREATE TABLE lemma (
    id INT NOT NULL AUTO_INCREMENT,
    lform VARCHAR(50) NOT NULL,
    wforms VARCHAR(270),
    PRIMARY KEY (id)
);

INSERT INTO lemma
    (lform, wforms)
VALUE ('buzzwole', 'buzzowling, buzzing, buzzwoled');

CREATE TABLE vectors (
    wform VARCHAR(50) NOT NULL,
    lform VARCHAR(50),
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