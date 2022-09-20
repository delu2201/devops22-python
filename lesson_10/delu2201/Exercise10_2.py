#Exercise2
import sys
class Animal():
    
    def __init__(self) -> None:
       
        pass
        

class Menu:
   
    MAIN_MENU_TEXT = """
    '-----------------------'
    '--------Main Menu------'
    '-----------------------'
    
    1. 'Create Object'
    2. 'Print Object'
    3. 'Delete Object'
    4. 'Exit program'
    """

    def user_input(self):
        return int(input("Enter your choice [1-4]: "))

    def create(self):
        self.my_object = Animal()
        print("You just created a horse!")
        print(f"your horse {self.my_object}")
        return self.my_object
    
    def print_obj(self):
        if not self.my_object:
            print("No Animal to display!")
        else:
            print(f'printing object {self.my_object}')

    def delete_obj(self):
        if self.my_object:
            self.my_object = None
            print("You just deleted your horse!")
        else:
            print("Nothing to delete")

    def menu_choice(self, choice):
        if choice == 4:
            sys.exit(0)
        elif choice == 3:
            self.delete_obj()
        elif choice == 1:
            self.create()
        elif choice == 2:
            self.print_obj()

    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.menu_choice(choice)

if __name__ == '__main__':
    my_object = Animal()
    Menu().menu_loop()