from src.etc.programLocation import programLocation
from src.etc.constants import ViewTextConstants
from src.controllers.settingsController import SettingsController


class SettingsView:

    @staticmethod
    def view():
        from src.controllers.lobbyController import LobbyController
        
        programLocation.setLocation(SettingsController)
        
        SettingsController.getViewTitles()

        while 1:
            command = input(ViewTextConstants.PREFIX)

            if command == "/back":
                programLocation.setLocation(LobbyController)
                LobbyController.getViewTitles()
                
                return

            SettingsController.commandStructure(command)