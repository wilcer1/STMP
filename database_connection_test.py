"""Unittest for database_connection."""

import unittest
import database_connection


class TestPlayerClass(unittest.TestCase):
    """Test Player Class."""

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database."""
        database_connection.disconnect()

    def test_get_income(self):
        """Test get_income."""
        exp = 5
        res = database_connection.get_income("s")
        self.assertEqual(res, exp)

    def test_get_basic_info(self):
        """Test get_basic_info."""
        exp = ("s", "s", "s", "s", "N")
        res = database_connection.get_basic_info("s")
        self.assertTrue(exp == res)

    def test_verify_login(self):
        """Test verify_login."""
        res = database_connection.verify_login("s", "s")
        self.assertTrue(res)

        res = database_connection.verify_login("s", "ss")
        self.assertFalse(res)

    def test_register_account(self):
        """Test register_account."""
