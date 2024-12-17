import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Rl13082002!",
    database = "mjtilekeeper"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO tile_counter (tile, count) VALUES (%s, %s)"
tileSet1 = [("2m", 2), ("2m", 2)]

mycursor.executemany(sqlFormula, tileSet1)

mydb.commit()