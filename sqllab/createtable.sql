DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime time,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  magType text,
  rms real,
  id text,
  place text,
  quaketype text,
  quakestatus text
);