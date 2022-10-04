# from product import Product
class Cart():
    def __init__(self, id) -> None:
        self.cart = []
        self.id = id

    def __str__(self) -> str:
        """Method for printing out an object"""
        return f"Items stored in basket: {self.cart.__str__()}"

    def add_to_cart():
        user_input = int(input("Enter article number you want to add to cart: "))