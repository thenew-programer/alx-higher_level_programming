--  lists all cities contained in the database hbtn_0d_usa.
SELECT C.id, C.name
FROM cities as C
INNER JOIN states as S
ON C.state_id = S.id;
