import pymssql
import json

server = "data.hacktechvalley.com:1433"
username = "ReadOnly"
password = "ReadOnly"
database = "GPSDATA"

connection = pymssql.connect(server, username, password, database)
cursor = connection.cursor()

#def getAllVehicles():
#    cursor.execute(
#        """
#        SELECT * FROM Vehicle;
#        """
#    )    
#    data = cursor.fetchall()
#    print(data)
#    print()
#    return json.dumps(data)

def timePerTruckPerDay():
    cursor.execute(
        """
        SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime))))), VehicleID 
        FROM VehicleEvent 
        GROUP BY VehicleID,DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);
        """
    )

    data = cursor.fetchall()
    return json.dumps(data)

def timePerDay():
    cursor.execute(
        """
        SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime)))))
        FROM VehicleEvent 
        GROUP BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);
        """
    )

    data = cursor.fetchall()
    return json.dumps(data)

def getRecentLocations():
    cursor.execute(
        """
        SELECT VehicleID,Latitude,Longitude,StartTime,Heading,EventTypeID,Location 
        FROM VehicleEvent 
        WHERE DAY(StartTime)=DAY(CURRENT_TIMESTAMP) AND MONTH(StartTime)=MONTH(CURRENT_TIMESTAMP) AND YEAR(StartTime)=YEAR(CURRENT_TIMESTAMP)
        ORDER BY StartTime;
        """
    )

    data = cursor.fetchall()
    return json.dumps(data)

def main():
    print(getAllVehicles())
    print("\n")
    print(timePerTruckPerDay())
    print("\n")
    print(timePerDay())
    print("\n")
    print(getRecentLocations())

if (__name__ == "__main__"):
    main()
