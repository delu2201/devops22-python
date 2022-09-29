import sqlite3
from product import Product
import csv

def import_products():
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    articleNumber INTEGER UNIQUE,
                    name TEXT,
                    price REAL,
                    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL                  
                )
                ''')
    path = "items.csv"

    try:
        with open(path, "r") as user_file:
            data = csv.reader(user_file)
            # skipping the first line with the column headers
            next(data, None)
            cursor.executemany("INSERT INTO products ('articleNumber', 'name', 'price') VALUES (?, ?, ?)", data)
            connection.commit()
            connection.close()
    except Exception as e:
        print(e)

print("Products has been successfully added.")