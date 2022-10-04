from import_products import import_products
import sqlite3, csv, sys
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
    # create an oject using certain columns from the database and print it
    for item in db_contents:
        list_of_products = Product(item[1], item[2], item[3])
        print(list_of_products)

    # if DB is empty.
    if not db_contents:
        print("The database is empty.")
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
    article_list = []
    #Iterate cart-object-list, pull articleNumber. Insert time and order-Id.
    for _, val in enumerate (cart):
        article_list.append(val.articleNumber)

    article_list.insert(0,datetime.now().strftime("%Y/%m/%d/ %H:%M:%S"))
    #Write order to file. 
    with open("orders.csv", "a", newline='') as file:
        csv_writer = csv.writer(file, delimiter=",")
        csv_writer.writerow(["Time", "Order-Id", "articleNumber"])
        csv_writer.writerow(article_list)
    #Erase purchase after ordering.
    article_list.clear()
    cart.clear()
    print("Your order has been processed. Thank you for shopping.")


def view_cart():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    lst_cart = [] 
    for _, val in enumerate(cart):
        cursor.execute("SELECT articleNumber, name, price from products WHERE articleNumber=?", (val.articleNumber,))
        lst_cart.append(cursor.fetchone())
    try:
        print(tabulate(lst_cart, headers=["Article", "Name", "Price"]))
    except UnboundLocalError:
        print(f"Your cart seems to be empty. Add items to cart before viewing.")
        main()

def add_item():
    article_to_add = "y"
    while article_to_add == "y":
        user_input = int(input("Input article number to add to cart: "))
        cart.append(Cart(user_input))
        print(f"Article number: {user_input} has been added to cart.")
        article_to_add = input("Would you like to add another article? y/n: ").strip().lower()
        if article_to_add != "y" and article_to_add != "n":
            article_to_add = input("please input y or n: ").strip().lower()


# MAIN MENU
def main():
    is_on = True
    while is_on:
        print(MAIN_MENU_TEXT +"\n")
        choice = input("""1. Load items to database.
2. List available items.
3. Add item to cart. 
4. View items in cart.
5. Remove item from cart.
6. Save order.
7. Quit shopping.\n
Input your choice: """)
        print()
        if choice == "1":
            import_products()
        if choice == "2":
            list_products()
            print()
        if choice == "3":
            add_item()
            # article_to_add = "y"
            # while article_to_add == "y":
                # user_input = int(input("Input article number to add to cart: "))
                # cart.append(Cart(user_input))
                # print(f"Article number: {user_input} has been added to cart.")
                # article_to_add = input("Would you like to add another article? y/n: ").strip().lower()
                # if article_to_add != "y" and article_to_add != "n":
                #     article_to_add = input("please input y or n: ").strip().lower()
        if choice == "4":
            view_cart()
        if choice == "5":
                user_input = int(input("Input article number to remove from cart: "))
                for i, val in enumerate(cart):
                    if val.articleNumber == user_input:
                        del cart[i]                
        if choice == "6":
            save_order()
        if choice == "7":
            sys.exit(0)

    dennis = cart
if __name__ == "__main__":
    main()

