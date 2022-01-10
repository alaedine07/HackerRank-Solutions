select concat(Name,'(',Substring(Occupation,1,1),')')
from OCCUPATIONS
order by Name;
SELECT concat('There are a total of ',' ',count(Occupation),' ',lower(Occupation),'s.') as occurences
from occupations
group by occupation
order by occurences;
