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