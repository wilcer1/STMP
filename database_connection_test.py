"""Unittest for self.DB."""

import unittest
from database_connection import database_connection as DB
import mysql.connector
from mysql.connector import Error


class test_database_connection_class(unittest.TestCase):
    """Test database_connection class."""

    @classmethod
    def setUpClass(cls):
        """Set up account for testing."""
        try:
            # Connect to the self.db
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

        cls.DB = DB()

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database and delete test account."""
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

    def test_init(self):
        """Test constructor."""
        exp = DB
        res = self.DB
        self.assertIsInstance(res, exp)

    def test_get_income(self):
        """Test get_income."""
        exp = 3
        res = self.DB.get_income("test@unit.se")
        self.assertEqual(res, exp)

    def test_update_income(self):
        """Test update_income."""
        exp = 100
        self.DB.update_income(100, "test@unit.se")
        res = self.DB.get_income("test@unit.se")
        self.assertEqual(res, exp)

    def test_set_variable_expenses(self):
        """Test set_variable_expenses."""
        sql = "DELETE FROM variable_expenses WHERE budget_account_email = 'test@unit.se';"
        self.mycursor.execute(sql)
        self.connection.commit()
        variable_expenses = {
            "food": 7,
            "bills": 6,
            "transportation": 5,
            "hygien": 4,
            "clothes": 3,
            "entertainment": 2,
            "others": 1,
        }

        exp = variable_expenses
        self.DB.set_variable_expenses("test@unit.se", variable_expenses)
        res = self.DB.get_variable_expenses("test@unit.se")
        self.assertEqual(res, exp)
        exp = {
            "food": 7,
            "bills": 6,
            "transportation": 7,
            "hygien": 2,
            "clothes": 6,
            "entertainment": 4,
            "others": 5,
        }
        self.assertNotEqual(res, exp)

    def test_set_fixed_expenses(self):
        """Test set_fixed_expenses."""
        sql = "DELETE FROM fixed_expenses WHERE budget_account_email = 'test@unit.se';"
        self.mycursor.execute(sql)
        self.connection.commit()

        fixed_expenses = {
            "rent": 4,
            "subscription": 3,
            "insurance": 2,
            "others": 1
        }

        exp = fixed_expenses
        self.DB.set_fixed_expenses("test@unit.se", fixed_expenses)
        res = self.DB.get_fixed_expenses("test@unit.se")
        self.assertEqual(exp, res)
        res = {
            "rent": 1,
            "subscription": 1,
            "insurance": 2,
            "others": 1
        }
        self.assertNotEqual(exp, res)

    def test_update_fixed_expenses(self):
        """Test update_fixed_expenses."""
        fixed_expenses = {
            "rent": 4,
            "subscription": 3,
            "insurance": 2,
            "others": 1
        }

        exp = fixed_expenses
        self.DB.update_fixed_expenses("test@unit.se", fixed_expenses)
        res = self.DB.get_fixed_expenses("test@unit.se")
        self.assertEqual(exp, res)

        res = {
            "rent": 1,
            "subscription": 1,
            "insurance": 2,
            "others": 1
        }
        self.assertNotEqual(exp, res)

    def test_update_variable_expenses(self):
        """Test update_variable_expenses."""
        variable_expenses = {
            "food": 7,
            "bills": 6,
            "transportation": 5,
            "hygien": 4,
            "clothes": 3,
            "entertainment": 2,
            "others": 1,
        }

        exp = variable_expenses
        self.DB.update_variable_expenses("test@unit.se", variable_expenses)
        res = self.DB.get_variable_expenses("test@unit.se")
        self.assertEqual(res, exp)
        exp = {
            "food": 7,
            "bills": 6,
            "transportation": 7,
            "hygien": 2,
            "clothes": 6,
            "entertainment": 4,
            "others": 5,
        }
        self.assertNotEqual(res, exp)

    def test_get_basic_info(self):
        """Test get_basic_info."""
        exp = ("test@unit.se", "test", "test2", "test3", "N")
        res = self.DB.get_basic_info("test@unit.se")
        self.assertTrue(exp == res)

    def test_verify_login(self):
        """Test verify_login."""
        res = self.DB.verify_login("test@unit.se", "test3")
        self.assertTrue(res)

        res = self.DB.verify_login("test@unit.se", "wrong")
        self.assertFalse(res)

    def test_register_account(self):
        """Test register_account."""
        res = self.DB.register_account("test@unit.se")
        self.assertFalse(res)

    def test_check_email(self):
        """Test check_email method."""
        self.assertTrue(self.DB.check_email("test@unit.se"))
        self.assertFalse(self.DB.check_email("s"))

    def test_new_customer(self):
        """Test new_customer function."""
        res = self.DB.new_customer("test@unit.se")
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
        res = self.DB.get_variable_expenses("test@unit.se")
        self.assertEqual(exp, res)

    def test_get_fixed_expenses(self):
        """Test get_fixed_expenses."""
        exp = {
            "rent": 1,
            "subscription": 2,
            "insurance": 3,
            "others": 4,
        }
        res = self.DB.get_fixed_expenses("test@unit.se")
        self.assertEqual(exp, res)

    def test_check_details(self):
        """Test check_details."""
        res = self.DB.check_details("test.23@unit.se", "Test", "User")
        self.assertTrue(res)
        res = self.DB.check_details("test.23@unit.s2", "123", "Us23")
        self.assertFalse(res)

    def test_get_buffert(self):
        """Test get_buffert."""
        exp = 2
        res = self.DB.get_buffert("test@unit.se")
        self.assertEqual(exp, res)
        exp = 5
        self.assertNotEqual(exp, res)

    def test_get_saving_goal(self):
        """Test get_saving_goal."""
        exp = 1
        res = self.DB.get_saving_goal("test@unit.se")
        self.assertEqual(exp, res)
        exp = 5
        self.assertNotEqual(exp, res)

    def test_update_buffert(self):
        """Test update_buffert."""
        exp = 3
        self.DB.update_buffert("test@unit.se", 3)
        res = self.DB.get_buffert("test@unit.se")
        self.assertEqual(exp, res)

    def test_update_saving_goal(self):
        """Test update_saving_goal."""
        exp = 4
        self.DB.update_saving_goal("test@unit.se", 4)
        res = self.DB.get_saving_goal("test@unit.se")
        self.assertEqual(exp, res)


if __name__ == '__main__':

    unittest.main()
