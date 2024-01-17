-- Script to display cities of California that can be found
-- in the database.

SELECT states.id, cities.name FROM cities WHERE states.id = cities.state_id ORDER BY cities.id ASC;
