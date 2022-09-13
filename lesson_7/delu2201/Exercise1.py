#1
from lib2to3.pgen2.token import NEWLINE
from locale import delocalize

import string

def do_nothing():
    pass

do_nothing()

#2
def hello_world():
    print("Hello World")

hello_world()


def result():
    print(1 == 1.0)

result()

def reverse():
    alphabet = list(string.ascii_lowercase)
    #print(alphabet)
    a_list = sorted(alphabet, reverse = True)
    for n in range(len(a_list)):
        print(a_list[n], end = "")
        
reverse()
print(NEWLINE)
#3
def hello(name, phrase="Hello"):
    print(f'{phrase}, {name}!')

hello("Dennis")

def capital(word):
    
    print(word.upper() + "!")

capital("hej")

def printing(stop, start=1):
    for i in range(start,stop):
        print(i)
    
printing(11)