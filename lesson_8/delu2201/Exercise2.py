
number = input("Input an integer:")

while True:
    try:
        number = int(number)
        break
    except ValueError:
        print("Sorry, not an int")
        number = input("Input an integer:")

if number % 2 == 0:
    raise ValueError("Even number is not allowed!")
else:
    print("Thank you!")


