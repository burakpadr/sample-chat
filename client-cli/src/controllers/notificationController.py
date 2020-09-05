from src.etc.common import Common
from src.etc.constants import ViewTextConstants


class NotificationController:

    @staticmethod
    def getViewTitles():
        Common.clearTerminal()
        Common.printStandartText(ViewTextConstants.NOTIFICATION_TITLE)

    @staticmethod
    def commandStructure(command):
        from src.command_structure.command import Command

        Command(NotificationController, command).handler()
        
    @staticmethod
    def clear():
        Common.clearTerminal()
        NotificationController.getViewTitles()
