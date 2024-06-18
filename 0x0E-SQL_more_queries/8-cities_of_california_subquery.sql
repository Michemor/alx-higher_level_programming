-- lists all cities of california that can be found in hbtn_0d_usa database
SELECT cities.id, cities.name FROM states, cities WHERE cities.state_id = states.id AND states.name = 'California' ORDER BY cities.id ASC;
