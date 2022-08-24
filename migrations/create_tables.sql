DROP TABLE IF EXISTS players;

CREATE TABLE IF NOT EXISTS players (
  id serial PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  age INTEGER,
  height VARCHAR(255),
  weight VARCHAR(255),
  shot VARCHAR(255),
  birth_place VARCHAR(255),
  birthdate VARCHAR(255),
  number VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
