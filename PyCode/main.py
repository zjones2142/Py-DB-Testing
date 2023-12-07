from getpass import getpass
from mysql.connector import connect, Error

def findItem(string):
    print("Item types: {Shirt,Sock,Hat} (case sensitive)")
    type = input("Enter type: ")
    if type == "Shirt" or "Sock" or "Hat":
        string = """
        SELECT * FROM PRODUCTS AS p
        WHERE p.Prod_type = '"""+type+"'"
    else:
        print("Not a valid type.")
    return string

def viewCart(string1, string2):
    string1 = """
    SELECT PRODUCTS.Prod_name, cart_item_list.P_Qtty, cart_item_list.Price_Total
    FROM CARTS
    INNER JOIN cart_item_list ON CARTS.Cart_id = cart_item_list.Cart_id
    INNER JOIN PRODUCTS ON cart_item_list.Prod_id = PRODUCTS.Prod_id
    WHERE CARTS.User_id ='"""+string2+"'"
    return string1

def viewOrders(string1, string2):
    string1 = """
    SELECT 
        ORDERS.Order_id,
        CARTS.Ship_date AS Order_ship_date,
        PRODUCTS.Prod_name,
        cart_item_list.P_Qtty AS Quantity,
        cart_item_list.Price_Total AS Total_price
    FROM CUSTOMERS
    INNER JOIN CARTS ON CUSTOMERS.User_id = CARTS.User_id
    INNER JOIN ORDERS ON CARTS.Cart_id = ORDERS.Cart_id
    INNER JOIN cart_item_list ON CARTS.Cart_id = cart_item_list.Cart_id
    INNER JOIN PRODUCTS ON cart_item_list.Prod_id = PRODUCTS.Prod_id
    WHERE CUSTOMERS.User_id = '"""+string2+"'"
    return string1

def generalFunc(string):
    usr = input("Enter Customer ID (1 or 2 for sample data): ")
    print("What would you like to do?")
    print("""
          1 to search product list
          2 to view cart
          3 to view previous orders
            """)
    inp = input("Enter Option: ")
    if inp == '1':
        return findItem(string)
    elif inp == '2':
        return viewCart(string, usr)
    elif inp == '3':
        return viewOrders(string, usr)
    else:
        print("Not a valid input.")
    
try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="3380Proj_db",
    ) as connection:
        sCode = ""
        sCode = generalFunc(sCode)
        with connection.cursor() as c: #execute final SQL statement
            c.execute(sCode)
            print("Returned Rows From DB:")
            columns = c.description 
            result = [{columns[index][0]:column for index, column in enumerate(value)} for value in c.fetchall()]
            for row in result:
                print(row)
except Error as e:
    print(e)