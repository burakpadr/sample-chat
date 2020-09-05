from src.controllers.loginController import LoginController


class LoginView:
    
    @staticmethod
    def view():
        LoginController.getViewTitles()
        LoginController.loginForm()