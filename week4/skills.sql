-- Note: Please consult the directions for this assignment 
-- for the most explanatory version of each question.

-- 1. Select all columns for all brands in the Brands table.
select * from Brands

-- 2. Select all columns for all car models made by Pontiac in the Models table.
select * from Models where brand_name='Pontiac';

-- 3. Select the brand name and model 
--    name for all models made in 1964 from the Models table.
select brand_name, name from Models where year='1964';

-- 4. Select the model name, brand name, and headquarters for the Ford Mustang 
--    from the Models and Brands tables.
select Models.name, 
       Models.brand_name, 
       Brands.headquarters 
from   Models JOIN Brands ON (Models.brand_name=Brands.name) 
where Models.brand_name="Ford"
and Models.name='Mustang';

-- 5. Select all rows for the three oldest brands 
--    from the Brands table (Hint: you can use LIMIT and ORDER BY).
select * from Brands order by founded LIMIT 3;

-- 6. Count the Ford models in the database (output should be a number).
select count(*) from Models where brand_name="Ford";

-- 7. Select the name of any and all car brands that are not discontinued.
select name from Brands where discontinued is NULL;

-- 8. Select rows 15-25 of the DB in alphabetical order by model name.
select * from Models order by name limit 25 offset 15;

-- 9. Select the brand, name, and year the model's brand was 
--    founded for all of the models from 1960. Include row(s)
--    for model(s) even if its brand is not in the Brands table.
--    (The year the brand was founded should be NULL if 
--    the brand is not in the Brands table.)
select Models.brand_name,
       Models.name, 
       Brands.founded 
from Models LEFT JOIN Brands ON (Models.brand_name = Brands.name)
where Models.year = '1960';


-- Part 2: Change the following queries according to the specifications. 
-- Include the answers to the follow up questions in a comment below your
-- query.

-- 1. Modify this query so it shows all brands that are not discontinued
-- regardless of whether they have any models in the models table.
-- before:
    -- SELECT b.name,
    --        b.founded,
    --        m.name
    -- FROM Model AS m
    --   LEFT JOIN brands AS b
    --     ON b.name = m.brand_name
    -- WHERE b.discontinued IS NULL;
    select b.name,
           b.founded,
           m.name
    FROM Brands as b LEFT JOIN Models as m
    ON m.brand_name=b.name
    where b.discontinued is NULL;

/* ANSWER:   
 Ford|1903|E-Series
 Ford|1903|Galaxie
 Ford|1903|Model T
 Ford|1903|Mustang
 Ford|1903|Thunderbird
 Ford|1903|Thunderbird
 Chrysler|1925|Imperial
 Citroën|1919|2CV
 Chevrolet|1911|Corvair
 Chevrolet|1911|Corvair 500
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Chevrolet|1911|Corvette
 Cadillac|1902|Fleetwood
 BMW|1916|600
 BMW|1916|600
 BMW|1916|600
 Buick|1903|Special
 Tesla|2003|*/


-- 2. Modify this left join so it only selects models that have brands in the Brands table.
-- before: 
    -- SELECT m.name,
    --        m.brand_name,
    --        b.founded
    -- FROM Models AS m
    --   LEFT JOIN Brands AS b
    --     ON b.name = m.brand_name;
    SELECT m.name,
           m.brand_name,
           b.founded
    FROM Models AS m 
    JOIN Brands AS b 
    ON b.name = m.brand_name;

-- ANSWER:
-- Model T|Ford|1903
-- Imperial|Chrysler|1925
-- 2CV|Citroën|1919
-- Minx Magnificent|Hillman|1907
-- Corvette|Chevrolet|1911
-- Corvette|Chevrolet|1911
-- Fleetwood|Cadillac|1902
-- Corvette|Chevrolet|1911
-- Thunderbird|Ford|1903
-- Corvette|Chevrolet|1911
-- Corvette|Chevrolet|1911
-- 600|BMW|1916
-- Corvette|Chevrolet|1911
-- 600|BMW|1916
-- Thunderbird|Ford|1903
-- Mini|Austin|1905
-- Corvette|Chevrolet|1911
-- 600|BMW|1916
-- Corvair|Chevrolet|1911
-- Corvette|Chevrolet|1911
-- Rockette|Fairthorpe|1954
-- Mini Cooper|Austin|1905
-- Avanti|Studebaker|1852
-- Tempest|Pontiac|1926
-- Corvette|Chevrolet|1911
-- Grand Prix|Pontiac|1926
-- Corvette|Chevrolet|1911
-- Avanti|Studebaker|1852
-- Special|Buick|1903
-- Mini|Austin|1905
-- Mini Cooper S|Austin|1905
-- Classic|Rambler|1901
-- E-Series|Ford|1903
-- Avanti|Studebaker|1852
-- Grand Prix|Pontiac|1926
-- Corvair 500|Chevrolet|1911
-- Corvette|Chevrolet|1911
-- Corvette|Chevrolet|1911
-- Mustang|Ford|1903
-- Galaxie|Ford|1903
-- GTO|Pontiac|1926
-- LeMans|Pontiac|1926
-- Bonneville|Pontiac|1926
-- Grand Prix|Pontiac|1926
-- Fury|Plymouth|1928
-- Avanti|Studebaker|1852
-- Mini Cooper|Austin|1905


-- followup question: In your own words, describe the difference between 
-- left joins and inner joins.
The INNER joins queries return all and only the rows where the join condition is met
in BOTH tables. 
The LEFT joins queries return all the rows of the left table and only the rows
from the right table that meet the condition.

-- 3. Modify the query so that it only selects brands that don't have any models in the models table. 
-- (Hint: it should only show Tesla's row.)
-- before: 
    -- SELECT name,
    --        founded
    -- FROM Brands
    --   LEFT JOIN Models
    --     ON brands.name = Models.brand_name
    -- WHERE Models.year > 1940;
    SELECT Brands.name, 
           Brands.founded
    FROM   Brands 
    LEFT JOIN Models 
    ON Brands.name = Models.brand_name 
    WHERE Brands.founded >= 2003;
   
-- ANSWER:
-- Tesla|2003

-- 4. Modify the query to add another column to the results to show 
-- the number of years from the year of the model until the brand becomes discontinued
-- Display this column with the name years_until_brand_discontinued.
-- before: 
    -- SELECT b.name,
    --        m.name,
    --        m.year,
    --        b.discontinued
    -- FROM Models AS m
    --   LEFT JOIN brands AS b
    --     ON m.brand_name = b.name
    -- WHERE b.discontinued NOT NULL;
    select b.name,
           m.name,
           m.year,
           b.discontinued,
           (b.discontinued-m.year) AS year_until_the_brand_discontinued
    FROM Models AS m 
    LEFT JOIN Brands AS b 
    ON m.brand_name = b.name 
    WHERE b.discontinued NOT NULL;

-- ANSWERS:
-- Hillman|Minx Magnificent|1950|1981|31
-- Austin|Mini|1959|1987|28
-- Fairthorpe|Rockette|1960|1976|16
-- Austin|Mini Cooper|1961|1987|26
-- Studebaker|Avanti|1961|1967|6
-- Pontiac|Tempest|1961|2010|49
-- Pontiac|Grand Prix|1962|2010|48
-- Studebaker|Avanti|1962|1967|5
-- Austin|Mini|1963|1987|24
-- Austin|Mini Cooper S|1963|1987|24
-- Rambler|Classic|1963|1969|6
-- Studebaker|Avanti|1963|1967|4
-- Pontiac|Grand Prix|1963|2010|47
-- Pontiac|GTO|1964|2010|46
-- Pontiac|LeMans|1964|2010|46
-- Pontiac|Bonneville|1964|2010|46
-- Pontiac|Grand Prix|1964|2010|46
-- Plymouth|Fury|1964|2001|37
-- Studebaker|Avanti|1964|1967|3
-- Austin|Mini Cooper|1964|1987|23



-- Part 3: Further Study

-- 1. Select the name of any brand with more than 5 models in the database.
SELECT b.name 
FROM Brands AS b 
JOIN Models AS m 
ON b.name = m.brand_name 
GROUP BY m.name 
HAVING count(m.name)>5;

-- ANSWER:
-- Chevrolet

-- 2. Add the following rows to the Models table.

-- year    name       brand_name
-- ----    ----       ----------
-- 2015    Chevrolet  Malibu
-- 2015    Subaru     Outback
INSERT into Models (year, name, brand_name) VALUES (2015, 'Chevrolet', 'Malibu');
INSERT into Models (year, name, brand_name) VALUES (2015, 'Subaru', 'Outback');


-- 3. Write a SQL statement to create a table called `Awards`
--    with columns `name`, `year`, and `winner`. Choose
--    an appropriate datatype and nullability for each column
--   (no need to do subqueries here).
CREATE TABLE Awards 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 name VARCHAR(50) NOT NULL,
 year INT NOT NULL,
 winner VARCHAR(50));

-- 4. Write a SQL statement that adds the following rows to the Awards table:

--   name                 year      winner_model_id
--   ----                 ----      ---------------
--   IIHS Safety Award    2015      the id for the 2015 Chevrolet Malibu
--   IIHS Safety Award    2015      the id for the 2015 Subaru Outback

INSERT INTO Awards (name, year, winner) VALUES ('IIHS Safety Award',2015,'the id for the 2015 Chevrolet Malibu');
INSERT INTO Awards (name, year, winner) VALUES ('IIHS Safety Award',2015,'the id for the 2015 Subaru Outback');

-- 5. Using a subquery, select only the *name* of any model whose 
-- year is the same year that *any* brand was founded.
select name from Models where year in (select founded from brands);

-- ANSWER:
-- Imperial
-- Corvette
-- Fleetwood





