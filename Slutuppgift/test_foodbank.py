#Import neccessary Modules
import sqlite3, csv, sys
from typing import List
from classes import Basket
from test_functions import import_items, list_items

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
            list_items()
            print()
        if choice == "3":
            list_items()
            # item_bought = str(input("Add item to basket: "))
            
            print()
            #delete(id)
            print()
        if choice == "4":
            sys.exit(0)
    


if __name__ == "__main__":
    main()


