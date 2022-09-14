def try_func(x,y):
    try:
       return x / y
    except ZeroDivisionError:
        print("Division by zero is not allowed!")
    except TypeError:
        print("y is not a number!")


try_func(4,"abc")