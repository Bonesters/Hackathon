import pymssql
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

    row = cursor.fetchone()
    numCols = len(row)
    #print(numCols)
    while row:
        print("%s, %s, %s, %s, %s" % (row[0], row[1], row[2], row[3], row[4]))
        row = cursor.fetchone()

def timePerTruckPerDay():
    cursor.execute("""
        SELECT CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime)))), VehicleID 
        FROM VehicleEvent 
        GROUP BY VehicleID,DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);        
        """)

    row = cursor.fetchone()
    numCols = len(row)
    #print(numCols)
    while row:
        print("%s, %s" % (row[0], row[1]))
        row = cursor.fetchone()

def timePerDay():
    cursor.execute("""
        SELECT CONVERT(datetime,(MAX(CONVERT(float,StartTime))-MIN(CONVERT(float,StartTime)))) 
        FROM VehicleEvent 
        GROUP BY DATEPART(year,StartTime),DATEPART(month,StartTime),DATEPART(day,StartTime);
        """)

    row = cursor.fetchone()
    if row:
        numCols = len(row)
        #print(numCols)

    while row:
        print("%s" % (row[0]))
        row = cursor.fetchone()

def getRecentLocations():
    cursor.execute(
        """
        SELECT VehicleID,Latitude,Longitude,StartTime,Heading,EventTypeID,Location FROM VehicleEvent ORDER BY VehicleID, StartTime DESC;
        """
    )

    row = cursor.fetchone()
    if row:
        numCols = len(row)
        #print(numCols)

    while row:
        print("%s, %s, %s, %s, %s, %s, %s" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        row = cursor.fetchone()

def main():
    getAllVehicles()
    print("\n")
    timePerTruckPerDay()
    print("\n")
    timePerDay()
    print("\n")
    getRecentLocations()

main()