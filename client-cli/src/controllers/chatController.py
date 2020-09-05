import time
from datetime import datetime
from src.etc.common import Common
from src.connection.connection import Connection
from src.etc.programLocation import programLocation


class ChatController:

    @staticmethod
    def getViewTitles():
        Common.clearTerminal()
        Common.printStandartText(f"Chat area with {programLocation.getLocationParameters().get('chatWith')}\n")

    @staticmethod
    def entryHandler(entry):
        from src.command_structure.command import Command

        command = Command(ChatController, entry)

        if command.commandStructureCompatibility():
            command.handler()
        else:
            ChatController.__sendMessage(entry)

    @staticmethod
    def clear():
        Common.clearTerminal()
        ChatController.getViewTitles()
        ChatController.stream()

    @staticmethod
    def stream():
        response = Connection.chatRequest(
            "stream", {"chatWith": programLocation.getLocationParameters().get("chatWith")})
        successful = response.get("successful")

        if successful:
            for messageSet in response.get("stream"):
                sender = messageSet.get("sender")
                date = messageSet.get("date")
                message = messageSet.get("message")

                if sender == "__session__":
                    Common.printChatLabelText(f"<You> <{date}>: ")
                    Common.printStandartText(message)
                else:
                    Common.printChatLabelText(f"<{sender}> <{date}>: ")
                    Common.printStandartText(message)
        else:
            Common.printNegativeText(response.get("message"))

    @staticmethod
    def __sendMessage(message):
        receiver = programLocation.getLocationParameters().get("chatWith")

        response = Connection.chatRequest(
            "send-message", {"receiver": receiver, "message": message})

        if response.get("successful"):
            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            Common.printChatLabelText(f"<You> <{date}>: ")
            Common.printStandartText(message)
        else:
            Common.printNegativeText(response.get("message"))

    # Thread Functions

    @staticmethod
    def newIncomingMessages():
        chatWith = programLocation.getLocationParameters().get("chatWith")

        while programLocation.getLocation() == "ChatController" and Connection.isSession():
            response = Connection.chatRequest(
                "new-incoming-messages", {"chatWith": chatWith})

            if response.get("successful"):
                for messageSet in response.get("newIncomingMessages"):
                    sender = messageSet.get("sender")
                    date = messageSet.get("date")
                    message = messageSet.get("message")

                    Common.printChatLabelText(f"<{sender}> <{date}>: ")
                    Common.printStandartText(message)

            time.sleep(.1)
