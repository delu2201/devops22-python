class Product():

    def __init__(self, articleNumber, name, price) -> None:
        self.articleNumber = articleNumber
        self.name = name
        self.price = price
        
        pass

    def __str__(self):
      # what it says when an object is printed
        return f"Product: {self.articleNumber}  Name: {self.name} Price:  {self.price}"