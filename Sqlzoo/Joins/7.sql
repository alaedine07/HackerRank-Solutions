SELECT player
FROM goal JOIN game ON (matchid = id)
WHERE stadium = 'National Stadium, Warsaw'