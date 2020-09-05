from src.etc.common import Common
from src.etc.constants import ViewTextConstants


class ProfileController:
    
    @staticmethod
    def getViewTitles():
        Common.clearTerminal()
        Common.printStandartText(ViewTextConstants.PROFILE_TITLE)

    @staticmethod
    def commandStructure(command):
        from src.command_structure.command import Command

        Command(ProfileController, command).handler()
        
    @staticmethod
    def clear():
        Common.clearTerminal()
        ProfileController.getViewTitles()
    