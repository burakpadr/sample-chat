from .commandRuntime import CommonCommandRuntime, SpecialCommandRuntime


class CommandConfig:

    __COMMON_COMMANDS = {
        "/help": {
            "description": "Shows the usable commands",
            "function": CommonCommandRuntime.helpCommand
        },
        "/clear": {
            "description": "Clear the terminal",
            "function": CommonCommandRuntime.clearCommand
        },
        "/exit": {
            "description": "Exit from the app",
            "function": CommonCommandRuntime.exitCommand
        }
    }

    __SPECIAL_COMMANDS = {
        "LobbyController": {
            "/profile": {
                "description": "Go to the profile area",
                "function": SpecialCommandRuntime.Lobby.profile
            },
            "/friendship": {
                "description": "Go to the friendship area",
                "function": SpecialCommandRuntime.Lobby.friendship
            },
            "/notifications": {
                "description": "Go to the notification area",
                "function": SpecialCommandRuntime.Lobby.notifications
            },
            "/settings": {
                "description": "Go to the settings area",
                "function": SpecialCommandRuntime.Lobby.settings
            },
            "/chat": {
                "description": "Chat your friend",
                "function": SpecialCommandRuntime.Lobby.chat
            },
            "/delete-stream": {
                "description": "Delete the chat you had with your friend",
                "function": SpecialCommandRuntime.Lobby.deleteStream
            }
        },
        "ProfileController": {
            "/back": {
                "description": "Turn back",
            },
            "/whoami": {
                "description": "Shows your account details",
                "function": SpecialCommandRuntime.Profile.whoami
            },
            "/reset-username": {
                "description": "Change the username",
                "function": SpecialCommandRuntime.Profile.resetUsername
            },
            "/reset-password": {
                "description": "Change the password",
                "function": SpecialCommandRuntime.Profile.resetPassword
            },
            "/reset-email": {
                "description": "Change the email address",
                "function": SpecialCommandRuntime.Profile.resetEmail
            }
        },
        "ChatController": {
            "/back": {
                "description": "Turn back"
            }
        },
        "FriendshipController": {
            "/back": {
                "description": "Turn back"
            },
            "/friends": {
                "description": "Shows your friendships",
                "function": SpecialCommandRuntime.Friendship.friends
            },
            "/incoming": {
                "description": "Shows your incoming friendship requests",
                "function": SpecialCommandRuntime.Friendship.incoming
            },
            "/outgoing": {
                "description": "Shows your outgoing friendship requests",
                "function": SpecialCommandRuntime.Friendship.outgoing
            },
            "/request": {
                "description": "Send friendship request",
                "function": SpecialCommandRuntime.Friendship.request
            },
            "/accept": {
                "description": "Accept incoming friendship request",
                "function": SpecialCommandRuntime.Friendship.accept
            },
            "/ignore": {
                "description": "Ignore incoming friendship request",
                "function": SpecialCommandRuntime.Friendship.ignore
            },
            "/remove": {
                "description": "Remove your friend from your frienship list",
                "function": SpecialCommandRuntime.Friendship.remove
            },
            "/online-list": {
                "description": "Shows your online friends",
                "function": SpecialCommandRuntime.Friendship.onlineList
            },
            "/is-online": {
                "description": "Shows your friend's online status",
                "function": SpecialCommandRuntime.Friendship.isOnline
            },
        },
        "NotificationController": {
            "/back": {
                "description": "Turn back"
            },
            "/read": {
                "description": "Shows all notifications",
                "function": SpecialCommandRuntime.Notification.read
            },
            "/delete-all": {
                "description": "Delete all notifications",
                "function": SpecialCommandRuntime.Notification.deleteAll
            },
            "/delete-one": {
                "description": "Delete one notification",
                "function": SpecialCommandRuntime.Notification.deleteOne
            }
        }
    }

    @staticmethod
    def insideTheCommonCommands(command):
        return CommandConfig.__COMMON_COMMANDS.__contains__(command)

    @staticmethod
    def insideTheSpecialCommands(controller, command):
        controllerName = controller.__name__

        return CommandConfig.__SPECIAL_COMMANDS.get(controllerName).__contains__(command)

    @staticmethod
    def getCommonCommands():
        return CommandConfig.__COMMON_COMMANDS

    @staticmethod
    def getSpecialCommands(controllerName):
        return CommandConfig.__SPECIAL_COMMANDS.get(controllerName)
