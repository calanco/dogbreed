DROP DATABASE IF EXISTS dogbreed;

CREATE DATABASE dogbreed;

\c dogbreed;

CREATE TYPE size AS ENUM ('small', 'medium', 'large', 'extra_large');
CREATE TYPE energy_level AS ENUM ('low', 'moderate', 'high');

CREATE TABLE breeds(
    id SERIAL PRIMARY KEY,
    breed varchar(50) UNIQUE NOT NULL,
    size size,
    energy_level energy_level,
    image_link varchar(100)
);

INSERT INTO breeds (id, breed, size, energy_level) VALUES 
(1, 'American Foxhound', 'large', 'high'),
(2, 'Boston Terrier', 'small', 'moderate'),
(3, 'Irish Wolfhound Terrier', 'extra_large', 'low'),
(4, 'American Bulldog', 'large', 'high');