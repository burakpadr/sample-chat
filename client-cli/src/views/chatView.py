from threading import Thread
from src.etc.programLocation import programLocation
from src.etc.common import Common
from src.controllers.chatController import ChatController


class ChatView:

    @staticmethod
    def view(chatWith):
        from src.controllers.lobbyController import LobbyController
        
        programLocation.setLocation(ChatController)
        programLocation.setLocationParameters(chatWith=chatWith)

        ChatController.getViewTitles()
        ChatController.stream()
        
        Thread(target=ChatController.newIncomingMessages).start()

        while 1:
            entry = input()
            
            if entry == "/back":
                programLocation.setLocation(LobbyController) 
                programLocation.setLocationParameters()
                LobbyController.getViewTitles()
                
                return

            ChatController.entryHandler(entry)
