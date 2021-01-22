SELECT Name AS Country, Continent AS B, Region AS "ANSWER"FROM COUNTRY;
# Column 선택할 떄
SELECT Name, Continent, Region FROM Country WHERE Continent = 'Europe' ORDER BY Name LIMIT 5 OFFSET 10;
# Row 선택할 때 

SELECT COUNT(*) FROM Country WHERE Population > 1000000;
Population > 1000000 이상인 것이 몇개인지 카운트 a

SELECT COUNT(LifeExpectancy) FROM Country; 
LifeExpectancy를 가지고 있는게 몇개 인지 카운트


SELECT COUNT(*) FROM Country WHERE Population > 1000000;
Population > 1000000 이상인 것이 몇개인지 카운트 a

SELECT COUNT(LifeExpectancy) FROM Country; 
#LifeExpectancy를 가지고 있는게 몇개 인지 카운트



SELECT * FROM customer;

INSERT INTO customer(name, address, city, state, zip)
    Values('Fred Flinstone', '123 Cobblestone way', 'Bedrock', 'CA', '91234');

INSERT INTO customer(name, city, state)
    Values('Jimi Hendrix', 'Renton', 'WA');
    
SELECT * FROM customer;

UPDATE customer SET address = '123 Music Avenue', zip = '02747' WHERE id = 5;
UPDATE customer SET address = '2603 S Washington St', zip = '98056' WHERE id = 6;
UPDATE customer SET address = NULL, zip = NULL WHERE id = 4;


SELECT * FROM customer WHERE id = 4;

DELETE FROM customer WHERE id = 4;
SELECT * FROM customer;

DELETE FROM customer WHERE id = 5;
SELECT * FROM customer;

the proper syntax for aliasing a field? 
SELECT FirstName AS "First Name";

an example of a query to get only data containing the word "Apple"? 
SELECT * FROM Fruits WHERE Name = 'Apple';


테이블 생성
CREATE TABLE test (
    a INTEGER,
    b TEXT
);

INSERT INTO test VALUES ( 1, 'a');
INSERT INTO test VALUES ( 2, 'b');
INSERT INTO test VALUES ( 3, 'c');
SELECT * FROM test;


CREATE TABLE test ( a , b  );
INSERT INTO test VALUES ('one', 'two');
SELECT * FROM test;
DROP TABLE test;
DROP TABLE IF EXISTS test;


DROP TABLE test;
CREATE TABLE test (a INTEGER, b TEXT, c TEXT);

INSERT INTO test VALUES ( 1, 'this', 'Right here!' );
INSERT INTO test (b, c) VALUES (' That', 'Over there!' );
INSERT INTO test DEFAULT VALUES;
INSERT INTO test ( a, b, c) SELECT id, name, description from item;

SELECT * FROM test;
SELECT * FROM test WHERE a = 1;
DELETE FROM test WHERE a = 1;

NULL은 VAlue가 아니라서, NULL인거 확인하려면 IS NULL로 해야함.. 위에 = 로 확인한 것은 Value라서 그런 것
SELECT * FROM test WHERE a IS NULL;


CREATE TABLE test (
 a INTEGER NOT NULL, 
 b TEXT NOT NULL,
 c TEXT 
);


INSERT INTO test VALUES (1, 'this', 'that');
INSERT INTO test (a,b) VALUES (1, 'two');

SELECT * FROM test;

DROP TABLE IF EXISTS test;



UNIQUE는 이 테이블 안에 똑같은 값이 하나만 있어야 할 때 설정, NOT NULL은 값이 NULL값이 들어가거나 EMPTY가 되지 않도록 할 때 설정
DEFAULT는 아무것도 안들어온다면, 항상 디폴트 값을 주고 싶을 때 설정 
DROP TABLE IF EXISTS test;
CREATE TABLE test (a TEXT UNIQUE, b TEXT NOT NULL, c TEXT DEFAULT 'panda');
INSERT INTO test (a, b) VALUES ('one', 'two');
INSERT INTO test (a, b) VALUES ('one', 'two');
SELECT * FROM test;


ALTER는 뒤에 Column을 추가할 때 사용함
DROP TABLE IF EXISTS test;
CREATE TABLE test (a TEXT, b TEXT, c TEXT);
INSERT INTO test VALUES ('one', 'two', 'three');
INSERT INTO test VALUES ('two', 'thre', 'four');
INSERT INTO test VALUES ('three', 'four', 'five');
SELECT * FROM test;

ALTER TABLE test ADD e TEXT DEFAULT 'panda';



PRIMARY KEY를 쓰면, ID 넘버가 자동으로 생성 됨. 

DROP TABLE IF EXISTS test;
CREATE TABLE test (
    id INTEGER PRIMARY KEY,
    a INTEGER,
    b TEXT
);

INSERT INTO test (a, b) VALUES ( 10, 'a');
INSERT INTO test (a, b) VALUES ( 11, 'b');
INSERT INTO test (a, b) VALUES ( 12, 'c');
SELECT * FROM test;



SELECT Name, Continent, Population FROM Country
    WHERE Population < 100000 OR Population IS NULL ORDER BY Population DESC;
    
SELECT Name, Continent, Population FROM Country
    WHERE Population < 100000 AND Continent = 'Oceania' ORDER BY Population DESC;

// 앞 뒤로 island라는 말이 붙어 있는거 다 고르기
SELECT Name, Continent, Population FROM Country
    WHERE Name Like '%island%' ORDER BY Name;
    
// ~~ Island로 끝나는 거 고르기
SELECT Name, Continent, Population FROM Country
    WHERE Name Like '%island' ORDER BY Name;
    
// Island ~~ 로 끝나는 거 고르기 
SELECT Name, Continent, Population FROM Country
    WHERE Name Like 'island%' ORDER BY Name;



// 인구수가 100000 미만이고, 오세아니아 대륙인 것들을 Popluation을 기준으로 디센딩하게 뽑기
SELECT Name, Continent, Population FROM Country
    WHERE Population < 100000 AND Continent = 'Oceania' ORDER BY Population DESC;

// Continent 콜럼안에서 유럽과 아시아인 것만 뽑아내기
SELECT Name, Continent, Population FROM Country
    WHERE Continent IN ('Europe', 'Asia') ORDER BY Name;



SELECT Continent FROM Country;

// SELECT DISTINCT는 중복된 거 없애는 것.. 이 예시에서는 Continent에서 중복된 것들 없애는 것 
SELECT DISTINCT Continent FROM Country;



//a, b 콜럼 합해서 Test테이블 안에서 중복된거 없이 구하기
SELECT DISTINCT a,b FROM test;
// b 콜럼만 따져서 중복된거 없이 하기 
SELECT DISTINCT a FROM test;


DROP TABLE test;

CREATE TABLE test (a INTEGER, b TEXT, c TEXT);

INSERT INTO test VALUES ( 1, 'this', 'Right here!' );

INSERT INTO test (b, c) VALUES (' That', 'Over there!' );

INSERT INTO test DEFAULT VALUES;

INSERT INTO test ( a, b, c) SELECT id, name, description from item;

SELECT * FROM test;
SELECT * FROM test WHERE a = 1;
DELETE FROM test WHERE a = 1;

INSERT INTO test(a, b, c) VALUES (0, NULL, '');
SELECT * FROM test WHERE b IS NULL;
SELECT * FROM test WHERE c = '';

DROP TABLE IF EXISTS test;

CREATE TABLE test (
 a INTEGER NOT NULL, 
 b TEXT NOT NULL,
 c TEXT 
);


INSERT INTO test VALUES (1, 'this', 'that');
INSERT INTO test (a,b) VALUES (1, 'two');

SELECT * FROM test;
DROP TABLE IF EXISTS test;
CREATE TABLE test (a TEXT UNIQUE NOT NULL, b TEXT NOT NULL, c TEXT DEFAULT 'panda');
INSERT INTO test (a, b) VALUES (NULL, 'two');
INSERT INTO test (a, b) VALUES (NULL, 'two');
SELECT * FROM test;

DROP TABLE IF EXISTS test;
CREATE TABLE test (a TEXT, b TEXT, c TEXT);
INSERT INTO test VALUES ('one', 'two', 'three');
INSERT INTO test VALUES ('two', 'thre', 'four');
INSERT INTO test VALUES ('three', 'four', 'five');
UPDATE test SET a = 'change?', b = 'well..', c = 'hacked' WHERE a = 'one';
SELECT * FROM test;

ALTER TABLE test ADD e TEXT DEFAULT 'panda';

DROP TABLE IF EXISTS test;
CREATE TABLE test (
    id INTEGER PRIMARY KEY,
    a INTEGER,
    b TEXT
);

INSERT INTO test (a, b) VALUES ( 10, 'a');
INSERT INTO test (a, b) VALUES ( 11, 'b');
INSERT INTO test (a, b) VALUES ( 12, 'c');
SELECT * FROM test;


// SELECT 모음집
SELECT Name, Continent, Population FROM Country
    WHERE Population < 100000 OR Population IS NULL ORDER BY Population DESC;

SELECT Continent FROM Country;

DROP TABLE IF EXISTS test;
CREATE TABLE test (a int, b int);
INSERT INTO test VALUES (1, 1);
INSERT INTO test VALUES (2, 1);
INSERT INTO test VALUES (3, 1);
INSERT INTO test VALUES (4, 2);
INSERT INTO test VALUES (2, 2);
INSERT INTO test VALUES (1, 2);
SELECT * FROM test;

SELECT Name FROM Country;
SELECT Name FROM Country ORDER BY Name;
SELECT Name FROM Country ORDER BY Name DESC;
SELECT Name FROM Country ORDER BY Name ASC;
SELECT Name, Continent FROM Country ORDER BY Continent, Name;
SELECT Name, Continent, Region FROM Country ORDER BY Continent DESC, Region, Name;

//// 테스트 
DROP TABLE IF EXISTS booltest;
CREATE TABLE booltest (a INTEGER, b INTEGER);
INSERT INTO booltest VALUES (1, 0);
SELECT * FROM booltest;


// < 5 또는 > 3 이런 식으로 범위를 주고 싶을 때 사용 함.. If Else문과 똑같음 
SELECT 
    CASE WHEN a < 5 THEN 'true' ELSE 'false' END as boolA,
    CASE WHEN b THEN 'true' ELSE 'false' END as boolB
    FROM booltest
;

// 하나만 특정해서 고를 때 사용하는 것 IF ELSE문과 똑같지만 하나의 값이 맞는지 확인할 때 사용 
SELECT 
    CASE a WHEN "1" THEN 'true' ELSE 'false' END as boolA,
    CASE b WHEN 1 THEN 'true' ELSE 'false' END as boolB
    FROM booltest
;

// Sale 테이블을 S라 칭하고, S테이블에서 date, price값을 가져오고, Item 테이블을 I라 칭해서 description과 name을 가져와서 
// ID 값이 같은 것들을 묶어서 출력한다. 
SELECT s.id AS sale, s.date, i.name, i.description, s.price
    FROM sale AS s
    JOIN item AS i ON s.item_id = i.id
    ;

//Mulitple로 나눌 때 쓴다
SELECT c.name AS Cust, c.zip, i.name AS Item, i.description, s.quantity AS Quan, s.price
    FROM customer AS c
    LEFT JOIN sale AS s ON s.customer_id = c.id
    LEFT JOIN item AS i ON s.item_id = i.id
    ORDER BY CUST, ITEM
;
   
SELECT Name, LENGTH(Name) As Len FROM City ORDER BY Len ASC, Name;

SELECT SUBSTR('1 this string', 6);

// released에 있는 것을 쪼개서 파싱할 때 쓴다
SELECT released, 
    SUBSTR(released, 1, 4) AS Year, 
    SUBSTR(released, 6, 2) AS Month, 
    SUBSTR(released, 9, 2) AS Day
    FROM album ORDER BY released
    ;