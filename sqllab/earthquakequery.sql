--Show all earthquakes with a depth greater than 100
SELECT * FROM earthquakes WHERE quakedepth>100;

--Show all earthquakes that have a status of reviewed
SELECT * FROM earthquakes WHERE quakestatus = 'reviewed';

--Show all earthquakes that have been reviewed and have a 
--magnitude greater than 5
SELECT * FROM earthquakes WHERE quakestatus = 'reviewed' AND mag>5;