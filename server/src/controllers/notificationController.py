import json
from datetime import datetime
from operator import itemgetter
from flask import request, jsonify, session
from src.etc.constants import ControllerTextConstants, OtherConstants
from .controller import Controller
from src.models.friendshipNotificationModel import FriendshipNotification
from src.models.userChatNotificationModel import UserChatNotification


class NotificationController(Controller):

    def __init__(self):
        super().__init__(self)

    class Post:

        def __init__(self):
            data = request.get_json()

            self.__action = data.get("action")
            self.__parameters = json.loads(data.get("parameters"))

        def handler(self):
            if not bool(session):
                return jsonify(None)

            if self.__action == "new-incoming-friendship-notifications":
                return self.__newIncomingFriendshipNotifications()
            elif self.__action == "new-incoming-user-chat-notifications":
                return self.__newIncomingUserChatNotifications()
            elif self.__action == "read":
                return self.__read()
            elif self.__action == "delete-all":
                return self.__deleteAll()
            elif self.__action == "delete-one":
                return self.__deleteOne()
            else:
                return jsonify(None)

        @staticmethod
        def __newIncomingFriendshipNotifications():
            notifications = []

            for notificationSet in FriendshipNotification(username=session.get("username")).read():
                if not notificationSet.get("isRead"):
                    notifications.append(notificationSet)

                    FriendshipNotification(
                        id=notificationSet.get("id")).update(isRead=True)

            return jsonify(notifications=notifications)

        @staticmethod
        def __newIncomingUserChatNotifications():
            notifications = []

            for notificationSet in UserChatNotification(username=session.get("username")).read():
                if not notificationSet.get("isRead"):
                    notifications.append(notificationSet)

                    UserChatNotification(
                        sender=notificationSet.get("sender")).update(isRead=True)

            return jsonify(notifications=notifications)

        def __read(self):
            friendshipNotifications = FriendshipNotification(
                username=session.get("username")).read()
            userChatNotifications = UserChatNotification(
                username=session.get("username")).read()

            notifications = friendshipNotifications + userChatNotifications

            for notification in friendshipNotifications:
                FriendshipNotification(
                    id=notification.get("id")).update(isRead=True)

            for notification in userChatNotifications:
                UserChatNotification(
                    sender=notification.get("sender")).update(isRead=True)

            notifications = sorted(notifications, key=lambda k: datetime.strptime(
                k["date"], OtherConstants.DATE_FORMAT), reverse=True)

            return jsonify(notifications=notifications)

        def __deleteAll(self):
            deletedCount = FriendshipNotification(
                username=session.get("username")).delete().deleted_count

            UserChatNotification(username=session.get(
                "username")).update(content=None)

            if deletedCount == 0:
                return jsonify(successful=False, message=ControllerTextConstants.NOTIFICATION_DELETE_ALL_ERR)

            return jsonify(successful=True, message=ControllerTextConstants.NOTIFICATION_DELETE_ALL_SUCCESSFUL)

        def __deleteOne(self):
            notificationId = self.__parameters.get("id")

            deletedCount = FriendshipNotification(username=session.get(
                "username"), id=notificationId).delete().deleted_count

            if deletedCount == 0:
                if not UserChatNotification(username=session.get("username"), id=notificationId).update(content=None).matched_count == 0:
                    return jsonify(successful=False, message=ControllerTextConstants.NOTIFICATION_DELETE_ONE_ERR)

            return jsonify(successful=True, message=ControllerTextConstants.NOTIFICATION_DELETE_ONE_SUCCESSFUL)
