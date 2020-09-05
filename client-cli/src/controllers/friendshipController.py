from src.etc.common import Common
from src.etc.constants import ViewTextConstants


class FriendshipController:

    @staticmethod
    def getViewTitles():
        Common.clearTerminal()
        Common.printStandartText(ViewTextConstants.FRIENDSHIP_TITLE)

    @staticmethod
    def commandStructure(command):
        from src.command_structure.command import Command

        Command(FriendshipController, command).handler()

    @staticmethod
    def clear():
        Common.clearTerminal()
        FriendshipController.getViewTitles()
