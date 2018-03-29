/* advanced select */

SELECT CASE
WHEN A + B > C AND A + C > B AND B + C > A
  THEN CASE
  WHEN A = B AND B = C THEN "Equilateral"
  WHEN A = B OR B = C OR A = C THEN "Isoceles"
  ELSE "Scalene"
  END
  ELSE "Not A Triangle"
  END FROM TRIANGLES;




SELECT CONCAT(Name,"(",Substring(Occupation,1,1),")") as Name
FROM Occupations
ORDER BY Name
SELECT CONCAT("There are a total of ",COUNT(Occupation)," ",LOWER(Occupation),"s.") AS total
FROM OCCUPATIONS
GROUP BY occupation
ORDER BY total;

/* pivoting */

SELECT * FROM
(SELECT )
