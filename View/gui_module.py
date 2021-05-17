from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from account import Account
import database_connection as DB

class Ui_LoginScreen(object):
    """Main Login Window."""

    def setupUi(self, MainWindow):
        self.customer = Account.getInstance()
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


class Ui_FirstLoginScreen(object):
    def setupUi(self, MainWindow):
        self.customer = Account.getInstance()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 572)
        MainWindow.setStyleSheet("background-color: rgb(3, 130, 168);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 47, 21))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 20, 51, 21))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.popUp = QMessageBox()
        self.popUp.setWindowTitle("Error")
        self.popUp.setText("Bad input, please only enter integers")
        self.listOfIncome = QtWidgets.QListWidget(self.centralwidget)
        self.listOfIncome.setGeometry(QtCore.QRect(80, 50, 121, 391))
        self.listOfIncome.setStyleSheet("background-color:\
                                        rgb(255, 255, 255);")
        self.listOfIncome.setObjectName("listOfIncome")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listOfIncome.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfIncome.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfIncome.addItem(item)
        self.listOfExpenses = QtWidgets.QListWidget(self.centralwidget)
        self.listOfExpenses.setGeometry(QtCore.QRect(450, 50, 131, 391))
        self.listOfExpenses.setStyleSheet("background-color: \
                                          rgb(255, 255, 255);")
        self.listOfExpenses.setObjectName("listOfExpenses")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(700, 480, 75, 23))
        self.saveButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.saveButton.setObjectName("saveButton")
        self.listOfIncomeSEK = QtWidgets.QListWidget(self.centralwidget)
        self.listOfIncomeSEK.setGeometry(QtCore.QRect(200, 50, 141, 391))
        self.listOfIncomeSEK.setStyleSheet("background-color: \
                                            rgb(255, 255, 255);")
        self.listOfIncomeSEK.setObjectName("listOfIncomeSEK")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listOfIncomeSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(
                      QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled
                      )
        self.listOfIncomeSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfIncomeSEK.addItem(item)
        self.listOfExpensesSEK = QtWidgets.QListWidget(self.centralwidget)
        self.listOfExpensesSEK.setGeometry(QtCore.QRect(580, 50, 131, 391))
        self.listOfExpensesSEK.setStyleSheet("background-color: \
                                             rgb(255, 255, 255);")
        self.listOfExpensesSEK.setObjectName("listOfExpensesSEK")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 480, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 0, 211, 21))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
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
        self.label.setText(_translate("MainWindow", "Income"))
        self.label_2.setText(_translate("MainWindow", "Expenses"))
        __sortingEnabled = self.listOfIncome.isSortingEnabled()
        self.listOfIncome.setSortingEnabled(False)
        item = self.listOfIncome.item(0)
        item.setText(_translate("MainWindow", "Type:"))
        item = self.listOfIncome.item(1)
        item.setText(_translate("MainWindow", "Total Income"))
        self.listOfIncome.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listOfExpenses.isSortingEnabled()
        self.listOfExpenses.setSortingEnabled(False)
        item = self.listOfExpenses.item(0)
        item.setText(_translate("MainWindow", "Type:"))
        item = self.listOfExpenses.item(1)
        item.setText(_translate("MainWindow", "Fixed expenses:"))
        item = self.listOfExpenses.item(2)
        item.setText(_translate("MainWindow", "Subscriptions"))
        item = self.listOfExpenses.item(3)
        item.setText(_translate("MainWindow", "Insurance"))
        item = self.listOfExpenses.item(4)
        item.setText(_translate("MainWindow", "Rent"))
        item = self.listOfExpenses.item(5)
        item.setText(_translate("MainWindow", "Others"))
        item = self.listOfExpenses.item(10)
        item.setText(_translate("MainWindow", "Variable expenses:"))
        item = self.listOfExpenses.item(11)
        item.setText(_translate("MainWindow", "Transportation"))
        item = self.listOfExpenses.item(12)
        item.setText(_translate("MainWindow", "Entertainment"))
        item = self.listOfExpenses.item(13)
        item.setText(_translate("MainWindow", "Clothes"))
        item = self.listOfExpenses.item(14)
        item.setText(_translate("MainWindow", "Hygien"))
        item = self.listOfExpenses.item(15)
        item.setText(_translate("MainWindow", "Food"))
        item = self.listOfExpenses.item(16)
        item.setText(_translate("MainWindow", "Bills"))
        item = self.listOfExpenses.item(17)
        item.setText(_translate("MainWindow", "Others"))
        self.listOfExpenses.setSortingEnabled(__sortingEnabled)
        self.saveButton.setText(_translate("MainWindow", "Save"))
        __sortingEnabled = self.listOfIncomeSEK.isSortingEnabled()
        self.listOfIncomeSEK.setSortingEnabled(False)
        item = self.listOfIncomeSEK.item(0)
        item.setText(_translate("MainWindow", "Amount:"))
        item = self.listOfIncomeSEK.item(1)
        item.setText(_translate("MainWindow", "0"))
        self.listOfIncomeSEK.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listOfExpensesSEK.isSortingEnabled()
        self.listOfExpensesSEK.setSortingEnabled(False)
        item = self.listOfExpensesSEK.item(0)
        item.setText(_translate("MainWindow", "Amount:"))
        item = self.listOfExpensesSEK.item(2)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(3)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(4)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(5)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(11)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(12)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(13)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(14)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(15)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(16)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(17)
        item.setText(_translate("MainWindow", "0"))
        self.listOfExpensesSEK.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow",
                                        "Set your income and expenses"))


class Ui_MenuScreen(object):
    """Menu Window"""

    def setupUi(self, MainWindow):
        self.customer = Account.getInstance()
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
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 300, 131, 23))
        self.pushButton_5.setObjectName("pushButton_5")
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
        self.label.setText(_translate("MainWindow", f"Welcome,\
                                      {self.customer.first_name}"))
        self.pushButton.setText(_translate("MainWindow", "Make a budget"))
        self.pushButton_2.setText(_translate("MainWindow",
                                             "Create long-term savings"))
        self.pushButton_3.setText(_translate("MainWindow", "eee"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "Log out"))


class Ui_RegisterScreen(object):
    """Register window."""

    def setupUi(self, MainWindow):
        self.customer = Account.getInstance()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 20, 47, 13))
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(290, 70, 113, 20))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(290, 120, 113, 20))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.firstname = QtWidgets.QLineEdit(self.centralwidget)
        self.firstname.setGeometry(QtCore.QRect(290, 170, 113, 20))
        self.firstname.setObjectName("firstname")
        self.lastname = QtWidgets.QLineEdit(self.centralwidget)
        self.lastname.setGeometry(QtCore.QRect(290, 220, 113, 20))
        self.lastname.setObjectName("lastname")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 150, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 200, 61, 16))
        self.label_6.setObjectName("label_6")
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
        self.popUp.setText("Incorrect email, please try again")
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
        self.pushButton_2.setText(_translate("MainWindow", "Back"))


class Ui_BudgetChoiceScreen(object):
    def setupUi(self, MainWindow):
        self.customer = Account.getInstance()
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
        self.pushButton_2.setText(_translate("MainWindow",
                                  "Get help with budget"))
        self.pushButton_3.setText(_translate("MainWindow",
                                             "Make your own budget"))
        self.pushButton.setText(_translate("MainWindow", "Back"))


class Ui_BudgetScreen(object):
    def setupUi(self, MainWindow):
        self.customer = Account.getInstance()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 572)
        MainWindow.setStyleSheet("background-color: rgb(3, 130, 168);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 47, 21))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 20, 51, 21))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.listOfIncome = QtWidgets.QListWidget(self.centralwidget)
        self.listOfIncome.setGeometry(QtCore.QRect(80, 50, 121, 391))
        self.listOfIncome.setStyleSheet("background-color: \
                                        rgb(255, 255, 255);")
        self.listOfIncome.setObjectName("listOfIncome")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listOfIncome.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfIncome.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfIncome.addItem(item)
        self.listOfExpenses = QtWidgets.QListWidget(self.centralwidget)
        self.listOfExpenses.setGeometry(QtCore.QRect(450, 50, 131, 391))
        self.listOfExpenses.setStyleSheet("background-color: \
                                          rgb(255, 255, 255);")
        self.listOfExpenses.setObjectName("listOfExpenses")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpenses.addItem(item)
        self.moneyleftLabel = QtWidgets.QLabel(self.centralwidget)
        self.moneyleftLabel.setGeometry(QtCore.QRect(330, 470, 131, 41))
        self.moneyleftLabel.setStyleSheet("background-color: \
                                          rgb(255, 255, 255);")
        self.moneyleftLabel.setAlignment(QtCore.Qt.AlignHCenter |
                                         QtCore.Qt.AlignTop)
        self.moneyleftLabel.setObjectName("moneyleftLabel")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(700, 480, 75, 23))
        self.saveButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.saveButton.setObjectName("saveButton")
        self.listOfIncomeSEK = QtWidgets.QListWidget(self.centralwidget)
        self.listOfIncomeSEK.setGeometry(QtCore.QRect(200, 50, 141, 391))
        self.listOfIncomeSEK.setStyleSheet("background-color: \
                                            rgb(255, 255, 255);")
        self.listOfIncomeSEK.setObjectName("listOfIncomeSEK")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listOfIncomeSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfIncomeSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfIncomeSEK.addItem(item)
        self.listOfExpensesSEK = QtWidgets.QListWidget(self.centralwidget)
        self.listOfExpensesSEK.setGeometry(QtCore.QRect(580, 50, 131, 391))
        self.listOfExpensesSEK.setStyleSheet("background-color: \
                                             rgb(255, 255, 255);")
        self.listOfExpensesSEK.setObjectName("listOfExpensesSEK")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled |
                      QtCore.Qt.ItemIsUserCheckable |
                      QtCore.Qt.ItemIsEnabled)
        self.listOfExpensesSEK.addItem(item)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(20, 480, 75, 23))
        self.backButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backButton.setObjectName("backButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 490, 47, 13))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.popUp = QMessageBox()
        self.popUp.setWindowTitle("Error")
        self.popUp.setText("Bad input, please enter only positive integers")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Income"))
        self.label_2.setText(_translate("MainWindow", "Expenses"))
        __sortingEnabled = self.listOfIncome.isSortingEnabled()
        self.listOfIncome.setSortingEnabled(False)
        item = self.listOfIncome.item(0)
        item.setText(_translate("MainWindow", "Type:"))
        item = self.listOfIncome.item(1)
        item.setText(_translate("MainWindow", "Total Income"))
        self.listOfIncome.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listOfExpenses.isSortingEnabled()
        self.listOfExpenses.setSortingEnabled(False)
        item = self.listOfExpenses.item(0)
        item.setText(_translate("MainWindow", "Type:"))
        item = self.listOfExpenses.item(1)
        item.setText(_translate("MainWindow", "Fixed expenses:"))
        item = self.listOfExpenses.item(2)
        item.setText(_translate("MainWindow", "Subscriptions"))
        item = self.listOfExpenses.item(3)
        item.setText(_translate("MainWindow", "Insurance"))
        item = self.listOfExpenses.item(4)
        item.setText(_translate("MainWindow", "Rent"))
        item = self.listOfExpenses.item(5)
        item.setText(_translate("MainWindow", "Others"))
        item = self.listOfExpenses.item(10)
        item.setText(_translate("MainWindow", "Variable expenses:"))
        item = self.listOfExpenses.item(11)
        item.setText(_translate("MainWindow", "Food"))
        item = self.listOfExpenses.item(12)
        item.setText(_translate("MainWindow", "Bills"))
        item = self.listOfExpenses.item(13)
        item.setText(_translate("MainWindow", "Transportation"))
        item = self.listOfExpenses.item(14)
        item.setText(_translate("MainWindow", "Hygien"))
        item = self.listOfExpenses.item(15)
        item.setText(_translate("MainWindow", "Clothes"))
        item = self.listOfExpenses.item(16)
        item.setText(_translate("MainWindow", "Entertainment"))
        item = self.listOfExpenses.item(17)
        item.setText(_translate("MainWindow", "Others"))
        self.listOfExpenses.setSortingEnabled(__sortingEnabled)
        self.moneyleftLabel.setText(_translate("MainWindow",
                                               "Money left to spend:"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        __sortingEnabled = self.listOfIncomeSEK.isSortingEnabled()
        self.listOfIncomeSEK.setSortingEnabled(False)
        item = self.listOfIncomeSEK.item(0)
        item.setText(_translate("MainWindow", "Amount:"))
        item = self.listOfIncomeSEK.item(1)
        item.setText(_translate("MainWindow", "0"))
        self.listOfIncomeSEK.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listOfExpensesSEK.isSortingEnabled()
        self.listOfExpensesSEK.setSortingEnabled(False)
        item = self.listOfExpensesSEK.item(0)
        item.setText(_translate("MainWindow", "Amount:"))
        item = self.listOfExpensesSEK.item(1)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(2)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(3)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(4)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(5)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(10)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(11)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(12)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(13)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(14)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(15)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(16)
        item.setText(_translate("MainWindow", "0"))
        item = self.listOfExpensesSEK.item(17)
        item.setText(_translate("MainWindow", "0"))
        self.listOfExpensesSEK.setSortingEnabled(__sortingEnabled)
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow", "put money left here"))


class Ui_SavinggoalScreen(object):
    def setupUi(self, MainWindow):
        self.customer = Account.getInstance()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 271)
        MainWindow.setStyleSheet("background-color: rgb(3, 130, 168);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 71, 21))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.popUp = QMessageBox()
        self.popUp.setWindowTitle("Error")
        self.popUp.setText("Bad input, enter only positive numbers")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 70, 141, 20))
        self.lineEdit.setToolTip("")
        self.lineEdit.setAccessibleDescription("")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 110, 141, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(50, 150, 191, 21))
        # self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.label_2.setText("")
        # self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 30, 151, 71))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading |
                                  QtCore.Qt.AlignLeft |
                                  QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 200, 101, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 150, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: \
                                        rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 140, 141, 40))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 21))
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
        self.label.setText(_translate("MainWindow", "Saving goal"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow",
                                                    "Amount to save a month"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow",
                                                      "Your saving goal"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p>Play around and \
                                            see how long </p><p>it would take \
                                            to reach your</p><p>saving goal \
                                            or buffert</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate"))




