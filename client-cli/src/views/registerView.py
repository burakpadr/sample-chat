from src.controllers.registerController import RegisterController


class RegisterView:
    
    @staticmethod
    def view():
        RegisterController.getViewTitles()
        RegisterController.registerForm()