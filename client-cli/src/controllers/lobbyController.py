from src.etc.common import Common
from src.etc.constants import ViewTextConstants
from src.command_structure.command import Command


class LobbyController:

    @staticmethod
    def getViewTitles():
        Common.clearTerminal()
        Common.printStandartText(ViewTextConstants.LOBBY_TITLE)

    @staticmethod
    def commandStructure(command):
        Command(LobbyController, command).handler()

    @staticmethod
    def clear():
        Common.clearTerminal()
        LobbyController.getViewTitles()
