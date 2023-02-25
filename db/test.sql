--inner join
--войдут только записи, которые присутствуют в обоих таблицах
SELECT * FROM customers INNER JOIN cities on customers.city_id = cities.id;

-- full outer join
--войдут все записи из обоих таблиц
SELECT * FROM customers FULL OUTER JOIN cities on customers.city_id = cities.id;

-- left join
--объединение по таблице заказчики
SELECT * FROM customers LEFT JOIN cities on customers.city_id = cities.id;

-- right join
-- объединение по таблице города
SELECT * FROM customers RIGHT JOIN cities on customers.city_id = cities.id;

