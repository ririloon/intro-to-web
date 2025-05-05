CREATE DATABASE mydb;

CREATE USER myuser WITH PASSWORD 'sql.2025';

GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

\c mydb

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100) UNIQUE
);

INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

SELECT * FROM users;