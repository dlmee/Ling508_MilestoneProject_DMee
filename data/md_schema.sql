DROP SCHEMA IF EXISTS mcdonald;
CREATE SCHEMA mcdonald;
USE mcdonald;

CREATE TABLE lexicon (
    id INT NOT NULL AUTO_INCREMENT,
    wordform VARCHAR(30) NOT NULL,
    pos VARCHAR(30),
    PRIMARY KEY (id)
)

