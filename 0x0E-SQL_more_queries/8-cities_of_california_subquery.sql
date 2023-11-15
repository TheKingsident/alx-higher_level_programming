-- Lists all the cities of California that can be found in the database hbtn_0d_usa
-- Select all cities from California
SELECT cities.id, cities.name 
FROM cities, (SELECT id FROM states WHERE name = 'California') AS california
WHERE cities.state_id = california.id
ORDER BY cities.id ASC;
