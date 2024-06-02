-- lists all cities of california that can be found in hbtn_0d_usa database
SELECT id, name FROM cities WHERE states.id IN ( SELECT id FROM states WHERE name = 'California') ORDER BY id;
