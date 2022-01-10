select h.hacker_id, h.name
from Submissions s
INNER JOIN challenges c
ON s.challenge_id = c.challenge_id
INNER JOIN Difficulty d
on c.difficulty_level = d.difficulty_level
INNER JOIN hackers h
on s.hacker_id = h.hacker_id
where s.score = d.score and c.difficulty_level = d.difficulty_level
group by h.hacker_id, h.name
having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, s.hacker_id asc