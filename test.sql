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
SELECT CONVERT(varchar,CONVERT(datetime,AVG(subquery1.maxT-subquery1.minT))),Vehicle.DisplayName  FROM VehicleEvent,(
    SELECT MAX(CONVERT(float,VehicleEvent.StartTime)) AS maxT,MIN(CONVERT(float,VehicleEvent.StartTime)) AS minT, VehicleEvent.VehicleID AS ID
    FROM VehicleEvent
    GROUP BY VehicleEvent.VehicleID,DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime)
)subquery1
INNER JOIN Vehicle ON subquery1.ID=Vehicle.VehicleID
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

/*---time per truck, per day, in range---*/
SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,VehicleEvent.StartTime))-MIN(CONVERT(float,VehicleEvent.StartTime))))),
CONVERT(varchar,MIN(VehicleEvent.StartTime)),Vehicle.DisplayName
FROM VehicleEvent 
INNER JOIN Vehicle ON VehicleEvent.VehicleID=Vehicle.VehicleID
WHERE StartTime BETWEEN CONVERT(datetime,'mm/dd/yyyy',101) AND DATEADD(day,1,CONVERT(datetime,'mm/dd/yyyy',101))
GROUP BY Vehicle.DisplayName,DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime)
ORDER BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime),CONVERT(int,Vehicle.DisplayName);

/*---time for a truck, per day, in range---*/
SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,VehicleEvent.StartTime))-MIN(CONVERT(float,VehicleEvent.StartTime))))),
CONVERT(varchar,MIN(VehicleEvent.StartTime)),Vehicle.DisplayName
FROM VehicleEvent 
INNER JOIN Vehicle ON VehicleEvent.VehicleID=Vehicle.VehicleID
WHERE (StartTime BETWEEN CONVERT(datetime,'mm/dd/yyyy',101) AND DATEADD(day,1,CONVERT(datetime,'mm/dd/yyyy',101))) AND (DisplayName='##')
GROUP BY Vehicle.DisplayName,DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime)
ORDER BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime),CONVERT(int,Vehicle.DisplayName);

/*---time per day in range---*/
SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime))))),CONVERT(varchar,MIN(StartTime))
FROM VehicleEvent 
WHERE StartTime BETWEEN CONVERT(datetime,'mm/dd/yyyy',101) AND DATEADD(day,1,CONVERT(datetime,'mm/dd/yyyy',101))
GROUP BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime)
ORDER BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);

/*---all events from date range---*/
SELECT Vehicle.DisplayName,Latitude,Longitude,CONVERT(varchar,VehicleEvent.StartTime),Heading,EventTypeID,Location 
FROM VehicleEvent 
INNER JOIN Vehicle ON VehicleEvent.VehicleID=Vehicle.VehicleID
WHERE VehicleEvent.StartTime BETWEEN CONVERT(datetime,'mm/dd/yyyy',101) AND DATEADD(day,1,CONVERT(datetime,'mm/dd/yyyy',101))
ORDER BY VehicleEvent.StartTime;

/*---get display names for all trucks---*/
SELECT DisplayName FROM Vehicle
ORDER BY CONVERT(int,DisplayName) ASC;