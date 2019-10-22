SELECT name, population, area
FROM World as w
WHERE area > 3000000 OR population > 25000000;

COMMIT;

-- Runtime: 217 ms (faster than 85% of online submissions)
-- Memory Usage: 0MB (less than 100% of online Go submissions)