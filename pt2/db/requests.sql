SELECT title, premiered
FROM titles
WHERE premiered < 2018;

SELECT title, votes
FROM titles t
    JOIN rating r ON t.title_id = r.title_id
ORDER BY votes DESC
LIMIT 50;

SELECT title, rating, votes
FROM titles t
    JOIN rating r ON t.title_id = r.title_id
    JOIN film_genres fg ON r.title_id = fg.title_id
    JOIN genre_types gt ON fg.genre_id = gt.id
WHERE genre_name = 'Comedy' AND rating >= 7 AND premiered = 2019
ORDER BY votes DESC
LIMIT 10;

SELECT title, premiered
FROM titles
    JOIN crew c ON titles.title_id = c.title_id
    JOIN role_categories rc ON rc.id = c.category AND rc.role_type = 'actor'
    JOIN people p ON c.person_id = p.person_id AND p.name = 'Dennis Hopper';

SELECT premiered, COUNT(title) titles
FROM titles t
    JOIN film_genres fg ON t.title_id = fg.title_id
    JOIN genre_types gt ON gt.id = fg.genre_id AND gt.genre_name = 'Film-Noir'
GROUP BY premiered;

SELECT name, born, died , IFNULL(died, 2022) - born age
FROM people p
WHERE EXISTS(
    SELECT *
    FROM crew c
        JOIN role_categories rc ON c.category = rc.id AND rc.role_type = 'actor'
    WHERE c.person_id = p.person_id
    ) AND age > 50
ORDER BY age DESC
LIMIT 10

SELECT name, born, died, IFNULL(died, 2022) - born age
FROM people p
WHERE EXISTS(
    SELECT *
    FROM crew c
        JOIN role_categories rc ON rc.id = c.category AND rc.role_type = 'actor'
    WHERE c.person_id = p.person_id
    )
    AND age >= 100
ORDER BY died DESC;

SELECT rating
FROM rating r
    JOIN film_genres fg ON r.title_id = fg.title_id
    JOIN genre_types gt ON fg.genre_id = gt.id
WHERE gt.genre_name = 'Comedy';

SELECT premiered, genre_name, AVG(fem_perc) female_percentage
FROM (
    SELECT title, premiered, genre_name, SUM(CASE WHEN rc.role_type = 'actress' THEN 1.0 ELSE 0 END) / SUM(CASE WHEN rc.role_type = 'actress' or rc.role_type = 'actor' THEN 1 ELSE 0 END) fem_perc
    FROM titles t
        JOIN crew c ON t.title_id = c.title_id
        JOIN role_categories rc ON c.category = rc.id
        JOIN film_genres fg ON t.title_id = fg.title_id
        JOIN genre_types gt ON fg.genre_id = gt.id
    WHERE premiered is not null
    GROUP BY title
)
WHERE fem_perc is not null
GROUP BY premiered, genre_name
ORDER BY premiered DESC;

SELECT name, born, died, IFNULL(died, 2022) - born age
FROM people p
WHERE EXISTS(
    SELECT *
    FROM crew c
        JOIN role_categories rc ON rc.id = c.category AND rc.role_type = 'actor'
    WHERE c.person_id = p.person_id
    )
ORDER BY age DESC
LIMIT 10;
