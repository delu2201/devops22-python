from cart import Cart
import sqlite3
from product import Product

cart = Cart()
list_of_items= []
def list_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from products")
    db_contents = cursor.fetchall()
    for item in db_contents:
        # create an oject using certain columns from the database and print it
        list_of_products = Product(item[1], item[2], item[3])
        print(list_of_products)

    # if no info in the database
    if not db_contents:
        print("The database is empty")
        print()
        print('Start with uploading data or choose exit the program')
        print()
        connection.close()


    

