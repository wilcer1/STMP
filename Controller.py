# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import account
import database_connection as DB
from View import gui_module as gui

class LoginScreen(QMainWindow, gui.Ui_LoginScreen):
    """Inherit from the code for the ui to have all information necessary."""

    # Login Screen Controller
    def __init__(self):
        """Constructor that runs the setup."""
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.pushButton.clicked.connect(
            self.loginFunc
        )  # Call function when button is pressed
        self.pushButton_2.clicked.connect(self.registerFunc)  #
    
    def loginFunc(self):
        """Confirm that login is correct."""
        username = (
            self.lineEdit.text()
        )  # Get the text from the username & password lineedit
        password = self.lineEdit_2.text()  #
        # Check if password and username isnt empty, if it is, popup
        if DB.verify_login(username, password) \
                and not DB.new_customer(username):
            self.customer.budget.set_budget(DB.get_income(self.customer.email),
                                       DB.get_variable_expenses(self.customer.email),
                                       DB.get_fixed_expenses(self.customer.email))
            self.displayUi = MenuScreen()
            self.hide()
            self.displayUi.show()
        elif DB.verify_login(username, password) and DB.new_self.customer(username):
            self.displayUi = FirstLoginScreen()
            self.hide()
            self.displayUi.show()
        else:
            self.popUp.exec_()

    def registerFunc(self):
        """Go to registerScreen."""
        self.displayUi = RegisterScreen()
        self.hide()
        self.displayUi.show()

class FirstLoginScreen(QMainWindow, gui.Ui_FirstLoginScreen):
    def __init__(self):
        """Constructor that runs the setup."""
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.saveButton.clicked.connect(self.save_change)
        self.pushButton.clicked.connect(self.go_back)

    def save_change(self):
        try:
            income = abs(float(self.listOfIncomeSEK.item(1).text()))
            fixed_expenses = {
                                "rent": abs(float(self.listOfExpensesSEK.item(4).text())),
                                "subscription":  abs(float(self.listOfExpensesSEK.item(2).text())),
                                "insurance":  abs(float(self.listOfExpensesSEK.item(3).text())),
                                "others":  abs(float(self.listOfExpensesSEK.item(5).text()))
                            }
            variable_expenses = {
                                "food":   abs(float(self.listOfExpensesSEK.item(11).text())),
                                "bills":   abs(float(self.listOfExpensesSEK.item(12).text())),
                                "transportation":   abs(float(self.listOfExpensesSEK.item(13).text())),
                                "hygien":   abs(float(self.listOfExpensesSEK.item(14).text())),
                                "clothes":   abs(float(self.listOfExpensesSEK.item(15).text())),
                                "entertainment":   abs(float(self.listOfExpensesSEK.item(16).text())),
                                "others":   abs(float(self.listOfExpensesSEK.item(17).text()))
                            }
            self.customer.budget.set_budget(income, fixed_expenses, variable_expenses)
            DB.set_variable_expenses(self.customer.email, variable_expenses)
            DB.set_fixed_expenses(self.customer.email, fixed_expenses)
            DB.not_new_customer(self.customer.email)

            self.displayUi = MenuScreen()
            self.hide()
            self.displayUi.show()
        except Exception:
            self.popUp.exec_()

    def go_back(self):
        self.displayUi = LoginScreen()
        # logout
        self.hide()
        self.displayUi.show()


class MenuScreen(QMainWindow, gui.Ui_MenuScreen):
    """Inherit from the code for the ui to have all information necessary."""

    # Logged in menu screen Controller
    def __init__(self):
        """Constructor that runs the setup."""
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.pushButton.clicked.connect(
            self.MakeBudget
        )  # Call function when button is pressed
        self.pushButton_5.clicked.connect(self.log_out)
        self.pushButton_2.clicked.connect(self.longtermSaving)

    def MakeBudget(self):
        """Display makebudget."""
        self.displayUi = BudgetChoiceScreen()
        self.hide()
        self.displayUi.show()

    def longtermSaving(self):
        """Switch screen."""
        self.displayUi = SavingGoal()
        self.hide()
        self.displayUi.show()

    def log_out(self):
        """Log out the customer and empty singleton."""
        DB.log_out()
        self.customer.log_out()
        self.displayUi = LoginScreen()
        self.hide()
        self.displayUi.show()


class RegisterScreen(QMainWindow, gui.Ui_RegisterScreen):
    """Inherit from the code for the ui to have all information necessary."""

    # Register user window controller
    def __init__(self):
        """Constructor that runs the setup."""
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.pushButton.clicked.connect(
            self.Register
        )  # Call function when button is pressed
        self.pushButton_2.clicked.connect(self.goBack)  #

    def Register(self):
        """Get details for register function."""
        if not self.firstname.text() or \
            not self.lastname.text() or not self.password.text():
            self.popUp.setText("Some fields empty, please fill them")
            self.popUp.exec_()
        else:
            val = (
                self.username.text(),
                self.firstname.text(),
                self.lastname.text(),
                self.password.text(),
                "Y"
                )
            if DB.register_account(val): # Check if account is in DB
                self.popUp.setText("Registered successfully, please log in")
                self.popUp.exec_()
                self.displayUi = LoginScreen()
                self.hide()
                self.displayUi.show()
            else:
                self.popUp.setText("email already exists, try log in")
                self.popUp.exec_() # popup error wrong username/password

    def goBack(self):
        """ Go back to login page."""
        self.displayUi = LoginScreen()
        self.hide()
        self.displayUi.show()


class BudgetChoiceScreen(QMainWindow, gui.Ui_BudgetChoiceScreen):
    """Inherit from the code for the ui to have all information necessary."""

    # Login Screen Controller
    def __init__(self):
        """Constructor that runs setup and connects buttons."""
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.pushButton_3.clicked.connect(
            self.Manual
        )  # Call function when button is pressed
        self.pushButton_2.clicked.connect(self.Auto)  #  -""-
        self.pushButton.clicked.connect(self.goBack)  #    -""-

    def Manual(self):
        """Show the budget screen."""
        self.displayUi = BudgetScreen()
        self.hide()
        self.displayUi.show()

    def Auto(self):
        pass

    def goBack(self):
        """Go back to previous screen."""
        self.displayUi = MenuScreen()
        self.hide()
        self.displayUi.show()


class BudgetScreen(QMainWindow, gui.Ui_BudgetScreen):
    def __init__(self):
        """Constructor that runs setup and buttons & labels."""
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.incomeItem = self.listOfIncomeSEK.item(1)
        self.incomeItem.setText(f"{self.customer.budget.income}")
        self.saveButton.clicked.connect(self.save_change)
        self.backButton.clicked.connect(self.go_back)
        total_fix, total_var = self.customer.budget.get_expenses()
        self.listOfExpensesSEK.item(1).setText(total_fix)
        self.listOfExpensesSEK.item(10).setText(total_var)
        self.set_list_of_expenses()
        self.label_3.setText(str(self.customer.budget.income - self.customer.budget.get_total_expenses()))

    def save_change(self):
        """Save the changes entered to DB and singleton."""
        try:
            self.customer.budget.income = abs(float(self.incomeItem.text()))
            self.incomeItem.setText(f"{self.customer.budget.income}")
            fixed_expenses = {
                                "rent":  abs(float(self.listOfExpensesSEK.item(4).text())),
                                "subscription":  abs(float(self.listOfExpensesSEK.item(2).text())),
                                "insurance":  abs(float(self.listOfExpensesSEK.item(3).text())),
                                "others":  abs(float(self.listOfExpensesSEK.item(5).text()))
                            }
            variable_expenses = {
                                "food":   abs(float(self.listOfExpensesSEK.item(11).text())),
                                "bills":   abs(float(self.listOfExpensesSEK.item(12).text())),
                                "transportation":   abs(float(self.listOfExpensesSEK.item(13).text())),
                                "hygien":   abs(float(self.listOfExpensesSEK.item(14).text())),
                                "clothes":   abs(float(self.listOfExpensesSEK.item(15).text())),
                                "entertainment":   abs(float(self.listOfExpensesSEK.item(16).text())),
                                "others":   abs(float(self.listOfExpensesSEK.item(17).text()))
                            }
            self.customer.budget.set_budget(self.customer.budget.income,
                                    variable_expenses, fixed_expenses)
            # update instead of set
            DB.update_variable_expenses(self.customer.email, variable_expenses)
            DB.update_fixed_expenses(self.customer.email, fixed_expenses)
            total_fix, total_var = self.customer.budget.get_expenses()
            self.listOfExpensesSEK.item(1).setText(total_fix)
            self.listOfExpensesSEK.item(10).setText(total_var)
            self.label_3.setText(str(self.customer.budget.income - self.customer.budget.get_total_expenses()))
        except Exception:
            self.popUp.exec_()

    def go_back(self):
        """Go back to the budget choice screen."""
        self.displayUi = BudgetChoiceScreen()
        self.hide()
        self.displayUi.show()

    def set_list_of_expenses(self):
        """Set the items in the listwidget to the budget numbers stored in DB."""
        fix_exp = DB.get_fixed_expenses(self.customer.email)
        var_exp = DB.get_variable_expenses(self.customer.email)
        self.listOfExpensesSEK.item(2).setText(str(fix_exp["subscription"]))
        self.listOfExpensesSEK.item(3).setText(str(fix_exp["insurance"]))
        self.listOfExpensesSEK.item(4).setText(str(fix_exp["rent"]))
        self.listOfExpensesSEK.item(5).setText(str(fix_exp["others"]))

        self.listOfExpensesSEK.item(11).setText(str(var_exp["food"]))
        self.listOfExpensesSEK.item(12).setText(str(var_exp["bills"]))
        self.listOfExpensesSEK.item(13).setText(str(var_exp["transportation"]))
        self.listOfExpensesSEK.item(14).setText(str(var_exp["hygien"]))
        self.listOfExpensesSEK.item(15).setText(str(var_exp["clothes"]))
        self.listOfExpensesSEK.item(16).setText(str(var_exp["entertainment"]))
        self.listOfExpensesSEK.item(17).setText(str(var_exp["others"]))


class SavingGoal(QMainWindow, gui.Ui_SavinggoalScreen):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goBack)
        self.pushButton_2.clicked.connect(self.calculate)

    def goBack(self):
        self.displayUi = MenuScreen()
        self.hide()
        self.displayUi.show()

    def calculate(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            amountPerMonth = float(self.lineEdit.text())
            savingGoal = float(self.lineEdit_2.text())
            timeToReach = savingGoal / amountPerMonth
            self.label_2.setText(f"It will take {timeToReach} months to reach your goal")
        else:
            self.popUp.exec_()



if __name__ == "__main__":
    import sys
    DB = DB.database_connection()
    customer = account.Account.getInstance()
    app = QApplication(sys.argv)
    MainWindow = LoginScreen()  # Use the login screen as the mainwindow to start
    MainWindow.show()
    sys.exit(app.exec_())
