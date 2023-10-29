SELECT DISTINCT p.name FROM people p, directors d, movies m, ratings r
WHERE d.person_id = p.id
AND m.id= d.movie_id
AND m.id = r.movie_id
AND r.rating >=9
ORDER BY m.year;