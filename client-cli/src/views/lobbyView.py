from src.connection.backupRequest import BackupRequest
from src.etc.programLocation import programLocation
from src.etc.constants import ViewTextConstants
from src.controllers.lobbyController import LobbyController


class LobbyView:
    
    @staticmethod
    def view():
        BackupRequest.handler()
        programLocation.setLocation(LobbyController)
        
        LobbyController.getViewTitles()
        
        while 1:
            command = input(ViewTextConstants.PREFIX)
            
            LobbyController.commandStructure(command) 