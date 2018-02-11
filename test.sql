USE GPSDATA;

/*
SELECT * FROM EventType;
SELECT * FROM Vehicle;
SELECT * FROM VehicleEvent;
*/

/*---time per truck, per day---*/
SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,VehicleEvent.StartTime))-MIN(CONVERT(float,VehicleEvent.StartTime))))),
CONVERT(varchar,MIN(VehicleEvent.StartTime)),Vehicle.DisplayName
FROM VehicleEvent 
INNER JOIN Vehicle ON VehicleEvent.VehicleID=Vehicle.VehicleID
GROUP BY Vehicle.DisplayName,DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime)
ORDER BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime),CONVERT(int,Vehicle.DisplayName);

/*---time per truck---*/
SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,VehicleEvent.StartTime))-MIN(CONVERT(float,VehicleEvent.StartTime))))),Vehicle.DisplayName 
FROM VehicleEvent 
INNER JOIN Vehicle ON VehicleEvent.VehicleID=Vehicle.VehicleID
GROUP BY Vehicle.DisplayName
ORDER BY CONVERT(int,Vehicle.DisplayName);

/*---time per day---*/
SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime))))),CONVERT(varchar,MIN(StartTime))
FROM VehicleEvent 
GROUP BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime)
ORDER BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);

/*---all events from today---*/
SELECT Vehicle.DisplayName,Latitude,Longitude,CONVERT(varchar,VehicleEvent.StartTime),Heading,EventTypeID,Location 
FROM VehicleEvent 
INNER JOIN Vehicle ON VehicleEvent.VehicleID=Vehicle.VehicleID
WHERE DAY(VehicleEvent.StartTime)=DAY(CURRENT_TIMESTAMP) AND MONTH(VehicleEvent.StartTime)=MONTH(CURRENT_TIMESTAMP) AND YEAR(VehicleEvent.StartTime)=YEAR(CURRENT_TIMESTAMP)
ORDER BY VehicleEvent.StartTime;

/*---current time---*/
SELECT CURRENT_TIMESTAMP;