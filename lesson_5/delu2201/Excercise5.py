firstname = "john"
lastname = "smith"
tele = "00468123456789"

#1
print(f'{firstname}, {lastname}, {tele}')

fullname = firstname + " " + lastname
print(fullname)

print(f' {len(fullname)} {len(firstname)} {len(lastname)}')

print(f"{fullname}\n{tele}")

print(fullname + " " + tele)

print(f'{fullname} {tele}')

print('{} {}'.format(fullname,  tele))
#print(f'Ditt namn är {} och ditt nummer är {}, fullname, tele')

#2
print(fullname[:5])
print(fullname[1:-1])
print(fullname.upper()[0:-1:2])
print(fullname[::-1])
print(fullname[5:5])

#3
price_of_car = int(input("what's the cost of the car? "))

price_symbol = '${}'.format(price_of_car)

print(price_symbol)

if price_of_car > 50000:
    print("\U0001f600")
else:
    print("\U0001F923")

#4
salery = 20000
print(f"your current salary is {salery}. How much more are you asking for?")
annual_raise = int(input("Enter amount: "))
new_salary = salery + annual_raise
perc_increase = (new_salary * 100 / salery) - 100
count = 0

while count < 5:
        if count == 0:
            print(f"You asked for a {perc_increase}% increase... NO! \U0001F923")
            annual_raise = int(input("Try again!: "))
            new_salary = salery + annual_raise
            perc_increase = (new_salary * 100 / salery) - 100
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
                    new_salary = salery + annual_raise
                    perc_increase = (new_salary * 100 / salery) - 100
            break