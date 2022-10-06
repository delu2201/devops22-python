from import_products import import_products, connection_to_db
import csv, sys, os
from cart import Cart
from datetime import datetime
from product import Product
###########################################################
OrderId = 1
def list_products():
    """Listing available products in stock"""
    if os.path.exists("products.db") == False:
        print("No available items at this time.\nPlease import items with menu choice 1.")
    else:
        connection, cursor = connection_to_db()
        cursor.execute("SELECT * from products")
        db_contents = cursor.fetchall()
        # create an oject using certain columns from the database and print it
        for item in db_contents:
            list_of_products = Product(item[1], item[2], item[3])
            print(list_of_products)
        connection.close()
     
def save_order():
    """Saving order to DB and clearing cart after processing"""
    if not Cart.cart:
        print("The cart is empty, please add items before saving order.")
    else:
        Cart.view_cart()
        user_input = "g"
        while user_input != "y" and user_input != "n":
            user_input = input('would you like to order the above items?\nEnter "y" to order or "n" to go back to main menu. y/n? ').strip().lower()
            if user_input == "n":
                main()
            elif user_input == "y":
                article_list = []
                #Iterate cart-object-list, pull articleNumber.Sort/Insert time and OrderId.
                for i in range(len(Cart.cart)):
                    article_list.append(Cart.cart[i])

                article_list.sort()
                article_list.insert(0,datetime.now().strftime("%Y/%m/%d/ %H:%M:%S"))
                article_list.insert(1,"OrderId:" +str(OrderId))
                #Write order to file.
                with open("orders.csv", "a") as file:
                    csv_writer = csv.writer(file, delimiter=",")
                    csv_writer.writerow(article_list)
                #Erase purchase after ordering.
                article_list.clear()
                Cart.cart.clear()
                increment()
                print("\nYour order has been processed. Thank you for shopping.")

def increment():
    """Increment OrderId when saving orders"""
    global OrderId
    OrderId +=1

def quit_program():
    """Quit program, check that cart is empty before quitting"""
    if not Cart.cart:
        sys.exit(0)
    else:
        q = "g"
        while q != "y" and q != "n":
            q = input("You have a ongoing order. Do you still want to quit? y/n: ").strip().lower()
            if q == "y":
                sys.exit(0)
            if q == "n":
                main()


MAIN_MENU_TEXT = """
'-------------------------'
'----- "Express shop" ----'
'-------------------------'
"""
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
            Cart.add_item()
        if choice == "4":
            Cart.view_cart()
        if choice == "5":
            Cart.remove_item()            
        if choice == "6":
            save_order()
        if choice == "7":
            quit_program()
            
if __name__ == "__main__":
    main()

