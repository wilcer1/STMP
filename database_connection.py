"""Database connection and quieries."""

from logging import setLogRecordFactory
from account import Account
import mysql.connector
from mysql.connector import Error
from datetime import datetime

current_date = datetime.today().strftime("%Y-%m-%d")


class database_connection():
    def __init__(self):
        
        try:
            self.connection = mysql.connector.connect(
                host="den1.mysql5.gear.host",
                user="stmp",
                password="Zq65rS9Q?x!D",
                database="stmp",
            )
            self.mycursor = self.connection.cursor()
            if self.connection.is_connected():
                print("Connected")


        except Error as e:
            print(e)


    def disconnect(self):
        """Disconnect from database."""
        try:
            if self.connection is not None and self.connection.is_connected():
                self.mycursor.close()
                self.connection.close()
                print("Disconnected")
        except Error as e:
            print("Failed to disconnect")
            print(e)


    def not_new_customer(self, email):
        """Change new_customer to 'N'."""
        sql = "UPDATE account SET new_customer = 'N' WHERE email = %s;"
        val = (email,)
        self.mycursor.execute(sql, val)
        self.connection.commit()


    def get_income(self, email):
        """Return income."""
        sql = "SELECT income FROM budget WHERE account_email = %s;"
        val = (email,)
        self.mycursor.execute(sql, val)
        myresult = self.mycursor.fetchone()[0]

        if myresult is not None:
            return myresult
        else:
            return 0


    def set_variable_expenses(self, email, var_exp):
        """Set variable_expenses."""
        val = []
        val.append(email)
        for x in var_exp:
            val.append(var_exp[x])

        sql = "INSERT INTO variable_expenses \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

        self.mycursor.execute(sql, tuple(val))
        self.connection.commit()


    def update_variable_expenses(self, email, var_exp):
        """Update variable_expenses."""
        val = []
        for x in var_exp:
            val.append(var_exp[x])
        val.append(email)

        sql = "UPDATE variable_expenses SET food = %s, bills = %s, transportation = %s, \
            hygien = %s, clothes = %s, enternainment = %s, others = %s \
            WHERE budget_account_email = %s;"

        self.mycursor.execute(sql, tuple(val))
        self.connection.commit()


    def get_variable_expenses(self, email):
        """Return variable_expenses."""
        sql = "SELECT * FROM variable_expenses WHERE budget_account_email = %s;"
        val = (email,)
        self.mycursor.execute(sql, val)
        myresult = self.mycursor.fetchone()
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


    def set_fixed_expenses(self, email, var_exp):
        """Set fixed_expenses."""
        val = []
        val.append(email)
        for x in var_exp:
            val.append(var_exp[x])

        sql = "INSERT INTO fixed_expenses VALUES (%s, %s, %s, %s, %s);"

        self.mycursor.execute(sql, tuple(val))
        self.connection.commit()

    def update_fixed_expenses(self, email, fix_exp):
        """Update fixed_expenses."""
        val = []
        for x in fix_exp:
            val.append(fix_exp[x])
        val.append(email)

        sql = "UPDATE fixed_expenses SET rent = %s, subscription = %s, insurance = %s, \
            others = %s WHERE budget_account_email = %s;"

        self.mycursor.execute(sql, tuple(val))
        self.connection.commit()


    def get_fixed_expenses(self, email):
        """Return fixed_expenses."""
        sql = "SELECT * FROM fixed_expenses WHERE budget_account_email = %s;"
        val = (email,)
        self.mycursor.execute(sql, val)
        myresult = self.mycursor.fetchone()
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


    def get_basic_info(self, email):
        """Get account info from DB."""
        sql = "SELECT * FROM account WHERE email = %s;"
        val = (email,)
        self.mycursor.execute(sql, val)
        myresult = self.mycursor.fetchone()
        return myresult


    def verify_login(self, email, password):
        """verify_login."""
        if not self.connection.is_connected():
            self.__init__()
        sql = "SELECT password FROM account WHERE email = %s;"
        val = (email,)
        self.mycursor.execute(sql, val)
        try:
            myresult = self.mycursor.fetchone()[0]
        except (TypeError):
            myresult = None
        finally:
            if password != myresult or myresult is None:
                return False
            else:
                customer = Account.getInstance()
                customer.set_customer(self.get_basic_info(email))
                return True


    def register_account(self, val):
        """Add new account to database."""
        # check if email is unique, return true if it is and create the acc.
        # Otherwise return false
        sql = "SELECT email FROM account;"
        email = val[0]
        self.mycursor.execute(sql)
        res = self.mycursor.fetchall()
        register = True
        for x in res:
            for i in x:
                if email == i:
                    register = False
                    break

        if not self.check_email(email) or not self.check_details(email, val[1], val[2]):
            register = False

        if register is not False:
            sql = "INSERT INTO account VALUES (%s, %s, %s, %s, %s);"
            self.mycursor.execute(sql, val)
            self.connection.commit()
            sql = "INSERT INTO budget VALUES (%s, %s, %s, %s, %s);"
            val = (email, 0, 0, current_date, 0)
            self.mycursor.execute(sql, val)
            self.connection.commit()

        return register
    
    def check_details(self, email, first_name, last_name):
        """Check if email/first/lastname contains nums."""
        isnum = 0
        for i in first_name:
            for c in last_name:
                if i.isdigit() or c.isdigit():
                    isnum += 1
        split = email.split(".")
        for c in split[-1]:
            if c.isdigit():
                isnum += 1


        if isnum > 0:
            return False

        return True



    def log_out(self):
        """Log out."""
        self.disconnect()


    def check_email(self, email):
        """Validate email format."""
        import re

        # Make a regular expression
        # for validating an Email
        regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"

        if re.search(regex, email):
            return True

        else:
            return False


    def new_customer(self, email):
        """Check if customer is new."""
        sql = "select new_customer from account where email = %s"
        val = (email,)
        self.mycursor.execute(sql, val)
        myresult = self.mycursor.fetchone()[0]
        if myresult == "Y":
            return True
        else:
            return False

    def get_buffert(self, email):
        sql = "SELECT buffert FROM budget WHERE account_email = %s"
        val = (email,)
        self.mycursor.execute(sql, val)
        myresult = self.mycursor.fetchone()[0]
        return myresult
    
    def get_saving_goal(self, email):
        sql = "SELECT saving_goal FROM budget WHERE account_email = %s"
        val = (email,)
        self.mycursor.execute(sql, val)
        myresult = self.mycursor.fetchone()[0]
        return myresult

    def update_buffert(self, email, buffert):
        sql = "UPDATE budget SET buffert = %s WHERE account_email = %s; "
        val = (buffert, email,)
        self.mycursor.execute(sql, val)
        self.connection.commit()

    def update_saving_goal(self, email, saving_goal):
        sql = "UPDATE budget SET saving_goal = %s WHERE account_email = %s; "
        val = (saving_goal, email,)
        self.mycursor.execute(sql, val)
        self.connection.commit()
if __name__ == "__main__":
    pass