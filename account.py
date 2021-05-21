"""Singleton account class."""
from budget import Budget


class Account:
    """Singleton account class."""

    __instance = None

    @staticmethod
    def getInstance():
        """Get instance of class."""
        if Account.__instance is None:
            Account()

        return Account.__instance

    def __init__(self):
        """Virtually private constructor."""
        if Account.__instance is not None:
            raise Exception("This class is a Account!")
        else:
            Account.__instance = self
            self.email = None
            self.first_name = None
            self.last_name = None
            self.password = None
            self.budget = Budget()

    def set_customer(self, details):
        """Set the customer attributes."""
        self.email = details[0]
        self.first_name = details[1]
        self.last_name = details[2]
        self.password = details[3]

    def log_out(self):
        """Remove the instance."""
        Account.__instance = None
