-- Script to display all cities in the database.

SELECT cities.id, cities.name, states.name
FROM cities
NATURAL JOIN states
ORDER BY cities.id ASC;
