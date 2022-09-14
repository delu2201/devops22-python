#1
import random
from re import X
def integer():
    x = random.randint(1,1000)
    return(x)

print(integer())

#2
def tup():
    x = ("x", "y")
    return(x)

print(type(tup()))
print(tup())

#3
def bool():
    x = (1 == 1.0)
    return(x)

print(type(bool()))
print(bool())

#4
def float():
    x = random.uniform(1.0, 100.0)
    return(x)

print(type(float()))
print(float())

#5
def my_name(firstname, lastname):
    x = (firstname + " " + lastname)
    return x
print(my_name("Dennis", "Lunnelid"))
#6
def rectangle(width, height):
    x = width * height
    return x

print(rectangle(5,4))
#7
def sum_list(summa):
    x = sum(summa)       
    return x

my_list_int =[2,3,5]

print(sum_list(my_list_int))
#8

def three_times(word, repeat):
    for i in range(repeat):
        print(word)

three_times("hello", 10)
