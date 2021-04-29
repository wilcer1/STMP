import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(
        host="den1.mysql5.gear.host",
        user="stmp",
        password="Zq65rS9Q?x!D",
        database="stmp",
    )
    mycursor = connection.cursor()
    if connection.is_connected():
        print("Connected")

except Error as e:
    print(e)


def disconnect():
    try:
        if connection.is_connected():
            mycursor.close()
            connection.close()
            print("Disconnected")
    except Error as e:
        print("Failed to disconnect")
        print(e)


def showTables():
    print("Show Tables")
    mycursor.execute("SELECT customer_id FROM customer;")
    myresult = mycursor.fetchall()

    print(myresult)

    for x in myresult:
        print(x)
