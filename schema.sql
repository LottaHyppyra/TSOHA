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
    kayttaja_id INTEGER REFERENCES users
)