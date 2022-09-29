import sqlite3, csv, os, classes
from classes import Basket
from tabulate import tabulate

def import_items():
    connection = sqlite3.connect("groceries.db")
    cursor = connection.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS groceries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    item TEXT UNIQE,
                    price REAL,
                    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL                  
                )
                ''')
    #Request filepath.
    path = input("Enter the path to your file: ")
    
    # the empty print is just for the MENU's esthetics
    print()
    
    # Check if file exists.
    while os.path.isfile(path) == False:
        print("File not found, please try again.")
        path = input("Input full filepath: ")
    else:
        try:
            with open(path, "r") as user_file:
                data = csv.reader(user_file)
                # skipping the first line with the column headers
                next(data, None)
                cursor.executemany("INSERT INTO groceries ('item', 'count') VALUES (?, ?)", data,)
                connection.commit()
        except FileNotFoundError:
                print("File not found, please try again.")
    connection.close()

def single_item():
        connection = sqlite3.connect("groceries.db")
        cursor = connection.cursor()
        cursor.execute("SELECT item from groceries")
        db_content = cursor.fetchall()
        item = input("Write which item to store: ").strip().capitalize()
        list_of_items = []
        for i in db_content:
            list_of_items.extend(i)
        while item in list_of_items:
                item = input("Item already in store. Please input another item: ").strip().capitalize()
        else: 
            cursor.execute("INSERT INTO groceries ('item') VALUES (?)", (item,))
            connection.commit()
            connection.close()
            print()
            print(f'Item "{item}" has been added to the store.')

def list_items():
    connection = sqlite3.connect("groceries.db")
    cursor = connection.cursor()

    cursor.execute("SELECT item from groceries ORDER BY item")
    db_contents = cursor.fetchall()
    print(db_contents)
    print("Available items in store.")
    print(tabulate(db_contents))
    pass

def add_item():
    
    print
    pass

def remove_item():
    pass



