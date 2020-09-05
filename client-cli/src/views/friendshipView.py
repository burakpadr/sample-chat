from src.etc.programLocation import programLocation
from src.etc.constants import ViewTextConstants
from src.controllers.friendshipController import FriendshipController


class FriendshipView:
    
    @staticmethod
    def view():
        from src.controllers.lobbyController import LobbyController
        
        programLocation.setLocation(FriendshipController)
        
        FriendshipController.getViewTitles()
        
        while 1:
            command = input(ViewTextConstants.PREFIX)
            
            if command == "/back":
                programLocation.setLocation(LobbyController)
                LobbyController.getViewTitles()
                
                return

            FriendshipController.commandStructure(command)