"""Unittest for DB."""

import unittest
import database_connection as DB
import mysql.connector
from mysql.connector import Error


class TestPlayerClass(unittest.TestCase):
    """Test Player Class."""

    @classmethod
    def setUpClass(cls):
        """Set up acc for testing."""
        try:
            # Connect to the db
            cls.connection = mysql.connector.connect(
                host="den1.mysql5.gear.host",
                user="stmp",
                password="Zq65rS9Q?x!D",
                database="stmp",
            )
        finally:
            cls.mycursor = cls.connection.cursor()

        # set up a test acc for testing purposes
        val = ("test@unit.se", "test", "test2", "test3", "N")
        sql = "INSERT INTO account VALUES (%s, %s, %s, %s, %s);"
        cls.mycursor.execute(sql, val)
        cls.connection.commit()
        sql = "INSERT INTO budget VALUES (%s, %s, %s, %s, %s);"
        val = ("test@unit.se", 1, 2, "2001-04-04", 3)
        cls.mycursor.execute(sql, val)
        cls.connection.commit()
        sql = "INSERT INTO variable_expenses VALUES (%s, %s, %s, %s, %s,\
                                                     %s, %s, %s);"
        val = ("test@unit.se", 1, 2, 3, 4, 5, 6, 7)
        cls.mycursor.execute(sql, val)
        cls.connection.commit()
        sql = "INSERT INTO fixed_expenses VALUES (%s, %s, %s, %s, %s);"
        val = ("test@unit.se", 1, 2, 3, 4)
        cls.mycursor.execute(sql, val)
        cls.connection.commit()

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database."""
        val = ("test@unit.se",)
        sql = "DELETE FROM variable_expenses WHERE budget_account_email = %s;"
        cls.mycursor.execute(sql, val)
        cls.connection.commit()
        sql = "DELETE FROM fixed_expenses WHERE budget_account_email = %s;"
        cls.mycursor.execute(sql, val)
        cls.connection.commit()
        sql = "DELETE FROM budget WHERE account_email = %s;"
        cls.mycursor.execute(sql, val)
        cls.connection.commit()
        sql = "DELETE FROM account WHERE email = %s;"
        cls.mycursor.execute(sql, val)
        cls.connection.commit()
        try:
            if cls.connection is not None and cls.connection.is_connected():
                cls.mycursor.close()
                cls.connection.close()
        except Error as e:
            print(e)

    def test_get_income(self):
        """Test get_income."""
        exp = 3
        res = DB.get_income("test@unit.se")
        self.assertEqual(res, exp)

    def test_get_basic_info(self):
        """Test get_basic_info."""
        exp = ("test@unit.se", "test", "test2", "test3", "N")
        res = DB.get_basic_info("test@unit.se")
        self.assertTrue(exp == res)

    def test_verify_login(self):
        """Test verify_login."""
        res = DB.verify_login("test@unit.se", "test3")
        self.assertTrue(res)

        res = DB.verify_login("test@unit.se", "wrong")
        self.assertFalse(res)

    def test_register_account(self):
        """Test register_account."""
        res = DB.register_account("test@unit.se")
        self.assertFalse(res)

    def test_check_email(self):
        """Test check_email method."""
        self.assertTrue(DB.check_email("test@unit.se"))
        self.assertFalse(DB.check_email("s"))

    def test_new_customer(self):
        """Test new_customer function."""
        res = DB.new_customer("test@unit.se")
        self.assertFalse(res)

    def test_get_variable_expenses(self):
        """Test get_variable_expenses."""
        exp = {
            "food": 1,
            "bills": 2,
            "transportation": 3,
            "hygien": 4,
            "clothes": 5,
            "entertainment": 6,
            "others": 7,
        }
        res = DB.get_variable_expenses("test@unit.se")
        self.assertEqual(exp, res)

    def test_get_fixed_expenses(self):
        """Test get_fixed_expenses."""
        exp = {
            "rent": 1,
            "subscription": 2,
            "insurance": 3,
            "others": 4,
        }
        res = DB.get_fixed_expenses("test@unit.se")
        self.assertEqual(exp, res)
