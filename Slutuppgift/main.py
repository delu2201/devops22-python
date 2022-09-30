from sre_constants import CATEGORY_NOT_SPACE
from import_products import import_products
import sqlite3, csv
from datetime import datetime
from product import Product
from tabulate import tabulate

MAIN_MENU_TEXT = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'
"""

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

cart = []

class Cart():

    def __init__(self, articleNumber) -> None:
        self.articleNumber = articleNumber

    def __str__(self) -> str:
        """Method for printing out an object"""
        return f"Items stored in basket: {cart}"

def save_order():
    order_id = 1    #Create order-Id
    article_list = [] 
    #Iterate cart-object-list, pull articleNumber. Insert time and order-Id.
    for _, val in enumerate (cart):
        article_list.append(val.articleNumber)

    article_list.insert(0,datetime.now().strftime("%Y/%m/%d/ %H:%M:%S"))
    article_list.insert(1, order_id)
    order_id += 1
    #Write order to file. 
    with open("orders.csv", "w+", newline='') as file:
        csv_writer = csv.writer(file, delimiter=",")
        csv_writer.writerow(["Time", "Order-Id", "articleNumber"])
        csv_writer.writerow(article_list)
    #Erase purchase after ordering.
    article_list = None
    cart = None

# MAIN MENU
def main():
    is_on = True
    while is_on:
        print(MAIN_MENU_TEXT +"\n")
        choice = input("""1. Load items to database.
2. List available items.
3. Add item to cart. 
4. Remove item from cart.
5. Save order.""")
        print()
        if choice == "1":
            import_products()
        if choice == "2":
            list_products()
            print()
        if choice == "3":
            user_input = int(input("artikelnummer: "))
            cart.append(Cart(user_input))
        if choice == "4":
            user_input = int(input("Remove artikelnummer: "))
            for i, val in enumerate(cart):
                if val.articleNumber == user_input:
                    del cart[i]
        if choice == "5":
            save_order()

    dennis = cart
if __name__ == "__main__":
    main()

