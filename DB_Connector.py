import mysql.connector
from mysql.connector import Error


def connect():
    database = None
    try:
        database = mysql.connector.connect(host='localhost',
                                        database='NAMNET PÅ DATABASEN',
                                        user='root',
                                        password='LÖSENORD')
        if database.is_connected():
            print('Connected to MySQL database')

    except Error as e:
                print(e)

    finally:
        if database is not None and database.is_connected():
            database.close()


if __name__ == '__main__':
    connect()