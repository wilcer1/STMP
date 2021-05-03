"""Database connection and quieries."""

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
    """Disconnect from database."""
    try:
        if connection is not None and connection.is_connected():
            mycursor.close()
            connection.close()
            print("Disconnected")
    except Error as e:
        print("Failed to disconnect")
        print(e)


# def show_account():
#     print("Show Columns in account")
#     mycursor.execute("show columns from account;")
#     myresult = mycursor.fetchall()

#     for x in myresult:
#         print(x)


def get_first_name(email):
    """Return first_name."""
    sql = "SELECT password FROM account WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()[0]

    return myresult


def get_last_name(email):
    """Return last_name."""
    sql = "SELECT password FROM account WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()[0]

    return myresult


def get_income(email):
    """Return income."""
    sql = "SELECT password FROM account WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()[0]

    return myresult


def get_expenses(email):
    """Return expenses."""
    sql = "SELECT password FROM account WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()[0]

    return myresult


def verify_login(email, password):
    """verify_login."""
    sql = "SELECT password FROM account WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    try:
        myresult = mycursor.fetchone()[0]
    except(TypeError):
        myresult = None
    finally:
        if password != myresult or myresult == None:
            return False
        else:
            customer = Account()
            customer = customer.setCustomer()
            return True

    


def register_account(email, first_name, last_name, password, income, expenses):
    """Add new account to database."""
    sql = "INSERT INTO account VALUES (%s, %s, %s, %s, %s, %s);"
    val = (email, first_name, last_name, password, income, expenses)
    mycursor.execute(sql, val)
    connection.commit()
