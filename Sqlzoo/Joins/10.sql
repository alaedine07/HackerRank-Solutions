select stadium, COUNT(*)
FROM game JOIN goal ON (matchid=id)
GROUP BY stadium