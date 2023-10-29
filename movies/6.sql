SELECT avg(rating) FROM ratings r, movies m
WHERE r.movie_id = m.id
AND m.year=2012;