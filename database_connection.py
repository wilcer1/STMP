import mysql.connector
from mysql.connector import Error

connection = None

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
        if connection is not None and connection.is_connected():
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


def get_first_name(email):
    """Gets first name from database"""

    mycursor.execute("SELECT first_name FROM account WHERE email ='" + email + "';")
    myresult = mycursor.fetchone()

    return myresult


def get_last_name(email):

    mycursor.execute("SELECT last_name FROM account WHERE email ='" + email + "';")
    myresult = mycursor.fetchone()

    return myresult


def get_income(email):

    mycursor.execute("SELECT income FROM account WHERE email ='" + email + "';")
    myresult = mycursor.fetchone()

    return myresult


def get_expenses(email):

    mycursor.execute("SELECT expenses FROM account WHERE email ='" + email + "';")
    myresult = mycursor.fetchone()

    return myresult


def verify_login(email, password):

    mycursor.execute("SELECT password FROM account WHERE email ='" + email + "';")
    myresult = mycursor.fetchone()

    if password == myresult:
        return True
    else:
        return False