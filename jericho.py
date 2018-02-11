import pymssql
import json

server = "data.hacktechvalley.com:1433"
username = "ReadOnly"
password = "ReadOnly"
database = "GPSDATA"

connection = pymssql.connect(server, username, password, database)
cursor = connection.cursor()

def timePerTruckPerDay():
    cursor.execute(
        """
        SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,VehicleEvent.StartTime))-MIN(CONVERT(float,VehicleEvent.StartTime))))),
        CONVERT(varchar,MIN(VehicleEvent.StartTime)),Vehicle.DisplayName
        FROM VehicleEvent 
        INNER JOIN Vehicle ON VehicleEvent.VehicleID=Vehicle.VehicleID
        GROUP BY Vehicle.DisplayName,DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime)
        ORDER BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime),CONVERT(int,Vehicle.DisplayName);
        """
    )

    data = cursor.fetchall()

    newData = list(data)

    for x in range(0,11):
        newData[x] = list(data[x])
        newData[x][0] = list(data[x][0])
        temp = str(data[x][0])[13:-2]
        newData[x][0] = temp

        newData[x][1] = list(data[x][1])
        temp = str(data[x][1])[0:-8]
        newData[x][1] = temp

    jsonMemes = json.dumps(newData)
    print(jsonMemes)
    return jsonMemes

def timePerTruck():
    cursor.execute(
        """
        SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,VehicleEvent.StartTime))-MIN(CONVERT(float,VehicleEvent.StartTime))))),Vehicle.DisplayName 
        FROM VehicleEvent 
        INNER JOIN Vehicle ON VehicleEvent.VehicleID=Vehicle.VehicleID
        GROUP BY Vehicle.DisplayName
        ORDER BY CONVERT(int,Vehicle.DisplayName);
        """
    )

    data = cursor.fetchall()
    #print(data[0])
    #print(data[1])
    #print(data[2])
    #print(data[3])
    #print(data[4])
    #print(data[5])
    #print(data[6])
    #print(data[7])
    #print(data[8])
    #print(data[9])
    #print(data[10])
    #print(data[11])
    #print(data[12])
    return json.dumps(data)

def timePerDay():
    cursor.execute(
        """
        SELECT CONVERT(varchar,CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime))))),CONVERT(varchar,MIN(StartTime))
        FROM VehicleEvent 
        GROUP BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime)
        ORDER BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);
        """
    )

    data = cursor.fetchall()
    #print(data[0])
    return json.dumps(data)

#Returns nothing
def getRecentLocations():
    cursor.execute(
        """
        SELECT Vehicle.DisplayName,Latitude,Longitude,CONVERT(varchar,VehicleEvent.StartTime),Heading,EventTypeID,Location 
        FROM VehicleEvent 
        INNER JOIN Vehicle ON VehicleEvent.VehicleID=Vehicle.VehicleID
        WHERE DAY(VehicleEvent.StartTime)=DAY(CURRENT_TIMESTAMP) AND MONTH(VehicleEvent.StartTime)=MONTH(CURRENT_TIMESTAMP) AND YEAR(VehicleEvent.StartTime)=YEAR(CURRENT_TIMESTAMP)
        ORDER BY VehicleEvent.StartTime;
        """
    )

    data = cursor.fetchall()
    dlen = len(data)
    print(dlen)
    return json.dumps(data)

def main():
    timePerTruckPerDay()
    print("\n")
    #timePerDay()
    #print("\n")
    #timePerTruck()
    #print("\n")
    #getRecentLocations()
    #print("\n")

if (__name__ == "__main__"):
    main()
