CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
) ;

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Myleene', 18);
INSERT INTO Ages (name, age) VALUES ('Jocelyn', 14);
INSERT INTO Ages (name, age) VALUES ('Eubh', 26);
INSERT INTO Ages (name, age) VALUES ('Virginia', 16);

SELECT hex(name || age) AS X FROM Ages ORDER BY X;
-- Output: 457562683236