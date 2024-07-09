-- QUESTION 1 
SELECT g.name, f.rating_average, f.owned_users
FROM facts_normalized f
JOIN games_dimension_normalized g ON f.game_id = g.game_id
ORDER BY f.owned_users DESC, f.rating_average DESC
LIMIT 10;

-- QUESTION 2
SELECT CORR(g.play_time, f.rating_average) AS correlation_play_time_rating,
       CORR(g.play_time, f.owned_users) AS correlation_play_time_popularity
FROM facts_normalized f
JOIN games_dimension_normalized g ON f.game_id = g.game_id;

-- QUESTION 3
SELECT CORR(g.min_age, f.owned_users) AS correlation_min_age_popularity
FROM facts_normalized f
JOIN games_dimension_normalized g ON f.game_id = g.game_id;

-- QUESTION 4
SELECT g.name, f.complexity_average
FROM facts_normalized f
JOIN games_dimension_normalized g ON f.game_id = g.game_id
ORDER BY f.owned_users DESC
LIMIT 10;

-- QUESTION 5
SELECT g.year_published, 
       AVG(f.rating_average) AS avg_rating, 
       SUM(f.owned_users) AS total_owners
FROM facts_normalized f
JOIN games_dimension_normalized g ON f.game_id = g.game_id
GROUP BY g.year_published
ORDER BY g.year_published;


-- QUESTION 6
-- Mechanics
SELECT m.mechanic_name, 
       AVG(f.rating_average) AS avg_rating, 
       SUM(f.owned_users) AS total_owners
FROM facts_normalized f
JOIN mechanics_dimension m ON f.game_id = m.game_id
GROUP BY m.mechanic_name
ORDER BY total_owners DESC, avg_rating DESC
LIMIT 10;

-- Domains
SELECT d.domain_name, 
       AVG(f.rating_average) AS avg_rating, 
       SUM(f.owned_users) AS total_owners
FROM facts_normalized f
JOIN mechanics_dimension m ON f.game_id = m.game_id
JOIN domains_dimension d ON f.game_id = d.game_id
GROUP BY d.domain_name
ORDER BY total_owners DESC, avg_rating DESC
LIMIT 10;

-- QUESTION 7
SELECT CORR(f.owned_users, f.rating_average) AS correlation_popularity_rating
FROM facts_normalized f;

-- QUESTION 8
SELECT g.min_players, g.max_players, 
       AVG(f.owned_users) AS avg_popularity
FROM facts_normalized f
JOIN games_dimension_normalized g ON f.game_id = g.game_id
GROUP BY g.min_players, g.max_players
ORDER BY avg_popularity DESC
LIMIT 10;
