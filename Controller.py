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
import database_connection


class Ui_LoginScreen(object):
    """Main Login Window."""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 150, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 210, 71, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 180, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 240, 113, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 360, 141, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 100, 191, 61))
        self.label_3.setObjectName("label_3")
        self.popUp = QMessageBox()
        self.popUp.setWindowTitle("Error")
        self.popUp.setText("Username/Password incorrect. Please try again")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log in"))
        self.label_3.setText(_translate("MainWindow", "STMP"))
        self.pushButton_2.setText(
            _translate("MainWindow", "Not Registered? Click here")
        )


class Ui_MenuScreen(object):
    """Menu Window"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 50, 100, 13))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 100, 131, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 140, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 180, 131, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 220, 131, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", f"Welcome, {customer.first_name}"))
        self.pushButton.setText(_translate("MainWindow", "Make a budget"))
        self.pushButton_2.setText(_translate("MainWindow", "Create long-term savings"))
        self.pushButton_3.setText(_translate("MainWindow", "eee"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))


class Ui_RegisterScreen(object):
    """Register window."""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 220, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 170, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 150, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 200, 61, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 320, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(290, 270, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 250, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 300, 61, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 360, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 360, 141, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.popUp = QMessageBox()
        self.popUp.setWindowTitle("Error")
        self.popUp.setText("Email already exists, go back and log in")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Register¨¨"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Register"))
        self.label_5.setText(_translate("MainWindow", "First name"))
        self.label_6.setText(_translate("MainWindow", "Last name"))
        self.label_7.setText(_translate("MainWindow", "Income"))
        self.label_8.setText(_translate("MainWindow", "Expenses"))
        self.pushButton_2.setText(_translate("MainWindow", "Back"))


class Ui_BudgetChoiceScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 392)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 170, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 120, 131, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Get help with budget"))
        self.pushButton_3.setText(_translate("MainWindow", "Make your own budget"))
        self.pushButton.setText(_translate("MainWindow", "Back"))


class Ui_BudgetScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 40, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(330, 80, 118, 23))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(110, 190, 118, 23))
        self.progressBar_2.setProperty("value", 20)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 170, 47, 13))
        self.label_4.setObjectName("label_4")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(110, 290, 118, 23))
        self.progressBar_3.setProperty("value", 20)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 250, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(140, 270, 47, 13))
        self.label_6.setObjectName("label_6")
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(110, 390, 118, 23))
        self.progressBar_4.setProperty("value", 20)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 350, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 370, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(350, 270, 47, 13))
        self.label_9.setObjectName("label_9")
        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setGeometry(QtCore.QRect(320, 290, 118, 23))
        self.progressBar_5.setProperty("value", 20)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_6.setGeometry(QtCore.QRect(320, 390, 118, 23))
        self.progressBar_6.setProperty("value", 20)
        self.progressBar_6.setObjectName("progressBar_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(340, 350, 47, 13))
        self.label_10.setObjectName("label_10")
        self.progressBar_7 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_7.setGeometry(QtCore.QRect(320, 190, 118, 23))
        self.progressBar_7.setProperty("value", 20)
        self.progressBar_7.setObjectName("progressBar_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 150, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(320, 250, 131, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(350, 170, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(350, 370, 47, 13))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(570, 370, 47, 13))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(570, 270, 47, 13))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(540, 250, 131, 16))
        self.label_17.setObjectName("label_17")
        self.progressBar_8 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_8.setGeometry(QtCore.QRect(540, 190, 118, 23))
        self.progressBar_8.setProperty("value", 20)
        self.progressBar_8.setObjectName("progressBar_8")
        self.progressBar_9 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_9.setGeometry(QtCore.QRect(540, 290, 118, 23))
        self.progressBar_9.setProperty("value", 20)
        self.progressBar_9.setObjectName("progressBar_9")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(560, 350, 47, 13))
        self.label_18.setObjectName("label_18")
        self.progressBar_10 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_10.setGeometry(QtCore.QRect(540, 390, 118, 23))
        self.progressBar_10.setProperty("value", 20)
        self.progressBar_10.setObjectName("progressBar_10")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(570, 150, 47, 13))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(570, 170, 47, 13))
        self.label_20.setObjectName("label_20")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 71, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(30, 60, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.popUp = QMessageBox()
        self.popUp.setWindowTitle("Error")
        self.popUp.setText("Incorrect income input")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 490, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 80, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Total Monthly Budget:"))
        self.label_2.setText(_translate("MainWindow", "SEK"))
        self.label_3.setText(_translate("MainWindow", "Food"))
        self.label_4.setText(_translate("MainWindow", "SEK"))
        self.label_5.setText(_translate("MainWindow", "Fixed Expenses"))
        self.label_6.setText(_translate("MainWindow", "SEK"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "SEK"))
        self.label_9.setText(_translate("MainWindow", "SEK"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "something"))
        self.label_12.setText(_translate("MainWindow", "Fixed Expenses"))
        self.label_13.setText(_translate("MainWindow", "SEK"))
        self.label_14.setText(_translate("MainWindow", "SEK"))
        self.label_15.setText(_translate("MainWindow", "SEK"))
        self.label_16.setText(_translate("MainWindow", "SEK"))
        self.label_17.setText(_translate("MainWindow", "Fixed Expenses"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "something"))
        self.label_20.setText(_translate("MainWindow", "SEK"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.label_21.setText(
            _translate("MainWindow", "Your total monthly income in SEK:")
        )
        self.pushButton_2.setText(_translate("MainWindow", "OK"))


class LoginScreen(QMainWindow, Ui_LoginScreen):
    """Inherit from the code for the ui to have all information necessary."""

    # Login Screen Controller
    def __init__(self):
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.pushButton.clicked.connect(
            self.loginFunc
        )  # Call function when button is pressed
        self.pushButton_2.clicked.connect(self.registerFunc)  #

    def loginFunc(self):
        username = (
            self.lineEdit.text()
        )  # Get the text from the username & password lineedit
        password = self.lineEdit_2.text()  #
        # Check if password and username isnt empty, if it is, popup
        if database_connection.verify_login(username, password):
            self.displayUi = MenuScreen()
            self.hide()
            self.displayUi.show()
        else:
            self.popUp.exec_()

    def registerFunc(self):
        self.displayUi = RegisterScreen()
        self.hide()
        self.displayUi.show()


class MenuScreen(QMainWindow, Ui_MenuScreen):
    """Inherit from the code for the ui to have all information necessary."""

    # Logged in menu screen Controller
    def __init__(self):
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.pushButton.clicked.connect(
            self.MakeBudget
        )  # Call function when button is pressed

    def MakeBudget(self):
        # display makebudget
        self.displayUi = BudgetChoiceScreen()
        self.hide()
        self.displayUi.show()


class RegisterScreen(QMainWindow, Ui_RegisterScreen):
    """Inherit from the code for the ui to have all information necessary."""

    # Register user window controller
    def __init__(self):
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.pushButton.clicked.connect(
            self.Register
        )  # Call function when button is pressed
        self.pushButton_2.clicked.connect(self.goBack)  #

    def Register(self):
        """Get details for register function."""
        val = (
            self.lineEdit.text(),
            self.lineEdit_2.text(),  # Insert all the values
            self.lineEdit_4.text(),
            self.lineEdit_3.text(),  # from the lineedits
            self.lineEdit_6.text(),
            self.lineEdit_5.text(),  # into a tuple
        )

        if database_connection.register_account(val):
            self.popUp.setText("Registered successfully, please log in")
            self.popUp.exec_()
            self.displayUi = LoginScreen()
            self.hide()
            self.displayUi.show()
        else:
            self.popUp.exec_()

    def goBack(self):
        """ Go back to login page."""
        self.displayUi = LoginScreen()
        self.hide()
        self.displayUi.show()


class BudgetChoiceScreen(QMainWindow, Ui_BudgetChoiceScreen):
    """Inherit from the code for the ui to have all information necessary."""

    # Login Screen Controller
    def __init__(self):
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.pushButton_3.clicked.connect(
            self.Manual
        )  # Call function when button is pressed
        self.pushButton_2.clicked.connect(self.Auto)  #  -""-
        self.pushButton.clicked.connect(self.goBack)  #    -""-

    def Manual(self):
        self.displayUi = BudgetScreen()
        self.hide()
        self.displayUi.show()

    def Auto(self):
        pass

    def goBack(self):
        self.displayUi = MenuScreen()
        self.hide()
        self.displayUi.show()


class BudgetScreen(QMainWindow, Ui_BudgetScreen):
    # Budget Screen Controller
    def __init__(self):
        super().__init__()  # Call the superclass constructor
        self.setupUi(self)  # Run the code that creates the UI layout
        self.pushButton.clicked.connect(self.goBack)
        self.pushButton_2.clicked.connect(self.updateIncome)

    def goBack(self):
        self.displayUi = BudgetChoiceScreen()
        self.hide()
        self.displayUi.show()

    def updateIncome(self):
        income = self.lineEdit.text()  # Get the lineedit text with the income
        # if income isInstance(int) and income > 0:
        income = int(income)  # convert it to int
        self.label_2.setText(f"{income} SEK")  # set the income in GUI
        self.lineEdit.clear()  # Clear the lineedit

        """Set the labels to 1/5 of the income if its not < 0"""

        self.label_4.setText(f"{income / 5} SEK")
        self.label_6.setText(f"{income / 5} SEK")
        self.label_8.setText(f"{income / 5} SEK")
        self.label_9.setText(f"{income / 5} SEK")
        self.label_13.setText(f"{income / 5} SEK")
        self.label_14.setText(f"{income / 5} SEK")
        self.label_15.setText(f"{income / 5} SEK")
        self.label_16.setText(f"{income / 5} SEK")
        self.label_20.setText(f"{income / 5} SEK")


if __name__ == "__main__":
    import sys

    customer = account.Account.getInstance()
    app = QApplication(sys.argv)
    MainWindow = LoginScreen()  # Use the login screen as the mainwindow to start
    MainWindow.show()
    sys.exit(app.exec_())
