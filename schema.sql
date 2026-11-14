CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE announcements (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    vähimmäismäärä INTEGER,
    user_id INTEGER REFERENCES users
);