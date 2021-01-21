SELECT Name AS Country, Continent AS B, Region AS "ANSWER"FROM COUNTRY;
# Column 선택할 떄
SELECT Name, Continent, Region FROM Country WHERE Continent = 'Europe' ORDER BY Name LIMIT 5 OFFSET 10;
# Row 선택할 때 