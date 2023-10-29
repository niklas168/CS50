SELECT DISTINCT m.title FROM people p, movies m, ratings r, stars s
WHERE m.id= r.movie_id
AND s.person_id=p.id
AND s.movie_id = m.id
AND p.name='Chadwick Boseman'
ORDER BY rating desc
limit 5;