-- Database: ev_intelligence

-- DROP DATABASE IF EXISTS ev_intelligence;

CREATE DATABASE ev_intelligence
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_India.1252'
    LC_CTYPE = 'English_India.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


SELECT COUNT(*) FROM ev_stations;

SELECT state, SUM(charger_count) AS total_chargers
FROM ev_stations
GROUP BY state
ORDER BY total_chargers DESC;

SELECT *
FROM ev_stations
LIMIT 5;