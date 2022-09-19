
# class Square:
    
#     def __init__(self, my_arg) -> None:
#         self.my_arg = my_arg
        
#     def area(self):
#         return self.my_arg * 2

#     def circumference(self):
#          return self.my_arg * 4

# if __name__ == '__main__':
#     my_object = Square(my_arg=5)
#     print(Square.area(my_object))    

#     my_another_object = Square(my_arg=5)
#     print(my_another_object.circumference())

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Check if year is divisible by four.
if year / 4 != 0:
    print("Not leap year")
    break
else:
    if year / 100 != 0:
        print("Leap year.")
        break
    elif year / 400 == 0:
        print("Leap year.") 