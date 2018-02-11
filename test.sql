USE GPSDATA;

SELECT * FROM EventType;
SELECT * FROM Vehicle;
SELECT * FROM VehicleEvent;

/*---time per truck, per day---*/
SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime))))), VehicleID 
FROM VehicleEvent 
GROUP BY VehicleID,DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);

/*---time per truck---*/
SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime))))), VehicleID 
FROM VehicleEvent 
GROUP BY VehicleID;

/*---time per day---*/
SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime)))))
FROM VehicleEvent 
GROUP BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);

/*---all events from today---*/
SELECT VehicleID,Latitude,Longitude,StartTime,Heading,EventTypeID,Location 
FROM VehicleEvent 
WHERE DAY(StartTime)=DAY(CURRENT_TIMESTAMP) AND MONTH(StartTime)=MONTH(CURRENT_TIMESTAMP) AND YEAR(StartTime)=YEAR(CURRENT_TIMESTAMP)
ORDER BY StartTime;

/*---current time---*/
SELECT CURRENT_TIMESTAMP;