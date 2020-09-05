from src.etc.programLocation import programLocation
from src.etc.constants import ViewTextConstants
from src.controllers.notificationController import NotificationController


class NotificationView:

    @staticmethod
    def view():
        from src.controllers.lobbyController import LobbyController
        
        programLocation.setLocation(NotificationController)
        
        NotificationController.getViewTitles()

        while 1:
            command = input(ViewTextConstants.PREFIX)

            if command == "/back":
                programLocation.setLocation(LobbyController)
                LobbyController.getViewTitles()
                
                return

            NotificationController.commandStructure(command)