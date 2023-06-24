-- Creates the hbtn_0d_usa, uses it  and creates the cities table
-- with foreign key as states_id
CREATE database IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS cities
       (id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id) REFERENCES states(id)
);
