SELECT p.name FROM people p, stars s, movies m
WHERE s.person_id = p.id
AND m.id= s.movie_id
AND m.title= 'Toy Story';