CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    kayttajatunnus TEXT,
    salasana TEXT,
    bongaukset INTEGER
);

CREATE TABLE bongaukset (
    id SERIAL PRIMARY KEY,
    laji TEXT,
    paikka TEXT,
    spotted DATE,
    kayttaja_id INTEGER REFERENCES users
);

CREATE TABLE birds (
    id SERIAL PRIMARY KEY,
    latin_name TEXT,
    name TEXT, 
    family TEXT
);

CREATE TABLE family (
    id SERIAL PRIMARY KEY,
    name TEXT
);