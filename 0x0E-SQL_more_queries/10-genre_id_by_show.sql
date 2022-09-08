--Using INNER JOIN
-- ORDER by title
SELECT s.`title`, c.`genre_id`
FROM `tv_show_genres` AS c
INNER JOIN `tv_shows` AS s
ON c.`show_id` = s.`id`
ORDER BY s.`title` ASC,  c.`genre_id` ASC;
