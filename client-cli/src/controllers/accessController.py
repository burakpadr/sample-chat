from src.etc.common import Common
from src.etc.constants import ViewTextConstants
from src.views.loginView import LoginView
from src.views.registerView import RegisterView


class AccessController:

    @staticmethod
    def getViewTexts():
        Common.clearTerminal()
        Common.printStandartText(ViewTextConstants.ACCESS_TITLE)
        Common.printStandartText(ViewTextConstants.ACCESS_SUBTITLE)

    @staticmethod
    def loadLoginArea():
        LoginView.view()
    
    @staticmethod
    def loadRegisterArea():
        RegisterView.view()