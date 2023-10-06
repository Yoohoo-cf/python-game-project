import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="airports",
    user="dbuser",
    password="707708",
    autocommit=True
)

def getairportsbycity(city_name):
    sql = "SELECT ID, cityname, countryname,  airport FROM locations"
    sql += " WHERE cityname='" + city_name + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Hello, you are flying to  {row[1]} in {row[2]} to collect the diamond in {row[3]}.")
    return


def storeplayerscores(player_name, score):
    sql = "INSERT INTO scores(playername, score) VALUES(%s, %s)"
    val = (player_name, score)
    cursor = connection.cursor()
    cursor.execute(sql, val)
    print(f"Player: {player_name}, Score: {score}")
    return

def allplayerscores():
    sql = "SELECT playername, score FROM scores"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()

    print("\nAll Players Scores: ")
    for result in results:
        print(f"Player: {result[0]}, Score: {result[1]}")