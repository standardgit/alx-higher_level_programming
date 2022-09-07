-- Creating full database table
-- Adding multiple rows
CREATE TABLE IF NOT EXISTS second_table (
	id (int),
	name (varcharr(256))
	score (int),); ENGINE = INNODB
INSERT INTO second_table (id, name, score) VALUES(
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8));
