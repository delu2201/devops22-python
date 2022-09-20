
#Excercise 1 & 2
class Animal:
    def __init__(self, type) -> None:
        self.type = type
        pass

class Dog(Animal):
    def __init__(self, type, breed, height) -> None:
        super().__init__(type)
        self.breed = breed
        self.height = height
        pass

class Supermarket:
    def __init__(self, brand, location, size) -> None:
        self.brand = brand
        self.location = location
        self.size = size
        pass
    

class Coop:
    def __init__(self, location, size, employees, earnings) -> None:
        self.location = location
        self.size = size
        self.employees = employees
        self.earnings = earnings
        pass
#Exercise 3  
class Square:
    def __init__(self, side) -> None:
        self.side = side
        
    def area(self):
        return float(self.side ** 2)

    def circumference(self):
         return self.side * 4.0

if __name__ == '__main__':
    my_object = Square(side=2)
    print(f'Uträkningen för första objektet är:')
    print(Square.area(my_object))
    print(my_object.circumference())

    print("Uträkningen för andra objektet är:")
    my_another_object = Square(side=3.5)
    print(Square.area(my_another_object))
    print(my_another_object.circumference())

#Exercise4
from cgitb import grey
from email.policy import default
from math import pi
from turtle import circle, color

class Circle:
    """Class circle for holding user created circles"""
    #Class Variable
    #color = "grey"
    #Data members
    def __init__(self, diagonal, color = "grey") -> None:
        self.diagonal = diagonal
        self.color = color
        self.area = self.calc_area
        self.circumference = self.calc_circumference

    #instance methods    
    def calc_area(self):
        result_area = pi * self.diagonal**2
        return result_area
    
    def calc_circumference(self):
        result_circ = pi * self.diagonal
        return result_circ
    
    def set_color(self, color):
        self.color = color #input("change color:")
    
    def show(self):
        print("Diag:", self.diagonal, "Color:", self.color)

    
# create two objects of Class Circle"
s1 = Circle(3)
s2 = Circle(2)
test_data_area = 2
test_data_circ = 3

if __name__ == '__main__':
    my_class = Circle(diagonal=2)
    circular_area = Circle(test_data_area)
    print(Circle.area(circular_area))

    circ = Circle(test_data_circ)
    print(Circle.circumference(circ))
    print(Circle.circumference(s1))
# call instance methods in class Circle. 
s1.show()
s1.set_color("blue")
s1.show()
s2.show()
print(s1.circumference())