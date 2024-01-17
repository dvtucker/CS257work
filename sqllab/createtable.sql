DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime time with time zone,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  magType text,
  rms real,
  id text,
  place text,
  quaketype text,
  quakestatus text,
);