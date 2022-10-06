from product import Product
from tabulate import tabulate
from operator import itemgetter
from import_products import connection_to_db
import os
###############################################
class Cart():
    cart = []
    def __init__(self, articleNumber) -> None:
        """Method for instantiating an object"""
        self.articleNumber = articleNumber

    def __str__(self) -> str:
        """Method for printing out an object"""
        return f"Items stored in basket: {self.cart}"

    @classmethod
    def add_item(self):
        """Function to add article to cart"""
        if  os.path.exists("products.db") == False:
            print("Products are not available at this time.")
        else:
            try:
                connection, cursor = connection_to_db()
                cursor.execute("SELECT articleNumber from products")
                lst_of_articleNumber = [i[0] for i in cursor.fetchall()]
                connection.close()
            except Exception as e:
                print (e)
                
            article_to_add = "y"
            while article_to_add == "y":
                try:
                    user_input = int(input("Enter article number to add to cart: "))
                    if user_input not in lst_of_articleNumber:
                        print("Article number is not available.")
                    else: 
                        self.cart.append(user_input)
                        print()
                        self.view_cart()
                        print(f"\nArticle number: {user_input} has been added to cart.")
                        article_to_add = input("Would you like to add another article? y/n: ").strip().lower()
                    if article_to_add != "y" and article_to_add != "n":
                        article_to_add = input("please enter y or n: ").strip().lower()
                except ValueError:
                    print("Please enter a number.")
                except Exception as e:
                    print(e)
            

    @classmethod
    def view_cart(self):
        """ Function to view items in cart and display total cost"""
        if not self.cart:
            print("Your cart is empty, please add items with menu choice 3.")

        elif self.cart:    
            connection, cursor = connection_to_db()
            lst_cart = []
            for _, val in enumerate(self.cart):
                cursor.execute("SELECT articleNumber, name, price from products WHERE articleNumber=?", (val,))
                lst_cart.append(cursor.fetchone())
            
            connection.close()
            try:
                print(tabulate(lst_cart, headers=["Article", "Name", "Price"]))
            except UnboundLocalError:
                print(f"Your cart seems to be empty. Add items to cart before viewing.")
            #Get index where price is stored and calc sum of cart.
            price = list((map(itemgetter(2), lst_cart)))
            print()
            print(f"Total sum of your cart: {sum(price)}")

    @classmethod
    def remove_item(self):
        """Function to remove item from cart"""
        self.view_cart() #List cart item for user.
        if not self.cart: #pass because empty cart is catched by view_cart().
            pass
        elif self.cart:
            article_remove = "y"
            while article_remove == "y":
                try:
                    if not self.cart: #If-statement to catch if last article is removed from cart. 
                        print("\nYour cart is empty. No items to remove.")
                        break
                    else:
                        user_input = int(input("Enter article number to remove from cart: "))
                        if user_input not in self.cart:
                            print("Please enter a article number present in cart.")
                        else:
                            for val in self.cart:
                                if val == user_input:
                                    self.cart.remove(val)
                                    self.view_cart() #Shows Cart and breaks out to main menu if last item is removed.
                                    article_remove = input("Would you like to remove another item? y/n: ").strip().lower()
                        if article_remove != "y" and article_remove!= "n":
                            article_remove = input("please enter y or n: ").strip().lower()
                except ValueError:
                    print("Please enter a number.")
                except Exception as e:
                    print(e)