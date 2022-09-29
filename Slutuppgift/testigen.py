from classes import Basket, Product
from tabulate import tabulate
import csv, os, sys

product_list = []
def import_items():
    path = input("Enter the path to your file: ")
    
    # the empty print is just for the MENU's esthetics
    print()
    # Check if file exists.
    while os.path.isfile(path) == False:
        print("File not found, please try again.")
        path = input("Input full filepath: ")
    else:
        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=None)
                for i in reader:
                    product_list.append(i)
                print(product_list)

        except Exception as e:
            print(e)
    print(tabulate(product_list, headers="keys"))
def view_products():
    if len(product_list) == 0:
        print("No products available.")
    else:
        print(tabulate(product_list, headers="keys"))
def add_item():
    add_to_cart = input("Write product to add: ").strip().capitalize()
    if add_to_cart in product_list:
        Basket.add_item(add_to_cart)
    else:
        print("No, item available")


MAIN_MENU_TEXT = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'
"""

# MAIN MENU
def main():
    is_on = True
    while is_on:
        print(MAIN_MENU_TEXT +"\n")
        choice = input("""1. Load items to database.
2. List available items.
3. Add Item to basket. 
4. Press 4 to exit. """)
        print()
        if choice == "1":
            import_items()
        if choice == "2":
            view_products()
            print()
        if choice == "3":
            add_item()
            # item_bought = str(input("Add item to basket: "))
            
            print()
            #delete(id)
            print()
        if choice == "4":
            sys.exit(0)
    
if __name__ == "__main__":
    main()