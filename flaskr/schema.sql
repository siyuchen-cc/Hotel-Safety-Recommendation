DROP TABLE IF EXISTS crimes;
DROP TABLE IF EXISTS police;

CREATE TABLE crimes (
    cases TEXT PRIMARY KEY,
    date DATETIME NOT NULL,
    block TEXT NOT NULL,
    iucr TEXT NOT NULL,
    primaryDescription TEXT NOT NULL,
    secondaryDescription TEXT NOT NULL,
    locationDescription TEXT NOT NULL,
    arrest CHAR(10) NOT NULL,
    domestic CHAR(10) NOT NULL,
    beat INT NOT NULL,
    ward INT NOT NULL,
    fbiCD CHAR(10) NOT NULL,
    x INT,
    y INT,
    latitude REAL,
    longitude REAL
);

CREATE TABLE police (
    district TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip INT NOT NULL,
    website TEXT NOT NULL,
    phone TEXT,
    fax TEXT,
    tty TEXT,
    x REAL NOT NULL,
    y REAL NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    FOREIGN KEY (latitude) REFERENCES crimes (latitude),
    FOREIGN KEY (longitude) REFERENCES crimes (longitude)
);