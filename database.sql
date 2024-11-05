CREATE DATABASE vote;
USE vote;
show databases;
CREATE TABLE voters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    has_voted BOOLEAN DEFAULT FALSE
);

CREATE TABLE candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE votes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    voter_id INT,
    candidate_id INT,
    FOREIGN KEY (voter_id) REFERENCES voters(id) ON DELETE CASCADE,
    FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE
);








-- CREATE TABLE IF NOT EXISTS voters (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(255) NOT NULL,
--     email VARCHAR(255) NOT NULL UNIQUE,
--     has_voted BOOLEAN DEFAULT FALSE
-- );

-- CREATE TABLE IF NOT EXISTS votes (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     voter_email VARCHAR(255) NOT NULL,
--     candidate VARCHAR(255) NOT NULL,
--     FOREIGN KEY (voter_email) REFERENCES voters(email)
-- );


select * from votes;
select * from voters;
select * from candidates;
