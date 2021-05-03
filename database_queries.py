import database_connection
from account import Account

customer = Account()
customer = customer.getCustomer()

database_connection.show_account()
print(database_connection.get_first_name("lucas@gmail.com"))
print(database_connection.verify_login("lucas@gmail.com", "Lucas123"))
database_connection.disconnect()