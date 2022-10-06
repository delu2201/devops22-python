import sqlite3, csv, os
#############################################
def connection_to_db():
    """Define connection to DB"""
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    return connection, cursor

#Create DB-table and import products.
def import_products():
    """Create DB table, import products to DB, create file to store orders. """
    connection, cursor = connection_to_db()
    #Create Table
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    articleNumber INTEGER UNIQUE,
                    name TEXT,
                    price REAL,
                    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL                  
                )
                ''')
    #Check if file with products exist.
    path = input("Input path to file with products: ")
    while os.path.exists(path) == False:
        path = input("input correct filepath: ")

    #Import products to DB.
    try:
        with open(path, "r") as user_file:
            data = csv.reader(user_file)
            # skipping the first line with the column headers
            next(data, None)
            cursor.executemany("INSERT INTO products ('articleNumber', 'name', 'price') VALUES (?, ?, ?)", data)
            connection.commit()
            connection.close()
            print("Products has been successfully added.")
    except sqlite3.DatabaseError:
        print("One or more articles already exists. Article number must be unique when importing.")
    except Exception as e:
        print(e)

    # Check if orders.csv exist, else create.
    if os.path.exists("orders.csv") == False:
        with open("orders.csv", "w", newline='') as file:
            csv_writer = csv.writer(file, delimiter=",")
            csv_writer.writerow(["Time for order", "Order ID", "articleNumbers..."])

    