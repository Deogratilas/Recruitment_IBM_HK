SELECT a.owner_id, o.owner_name, COUNT(DISTINCT c.category_name) as different_category_count
FROM articles a
INNER JOIN owners o ON a.owner_id = o.owner_id
INNER JOIN categories c ON a.category_id = c.category_id
GROUP BY a.owner_id, o.owner_name
ORDER BY different_category_count DESC;
