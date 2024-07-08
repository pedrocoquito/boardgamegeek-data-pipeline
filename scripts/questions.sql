# 1 
SELECT name, rating_average, users_rated
FROM games_dimension gd
JOIN facts_table ft ON gd.id = ft.id
ORDER BY rating_average DESC, users_rated DESC
LIMIT 20;

# 2
SELECT play_time, AVG(rating_average) AS avg_rating, AVG(users_rated) AS avg_users_rated
FROM games_dimension gd
JOIN facts_table ft ON gd.id = ft.id
GROUP BY play_time
ORDER BY play_time
LIMIT 20;

# 3


# 4
SELECT year_published, AVG(rating_average) AS avg_rating, COUNT(gd.id) AS num_games
FROM games_dimension gd
JOIN facts_table ft ON gd.id = ft.id
WHERE year_published BETWEEN 2000 AND 2020
GROUP BY year_published
ORDER BY year_published;

# 5
SELECT dd.domain_name, AVG(ft.rating_average) AS avg_rating, COUNT(gd.id) AS num_games
FROM domains_dimension dd
JOIN facts_table ft ON dd.id = ft.id
JOIN games_dimension gd ON gd.id = dd.id
GROUP BY dd.domain_name
ORDER BY avg_rating DESC, num_games DESC
LIMIT 20;
