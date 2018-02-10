USE GPSDATA;

SELECT * FROM EventType;
SELECT * FROM Vehicle;
SELECT * FROM VehicleEvent;

/*---time per truck, per day---*/
SELECT CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime)))), VehicleID 
FROM VehicleEvent 
GROUP BY VehicleID,DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);

/*---time per truck---*/
SELECT CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime)))), VehicleID 
FROM VehicleEvent 
GROUP BY VehicleID;

/*---time per day---*/
SELECT CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime)))) 
FROM VehicleEvent 
GROUP BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);

/*---most recent events from vehicle---*/
SELECT VehicleID,Latitude,Longitude,StartTime,Heading,EventTypeID,Location FROM VehicleEvent WHERE StartTime>/*INSERT LAST TIME HERE*/ ORDER BY StartTime;

/*---current time---*/
SELECT CURRENT_TIMESTAMP;