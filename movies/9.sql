SELECT DISTINCT p.name FROM people p, stars s, movies m
WHERE s.person_id = p.id
AND m.id= s.movie_id
AND m.year= 2004
ORDER BY p.birth;