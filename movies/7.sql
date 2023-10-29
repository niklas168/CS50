SELECT m.title, r.rating FROM ratings r, movies m
WHERE r.movie_id = m.id
AND m.year=2010
ORDER BY r.rating desc, m.title
