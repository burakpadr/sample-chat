from datetime import datetime
from getpass import getpass
from src.etc.common import Common
from src.views import profileView, friendshipView, notificationView, settingsView, chatView
from src.connection.connection import Connection


class CommonCommandRuntime:
    @staticmethod
    def helpCommand(**kwargs):
        from .commandConfig import CommandConfig

        controllerName = kwargs.get("controller").__name__

        commonCommands = CommandConfig.getCommonCommands()
        privateCommands = CommandConfig.getSpecialCommands(controllerName)

        for command, value in commonCommands.items():
            Common.printNotificationText(
                f"{command} -> {value.get('description')}")

        for command, value in privateCommands.items():
            Common.printNotificationText(
                f"{command} -> {value.get('description')}")

    @staticmethod
    def clearCommand(**kwargs):
        Common.clearTerminal()
        kwargs.get("controller").clear()

    @staticmethod
    def exitCommand(**kwargs):
        Connection.sessionClose()

        exit()


class SpecialCommandRuntime:

    class Lobby:

        @staticmethod
        def profile():
            profileView.ProfileView.view()

        @staticmethod
        def friendship():
            friendshipView.FriendshipView.view()

        @staticmethod
        def notifications():
            notificationView.NotificationView.view()

        @staticmethod
        def settings():
            settingsView.SettingsView.view()
            
        @staticmethod
        def chat():
            chatWith = input("Chat With (Username) -> ")

            response = Connection.chatRequest(
                "chat-permission", {"chatWith": chatWith})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                chatView.ChatView.view(chatWith)
            else:
                Common.printNegativeText(message)
        
        @staticmethod
        def deleteStream():
            chatWith = input("Username -> ")

            response = Connection.chatRequest(
                "delete-stream", {"chatWith": chatWith})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)

    class Profile:
        @staticmethod
        def whoami():
            response = Connection.profileRequest("whoami", {}).get("whoami")

            Common.printNotificationText(
                f"Username -> {response.get('username')}\nEmail -> {response.get('email')}")

        @staticmethod
        def resetUsername():
            username = input("Username -> ")

            response = Connection.profileRequest(
                "reset-username", {"username": username})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)

        @staticmethod
        def resetPassword():
            password = getpass("Password -> ")

            response = Connection.profileRequest(
                "reset-password", {"password": password})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)

        @staticmethod
        def resetEmail():
            email = input("Email -> ")

            response = Connection.profileRequest(
                "reset-email", {"email": email})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)

    class Friendship:

        @staticmethod
        def friends():
            friends = Connection.friendshipRequest(
                "friends", {}).get("friends")

            Common.printNotificationText(f"Friends: {len(friends)}")

            for friend in friends:
                Common.printNotificationText(friend)

        @staticmethod
        def incoming():
            incoming = Connection.friendshipRequest(
                "incoming", {}).get("incoming")

            Common.printNotificationText(
                f"Incoming Friendship Requests: {len(incoming)}")

            for username in incoming:
                Common.printNotificationText(username)

        @staticmethod
        def outgoing():
            outgoing = Connection.friendshipRequest(
                "outgoing", {}).get("outgoing")

            Common.printNotificationText(
                f"Ougoing Friendship Requests: {len(outgoing)}")

            for username in outgoing:
                Common.printNotificationText(username)

        @staticmethod
        def request():
            username = input("Username -> ")

            response = Connection.friendshipRequest(
                "request", {"username": username})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)

        @staticmethod
        def accept():
            username = input("Username -> ")

            response = Connection.friendshipRequest(
                "accept", {"username": username})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)

        @staticmethod
        def ignore():
            username = input("Username -> ")

            response = Connection.friendshipRequest(
                "ignore", {"username": username})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)

        @staticmethod
        def remove():
            username = input("Username -> ")

            response = Connection.friendshipRequest(
                "remove", {"username": username})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)

        @staticmethod
        def onlineList():
            pass

        @staticmethod
        def isOnline():
            pass

    class Notification:

        @staticmethod
        def read():
            response = Connection.notificationRequest("read", {})
            notifications = response.get("notifications")

            Common.printNotificationText("Notifications:\n")

            for notification in notifications:
                if notification.get("content") is None:
                    continue
                
                notificationId = notification.get("id")
                date = notification.get("date")
                content = notification.get("content")

                Common.printNotificationText(
                    f"id -> {notificationId}\ndate -> {date}\ncontent -> {content}\n")

        @staticmethod
        def deleteAll():
            response = Connection.notificationRequest("delete-all", {})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)

        @staticmethod
        def deleteOne():
            try:
                notificationId = int(input("Notification Id -> "))
            except ValueError:
                Common.printNegativeText("Notification id must be integer")

                return

            response = Connection.notificationRequest(
                "delete-one", {"id": notificationId})
            successful = response.get("successful")
            message = response.get("message")

            if successful:
                Common.printPositiveText(message)
            else:
                Common.printNegativeText(message)
