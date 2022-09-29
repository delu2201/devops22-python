from unicodedata import name


class Basket():
    def __init__(self) -> None:
        self.cart = []

    def __str__(self) -> str:
        """Method for printing out an object"""
        return f"Items stored in basket: {self.cart}"

    def add_item(self, item):
        self.cart.append(item)
