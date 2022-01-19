SELECT mdate, teamname
FROM game JOIN eteam ON (eteam.id = team1)
WHERE coach = 'Fernando Santos'