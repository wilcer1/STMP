"""Unittest for database_connection."""

import unittest
import database_connection
import mysql.connector
from mysql.connector import Error


class TestPlayerClass(unittest.TestCase):
    """Test Player Class."""

    @classmethod
    def setUpClass(cls):
        """set up acc for testing."""
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
        try:
            if cls.connection is not None and cls.connection.is_connected():
                cls.mycursor.close()
                cls.connection.close()
        except Error as e:
            print(e)

    def test_get_income(self):
        """Test get_income."""
        exp = 3
        res = database_connection.get_income("test@unit.se")
        self.assertEqual(res, exp)

    def test_get_basic_info(self):
        """Test get_basic_info."""
        exp = ("test@unit.se", "test", "test2", "test3", "N")
        res = database_connection.get_basic_info("test@unit.se")
        self.assertTrue(exp == res)

    def test_verify_login(self):
        """Test verify_login."""
        res = database_connection.verify_login("test@unit.se", "test3")
        self.assertTrue(res)

        res = database_connection.verify_login("test@unit.se", "wrong")
        self.assertFalse(res)

    def test_register_account(self):
        """Test register_account."""
