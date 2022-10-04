from product import Product
from tabulate import tabulate
from operator import itemgetter
from import_products import connection_to_db
class Cart():
    cart = []
    def __init__(self, articleNumber) -> None:
        self.articleNumber = articleNumber

    def __str__(self) -> str:
        """Method for printing out an object"""
        return f"Items stored in basket: {self.cart}"

    @classmethod
    def add_item(self):
            """Function to add article to cart"""
        
            connection, cursor = connection_to_db()
            cursor.execute("SELECT articleNumber from products")
            lst_of_articleNumber = [i[0] for i in cursor.fetchall()]

            article_to_add = "y"
            while article_to_add == "y":
                try:
                    user_input = int(input("Input article number to add to cart: "))
                    if user_input not in lst_of_articleNumber:
                        print("Article number is not available.")
                    else: 
                        self.cart.append(user_input)
                        print(f"Article number: {user_input} has been added to cart.")
                        print(self.cart)
                        article_to_add = input("Would you like to add another article? y/n: ").strip().lower()
                    if article_to_add != "y" and article_to_add != "n":
                        article_to_add = input("please input y or n: ").strip().lower()
                except ValueError:
                    print("Please input a number.")
                except Exception as e:
                    print(e)
            connection.close()

    @classmethod
    def view_cart(self):
        """ Function to view items in cart and display total cost"""
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
        """Fuction to remove item from cart"""
        try:
            user_input = int(input("Input article number to remove from cart: "))
            for _, val in enumerate(self.cart):
                if val == user_input:
                    self.cart.remove(val)
        except ValueError:
                print("Please input a number.")
        except Exception as e:
            print(e)