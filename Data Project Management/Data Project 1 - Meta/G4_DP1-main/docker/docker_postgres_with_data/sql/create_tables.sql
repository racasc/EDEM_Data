-- Creation of raw_data table
CREATE TABLE IF NOT EXISTS raw_data
(
    id
              INT,
    name
              VARCHAR(50),
    last_name VARCHAR(50),
    f1        INT,
    f2        INT,
    f3        INT,
    f4        INT,
    f5        INT,
    f6        INT,
    f7        INT,
    f8        INT,
    f9        INT,
    f10       INT,
    lat       FLOAT,
    lon       FLOAT,
    transport VARCHAR(50),
    age       INT,
    gender    VARCHAR(5),
    weight    FLOAT,
    height    FLOAT,
    time      TIMESTAMP,
    PRIMARY KEY
        (
         id,
         time
            )
);


-- Creation of matches table
CREATE TABLE IF NOT EXISTS matches
(
    user_id
             INT,
    user_lat
             FLOAT,
    user_lon
             FLOAT,
    friend_id
             INT,
    friend_lat
             FLOAT,
    friend_lon
             FLOAT,
    transport
             VARCHAR(50),
    distance FLOAT,
    time     TIMESTAMP,
    PRIMARY KEY
        (
         user_id,
         friend_id,
         time
            )
);

-- Creation of USER and PERMISSIONS FOR GRAFANA
CREATE
    USER grafanareader WITH PASSWORD 'metaverso';
GRANT CONNECT
    ON DATABASE metaverso TO grafanareader;
GRANT SELECT ON raw_data TO grafanareader;
GRANT SELECT ON matches TO grafanareader;

CREATE
    USER grafana WITH PASSWORD 'metaverso';
GRANT
    SELECT
    ON ALL TABLES IN SCHEMA public TO grafana;
GRANT
    EXECUTE
    ON
    ALL
    FUNCTIONS IN SCHEMA public TO grafana;