from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="3380Proj_db",
    ) as connection:
        show = "SELECT * FROM PRODUCTS"
        with connection.cursor() as c:
            c.execute(show)
            result = c.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)