-- Active: 1670612804657@@localhost@3306@myschema
SELECT * FROM myschema.mmr_clean;

ALTER TABLE myschema.mmr_clean DROP COLUMN Testing;

ALTER TABLE myschema.mmr_clean ADD COLUMN Testing VARCHAR(255);

SELECT * FROM myschema.mmr_clean ORDER BY Date DESC;

INSERT INTO mmr_clean (Date) VALUES ('2022-12-23'); 

DELETE from mmr_clean WHERE `Date` = '2022-12-23';

ALTER TABLE `myschema`.`mmr_clean` 
CHANGE COLUMN `Max.Pace` `MaxPace` DOUBLE NULL DEFAULT NULL ;

ALTER TABLE mmr_clean CHANGE COLUMN `Avg.Spd` `AvgSpd` DOUBLE NULL DEFAULT NULL; 

INSERT INTO myschema.mmr_clean (Date, Activity, Duration, Distance, AvgPace, MaxPace, AvgSpd, `Cal.Burned`, `Avg.HR`, Steps, mileage, minutes, year) 
VALUES ('2022-12-23', 'Run', '1750', '3.1', '9.4', '0', '6.3', '410', '146', '4861', 'FiveK', '1750', '2022');    

SELECT * FROM myschema.mmr_clean WHERE `Date` = '2022-12-23';

SHOW TABLES;

SHOW COLUMNS FROM myschema.mmr_clean;

SELECT * FROM myschema.mmr_clean WHERE `Date` = '2022-12-23';

SELECT * FROM uwh;

UPDATE myschema.uwh SET `Avg Heart Rate` = 142 WHERE `Avg Heart Rate` = '';

ALTER TABLE myschema.uwh MODIFY `Avg Heart Rate` INTEGER;






