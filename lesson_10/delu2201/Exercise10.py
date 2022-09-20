#Nummer1
class ACLass():
    """ Parent class """
    def __init__(self, type) -> None:
        self.type = type
        print("Parent class created")
    
    def show(self):
        return print("func. AClass executed")

class BClass(ACLass):
    def __init__(self, type) -> None:
        super().__init__(type)
        print("childclass created")
    def show(self):
        return print("func. BClass executed")



obj1 = ACLass("car")
obj2 = BClass("dog")

if __name__ == '__main__':
    obj1.show()
    obj2.show()

print(type(obj1))
print(type(obj2))

#Nummer2
