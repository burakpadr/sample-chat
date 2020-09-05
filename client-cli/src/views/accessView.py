from src.controllers.accessController import AccessController


class AccessView:
    
    @staticmethod
    def view():
        while 1:
            AccessController.getViewTexts()

            selection = input("Selection -> ")

            if selection == "1":
                AccessController.loadLoginArea()
            elif selection == "2":
                AccessController.loadRegisterArea()
            elif selection == "3":
                pass
            elif selection == "4":
                exit()
