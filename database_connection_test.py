"""Unittest for database_connection."""

import unittest
import database_connection


class TestPlayerClass(unittest.TestCase):
    """Test Player Class."""

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database."""
        database_connection.disconnect()

    def test_get_first_name(self):
        """Test get_first_name."""
        exp = "s"
        res = database_connection.get_first_name("s")
        self.assertEqual(exp, res)

    def test_get_last_name(self):
        """Test get_last_name."""
        exp = "s"
        res = database_connection.get_last_name("s")
        self.assertEqual(exp, res)

    def test_get_income(self):
        """Test get_income."""
        exp = 5
        res = database_connection.get_income("s")
        self.assertEqual(res, exp)

    def test_get_expenses(self):
        """Test get_expenses."""
        exp = 5
        res = database_connection.get_expenses("s")
        self.assertEqual(res, exp)

    def test_get_all_info(self):
        """Test get_all_info."""
        exp = ("s", "s", "s", "s", 5.0, 5.0)
        res = database_connection.get_all_info("s")
        self.assertTrue(exp == res)

    def test_verify_login(self):
        """Test verify_login."""
        res = database_connection.verify_login("s", "s")
        self.assertTrue(res)

        res = database_connection.verify_login("s", "ss")
        self.assertFalse(res)

    def test_register_account(self):
        """Test register_account."""
