"""Unitest for budget class."""

from budget import Budget
import unittest


class test_budget_class(unittest.TestCase):
    """Test budget class."""

    def setUp(self) -> None:
        """Set up an instance of budget for testing."""
        self.budget = Budget()
        self.budget.set_budget(10, {"test": 1}, {"test2": 2})
        return super().setUp()

    def tearDown(self) -> None:
        """Delete the instance."""
        del self.budget
        return super().tearDown()

    def test_init(self):
        """Test the constructor."""
        exp = Budget
        res = self.budget
        self.assertIsInstance(res, exp)

        exp = 10
        res = self.budget.income
        self.assertEqual(res, exp)

        exp = dict
        res = self.budget.variable_expenses
        self.assertIsInstance(res, exp)
        res = self.budget.fixed_expenses
        self.assertIsInstance(res, exp)

    def test_set_budget(self):
        """Test set budget values."""
        self.budget.set_budget(15, {"test": 5}, {"test2": 7})
        exp = 15
        res = self.budget.income
        self.assertEqual(exp, res)

        exp = 5
        res = self.budget.variable_expenses["test"]
        self.assertEqual(exp, res)

        exp = 7
        res = self.budget.fixed_expenses["test2"]
        self.assertEqual(exp, res)

    def test_get_expenses(self):
        """Test get_expenses."""
        exp = "2"
        res1, res2 = self.budget.get_expenses()
        self.assertEqual(res1, exp)
        exp = "1"
        self.assertEqual(res2, exp)

    def test_get_total_expenses(self):
        """Test get_total_expenses."""
        exp = 3
        res = self.budget.get_total_expenses()
        self.assertEqual(exp, res)


if __name__ == '__main__':
    unittest.main()
