SELECT p2.name FROM movies m, people p1, people p2, stars s1, stars s2
WHERE m.id =  s1.movie_id AND m.id = s2.movie_id
AND p1.id=s1.person_id AND p2.id = s2.person_id
AND p1.name = 'Kevin Bacon' AND p1.birth=1958
AND p2.name != 'Kevin Bacon';