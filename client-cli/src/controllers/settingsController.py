from src.etc.common import Common
from src.etc.constants import ViewTextConstants


class SettingsController:

    @staticmethod
    def getViewTitles():
        Common.clearTerminal()
        Common.printStandartText(ViewTextConstants.SETTINGS_TITLE)

    @staticmethod
    def commandStructure(command):
        from src.command_structure.command import Command
        
        Command(SettingsController, command).handler()
        
    @staticmethod
    def clear():
        Common.clearTerminal()
        SettingsController.getViewTitles()
