class Product():

    def __init__(self, articleId, name, price) -> None:
        self.articleId = articleId
        self.name = name
        self.price = price
        
        pass

    def __str__(self):
      # what it says when an object is printed
        return f"Product: {self.articleId}  Name: {self.name} Price:  {self.price}"