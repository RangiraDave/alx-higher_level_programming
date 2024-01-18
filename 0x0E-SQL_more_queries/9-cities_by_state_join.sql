-- Script to display all cities in the database.

SELECT cities.id as i, cities.name, states.name FROM cities ORDER BY i ASC JOIN states;
