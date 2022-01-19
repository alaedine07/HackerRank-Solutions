SELECT id, mdate, count(*)
FROM game JOIN goal ON (id=matchid)
WHERE teamid='GER'
GROUP BY id, mdate