SELECT * FROM myschema.mmr_clean;

#ALTER TABLE myschema.mmr_clean DROP COLUMN MyUnknownColumn;

ALTER TABLE myschema.mmr_clean ADD COLUMN Testing VARCHAR(255);

SELECT * FROM myschema.mmr_clean;

