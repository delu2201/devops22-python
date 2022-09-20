# #Inheritance

# from ast import Add


# class Person():
#     def __init__(self, adress) -> None:
#         self.adress = adress
#         pass

# class Employee(Person):
#     def __init__(self, adress, employee_nr, salary) -> None:
#         super().__init__(adress)
#         self.emp_number = employee_nr
#         self.salary = salary
#         pass

# person_1 = Person(adress=("Bygatan", 15, 17149, "Sweden"))

# if __name__ == '__main__':
#     print(person_1.adress)

# Composition

class Address():
    def __init__(self, address) -> None:
        self.address = address
        pass
    def get_adress(self):
        return self.address

class Employee():
    def __init__(self, emp_nr, salary) -> None:
        self.obj1 = Address()
        self.emp_nr = emp_nr
        self.salary = salary
    
    def get_m2(self):
        self.obj1.get_adress()
        pass

#obj_address = Address(address=("Bygatan", 15, 17149, "Sweden"))

#emp = Employee(127, 3000)

if __name__ == '__main__':
    obj3 = Address(address=("Bygatan", 15, 17149, "Sweden"))
    emp = Employee(127, 3000)
    obj2 = Employee(emp_nr=127, salary=3000)
    obj2.get_m2()
