import mysql.connector
from mysql.connector import Error


def connect():
    connection = None
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='gym',
                                        user='newuser',
                                        password='rootroot!123')
        if connection.is_connected():
            print('Connected to MySQL database')
            cursor = connection.cursor()  
            cursor.execute("SELECT * FROM customer;")
            print(cursor.fetchall())



    except Error as e:
                print(e)

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()




if __name__ == '__main__':
    connect()


    