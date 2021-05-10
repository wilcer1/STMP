"""Database connection and quieries."""

from account import Account
import mysql.connector
from mysql.connector import Error
from datetime import datetime

current_date = datetime.today().strftime("%Y-%m-%d")
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


def not_new_customer(email):
    sql = "UPDATE account SET new_customer = 'N' WHERE email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    connection.commit()


def get_income(email):
    """Return income."""
    sql = (
        "SELECT income FROM budget WHERE account_email = %s;"
    )
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()[0]

    if myresult is not None:
        return myresult
    else:
        return 0


def set_variable_expenses(email, var_exp):
    """Set variable_expenses."""
    val = []
    val.append(email)
    for x in var_exp:
        val.append(var_exp[x])

    sql = "INSERT INTO variable_expenses VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

    mycursor.execute(sql, tuple(val))
    connection.commit()

def update_variable_expenses(email, var_exp):
    """update variable_expenses."""
    val = []
    for x in var_exp:
        val.append(var_exp[x])
    val.append(email)
    sql = "UPDATE variable_expenses SET food = %s, bills = %s, transportation = %s, hygien = %s, clothes = %s, enternainment = %s, others = %s WHERE budget_account_email = %s;"
    for x in val:
        print(x)
    mycursor.execute(sql, tuple(val))
    connection.commit()
def get_variable_expenses(email):
    """Return variable_expenses."""
    sql = "SELECT * FROM variable_expenses WHERE budget_account_email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    if myresult is not None:
        food = myresult[1]
        bills = myresult[2]
        transportation = myresult[3]
        hygien = myresult[4]
        clothes = myresult[5]
        entertainment = myresult[6]
        others = myresult[7]

        variable_expenses = {
            "food": food,
            "bills": bills,
            "transportation": transportation,
            "hygien": hygien,
            "clothes": clothes,
            "entertainment": entertainment,
            "others": others,
        }

        return variable_expenses


def set_fixed_expenses(email, var_exp):
    """Set fixed_expenses."""
    val = []
    val.append(email)
    for x in var_exp:
        val.append(var_exp[x])

    sql = "INSERT INTO fixed_expenses VALUES (%s, %s, %s, %s, %s);"

    mycursor.execute(sql, tuple(val))
    connection.commit()


def get_fixed_expenses(email):
    """Return fixed_expenses."""
    sql = "SELECT * FROM fixed_expenses WHERE budget_account_email = %s;"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    if myresult is not None:
        rent = myresult[1]
        subscription = myresult[2]
        insurance = myresult[3]
        others = myresult[4]

        fixed_expenses = {
            "rent": rent,
            "subscription": subscription,
            "insurance": insurance,
            "others": others,
        }

        return fixed_expenses


def get_basic_info(email):
    """Get account info from DB."""
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
            customer.set_customer(get_basic_info(email))
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

    if not check_email(email):
        register = False

    if register is not False:
        sql = "INSERT INTO account VALUES (%s, %s, %s, %s, %s);"
        mycursor.execute(sql, val)
        connection.commit()
        sql = "INSERT INTO budget VALUES (%s, %s, %s, %s, %s);"
        val = (email, 0, 0, current_date, 0)
        mycursor.execute(sql, val)
        connection.commit()

    return register


def log_out():
    sql = "INSERT INTO account VALUES (%s, %s, %s, %s);"



def check_email(email):
    """Validate email format."""
    import re

    # Make a regular expression
    # for validating an Email
    regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"

    if re.search(regex, email):
        return True

    else:
        return False


def new_customer(email):
    """Check if customer is new."""
    sql = "select new_customer from account where email = %s"
    val = (email,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()[0]
    if myresult == "Y":
        return True
    else:
        return False


if __name__ == "__main__":

    disconnect()
