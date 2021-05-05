import unittest
import database_connection

class TestPlayerClass(unittest.TestCase):
    """Test Player Class."""
    
    def test_get_first_name(self):
        exp = "s"
        res = database_connection.get_first_name("s")
        self.assertEqual(exp, res)

    def test_get_last_name(self):
        exp = "s"
        res = database_connection.get_last_name("s")
        self.assertEqual(exp, res)

    def test_get_income(self):
        exp = 5
        res = database_connection.get_income("s")
        self.assertEqual(res, exp)

    def test_get_expenses(self):
        exp = 5
        res = database_connection.get_expenses("s")
        self.assertEqual(res, exp)

    def test_get_all_info(self):
        exp = ('s', 's', 's', 's', 5.0, 5.0)
        res = database_connection.get_all_info("s")
        self.assertTrue(exp == res)



