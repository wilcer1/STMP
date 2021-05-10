"""Database connection and quieries."""

from account import Account
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


def get_first_name(email):
    """Return first_name."""
    sql = "SELECT first_name FROM account WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()[0]

    return myresult


def get_last_name(email):
    """Return last_name."""
    sql = "SELECT last_name FROM account WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()[0]

    return myresult


def get_income(email):
    """Return income."""
    sql = "SELECT income.name, income.value From income Right join account ON budget_budget_id = account.email WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()[0]

    return myresult


def get_expenses(email):
    """Return expenses."""
    sql = "SELECT expenses FROM account WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()[0]

    return myresult


def get_all_info(email):
    """Return all info."""
    sql = "SELECT * FROM fixed_expenses, variable_expenses INNER JOIN account ON budget_budget_id = account.email WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    return myresult

def get_basic_info(email):
    sql = "SELECT * FROM account WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    return myresult


def verify_login(email, password):
    """verify_login."""
    sql = "SELECT password FROM account WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    try:
        myresult = mycursor.fetchone()[0]
    except (TypeError):
        myresult = None
    finally:
        if password != myresult or myresult is None:
            return False
        else:
            customer = Account.getInstance()
            customer.setCustomer(getBasicInfo(email))
            return True


def register_account(val):
    """Add new account to database."""
    # check if email is unique, return true if it is and create the acc.
    # Otherwise return false
    sql = "SELECT email FROM account;"
    email = val[0]
    mycursor.execute(sql)
    res = mycursor.fetchall()
    register = True
    for x in res:
        for i in x:
            if email == i:
                register = False
                break

    if register is not False:
        sql = "INSERT INTO account VALUES (%s, %s, %s, %s);"
        mycursor.execute(sql, val)
        connection.commit()
    return register

def log_out():
    sql = "INSERT INTO account VALUES (%s, %s, %s, %s);"

def check_email(email):
    import re
    # Make a regular expression
    # for validating an Email
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    if(re.search(regex, email)):
        return True
 
    else:
        return False

if __name__ == "__main__":
    getBasicInfo("s")