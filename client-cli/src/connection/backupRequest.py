import sys
import subprocess
from time import sleep
from threading import Thread
from .connection import Connection
from src.etc.common import Common
from src.etc.programLocation import programLocation
from src.sound_structure.sound import Sound


class BackupRequest:

    @staticmethod
    def handler():
        Thread(target=BackupRequest.__friendshipNotificationBackupRequest).start()
        Thread(target=BackupRequest.__userChatNotificationBackupRequest).start()

    @staticmethod
    def __friendshipNotificationBackupRequest():
        while Connection.isSession():
            notifications = Connection.notificationRequest(
                "new-incoming-friendship-notifications", {}).get("notifications")

            if notifications:
                for notificationSet in notifications:
                    # Play Sound

                    Thread(target=Sound.playNotificationSound).start()

                    # Push notification to screen by os

                    if sys.platform == "linux":
                        subprocess.Popen(
                            ["notify-send", "pychat", notificationSet.get("content")])

                    sleep(4)

            sleep(.5)

    @staticmethod
    def __userChatNotificationBackupRequest():
        while Connection.isSession():
            notifications = Connection.notificationRequest(
                "new-incoming-user-chat-notifications", {}).get("notifications")

            if notifications:
                for notificationSet in notifications:
                    # Play Sound
                    
                    location = programLocation.getLocation()
                    locationParameters = programLocation.getLocationParameters()

                    if location == "ChatController" and locationParameters.get("chatWith") == notificationSet.get("sender"):
                        Connection.notificationRequest("delete-one", {"id": notificationSet.get("id")})
                        
                        continue

                    Thread(target=Sound.playChatSound).start()

                    # Push notification to screen by os

                    if sys.platform == "linux":
                        subprocess.Popen(
                            ["notify-send", "pychat", notificationSet.get("content")])

                    sleep(4)

            sleep(.5)
