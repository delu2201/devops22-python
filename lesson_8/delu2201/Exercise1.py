import random

def try_float(my_float):
    try:
        float(my_float)
    except ValueError:
        print("Something went wrong")

try_float("abc")