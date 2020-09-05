from src.etc.common import Common
from src.etc.constants import ViewTextConstants
from src.forms.loginForm import LoginForm
from src.connection.connection import Connection
from src.views.lobbyView import LobbyView


class LoginController:

    @staticmethod
    def getViewTitles():
        Common.clearTerminal()
        Common.printStandartText(ViewTextConstants.LOGIN_TITLE)

    @staticmethod
    def loginForm():
        form = LoginForm()
        form.fillTheForm()
        
        Common.clearTerminal()

        if form.validation():
            response = Connection.loginRequest(form.getData())
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
                Common.programSleep()
                
                LobbyView.view()
            else:
                Common.printNegativeText(message)
        else:
            Common.printNegativeText(form.getValidationMessage())

        Common.programSleep()
