
#4

salary = 20000
print(f"your current salary is {salary}. How much more are you asking for?")
annual_raise = int(input("Enter amount: "))
new_salary = salary + annual_raise
perc_increase = (new_salary * 100 / salary) - 100
count = 0

while count < 5:
        if count == 0:
            print(f"You asked for a {perc_increase}% increase... NO! \U0001F923")
            annual_raise = int(input("Try again!: "))
            new_salary = salary + annual_raise
            perc_increase = (new_salary * 100 / salary) - 100
            count = count + 1
        else:
            for i in range(4):
                count = count + 1
                if perc_increase <= 5:
                    print(f"Sure, you'll get {new_salary}!")
                    break
                else:    
                    print(f"You asked for a {perc_increase}% increase... FUCK NO! \U0001F923")
                    annual_raise = int(input("Try again!: "))
                    new_salary = salary + annual_raise
                    perc_increase = (new_salary * 100 / salary) - 100
            print("These negotiations are going nowhere, BYE!")
            break

#Jag är här för dig Dennis!! <3
#Du lär dig dag för dag min vän! If else we trust!