from multiprocessing.spawn import import_main_path
from add_products import import_items
from list_products import list_products


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
            list_products()
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