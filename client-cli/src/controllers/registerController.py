from src.etc.common import Common
from src.etc.constants import ViewTextConstants
from src.forms.registerForm import RegisterForm
from src.connection.connection import Connection


class RegisterController:

    @staticmethod
    def getViewTitles():
        Common.clearTerminal()
        Common.printStandartText(ViewTextConstants.REGISTER_TITLE)

    @staticmethod
    def registerForm():
        form = RegisterForm()
        form.fillTheForm()
        
        Common.clearTerminal()

        if form.validation():
            response = Connection.registerRequest(form.getData())
            successful = response.get("successful")
            message = response.get("message")
            
            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)
        else:
            Common.printNegativeText(form.getValidationMessage())
            
        Common.programSleep()
