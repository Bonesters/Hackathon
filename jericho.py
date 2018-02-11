import pymssql
import json

server = "data.hacktechvalley.com:1433"
username = "ReadOnly"
password = "ReadOnly"
database = "GPSDATA"

connection = pymssql.connect(server, username, password, database)
cursor = connection.cursor()

def getAllVehicles():
    cursor.execute(
        """
        SELECT * FROM Vehicle;
        """
    )
    
    data = cursor.fetchall()
    print(data)
    print()
    return json.dumps(data)

def timePerTruckPerDay():
    cursor.execute("""
        SELECT CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime)))), VehicleID 
        FROM VehicleEvent 
        GROUP BY VehicleID,DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);        
        """)

    data = cursor.fetchall()
    print(data)
    print()
    return json.dumps(data)

def timePerDay():
    cursor.execute("""
        SELECT CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime)))) 
        FROM VehicleEvent 
        GROUP BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);
        """)

    data = cursor.fetchall()
    print(data)
    print()
    return json.dumps(data)

def getRecentLocations():
    cursor.execute(
        """
        SELECT VehicleID,Latitude,Longitude,StartTime,Heading,EventTypeID,Location FROM VehicleEvent ORDER BY VehicleID, StartTime DESC;
        """
    )

    data = cursor.fetchall()
    print(data)
    print()
    return json.dumps(data)

def main():
    getAllVehicles()
    print("\n")
    timePerTruckPerDay()
    print("\n")
    timePerDay()
    print("\n")
    getRecentLocations()

if (__name__ == "__main__"):
    main()