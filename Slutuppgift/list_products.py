import sqlite3
from product import Product
def list_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from products")
    db_contents = cursor.fetchall()
    for item in db_contents:
        # create an oject using certain columns from the database and print it
        print(Product(item[1], item[2], item[3]))

    # if no info in the database
    if not db_contents:
        print("The database is empty")
        print()
        print('Start with uploading data or choose exit the program')
        print()
        connection.close()