-- Script to display cities of California that can be found
-- in the database.

SELECT id, name FROM cities WHERE states.name = 'California' ORDER BY cities.id ASC;
