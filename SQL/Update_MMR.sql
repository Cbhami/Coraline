SELECT * FROM myschema.mmr_clean WHERE `Date` = '2022-12-23';

SELECT * FROM myschema.mmr_clean ORDER BY `Date` DESC;

UPDATE mmr_clean
SET `minutes` = '30.20' 
WHERE `Date` = '2022-12-23'; 