from src.etc.programLocation import programLocation
from src.etc.constants import ViewTextConstants
from src.controllers.profileController import ProfileController


class ProfileView:

    @staticmethod
    def view():
        from src.controllers.lobbyController import LobbyController
        
        programLocation.setLocation(ProfileController)
        
        ProfileController.getViewTitles()

        while 1:
            command = input(ViewTextConstants.PREFIX)

            if command == "/back":
                programLocation.setLocation(LobbyController)
                LobbyController.getViewTitles()
                
                return

            ProfileController.commandStructure(command)
