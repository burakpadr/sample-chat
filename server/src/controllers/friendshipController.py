import json
import random
from datetime import datetime
from flask import request, jsonify, session
from .controller import Controller
from src.etc.constants import ControllerTextConstants, OtherConstants
from src.models.friendshipModel import Friendship
from src.models.userChatMessageModel import UserChatMessage
from src.models.friendshipNotificationModel import FriendshipNotification
from src.models.userChatNotificationModel import UserChatNotification


class FriendshipController(Controller):

    def __init__(self):
        super().__init__(self)

    class Post:

        def __init__(self):
            data = request.get_json()

            self.__sessionFriendship = Friendship(
                username=session.get("username"))
            self.__sessionFriendshipRead = self.__sessionFriendship.readFirst()

            self.__action = data.get("action")
            self.__parameters = json.loads(data.get("parameters"))

        def handler(self):
            if not bool(session):
                return jsonify(None)

            if self.__action == "friends":
                return self.__friends()
            elif self.__action == "incoming":
                return self.__incoming()
            elif self.__action == "outgoing":
                return self.__outgoing()
            elif self.__action == "request":
                return self.__request()
            elif self.__action == "accept":
                return self.__accept()
            elif self.__action == "ignore":
                return self.__ignore()
            elif self.__action == "remove":
                return self.__remove()
            elif self.__action == "online-list":
                return self.__onlineList()
            elif self.__action == "is-online":
                return self.__isOnline()
            else:
                return jsonify(None)

        def __friends(self):
            return jsonify(friends=self.__sessionFriendshipRead.get("friends"))

        def __incoming(self):
            return jsonify(incoming=self.__sessionFriendshipRead.get("incoming"))

        def __outgoing(self):
            return jsonify(outgoing=self.__sessionFriendshipRead.get("outgoing"))

        def __request(self):
            username = self.__parameters.get("username")

            sessionFriends = self.__sessionFriendshipRead.get("friends")
            sessionIncoming = self.__sessionFriendshipRead.get("incoming")
            sessionOutgoing = self.__sessionFriendshipRead.get("outgoing")

            userFriendship = Friendship(username=username)

            if session.get("username") == username:
                return jsonify(successful=False, message=ControllerTextConstants.FRIENDSHIP_USERNAME_ERR)
            elif not userFriendship.isExistModel():
                return jsonify(successful=False, message=ControllerTextConstants.FRIENDSHIP_NO_SUCH_USER_ERR)
            elif sessionFriends.__contains__(username):
                return jsonify(successful=False, message=ControllerTextConstants.FRIENDSHIP_ALREADY_YOU_ARE_FRIENDS_ERR)
            elif sessionIncoming.__contains__(username) or sessionOutgoing.__contains__(username):
                return jsonify(successful=False, message=ControllerTextConstants.FRIENDSHIP_ALREADY_SUCH_EXIST_REQUEST_ERR)

            userFriendshipRead = userFriendship.readFirst()
            userIncoming = userFriendshipRead.get("incoming")

            sessionOutgoing.append(username)
            userIncoming.append(session.get("username"))

            self.__sessionFriendship.update(outgoing=sessionOutgoing)
            userFriendship.update(incoming=userIncoming)

            FriendshipNotification.createNotification(
                username, f"New friendship request recieved from {session.get('username')}")

            return jsonify(successful=True, message=ControllerTextConstants.FRIENDSHIP_REQUEST_SENT)

        def __accept(self):
            username = self.__parameters.get("username")

            userFriendship = Friendship(username=username)

            if not userFriendship.isExistModel():
                return jsonify(successful=False, message=ControllerTextConstants.FRIENDSHIP_NO_SUCH_USER_ERR)

            sessionIncoming = self.__sessionFriendshipRead.get("incoming")
            sessionFriends = self.__sessionFriendshipRead.get("friends")

            userFriendshipRead = userFriendship.readFirst()
            userOutgoing = userFriendshipRead.get("outgoing")
            userFriends = userFriendshipRead.get("friends")

            if not sessionIncoming.__contains__(username):
                return jsonify(successful=False, message=ControllerTextConstants.FRIENDSHIP_NO_SUCH_REQUEST_ERR)

            sessionIncoming.remove(username)
            sessionFriends.append(username)
            userOutgoing.remove(session.get("username"))
            userFriends.append(session.get("username"))

            self.__sessionFriendship.update(
                friends=sessionFriends, incoming=sessionIncoming)
            UserChatMessage(username=session.get(
                "username"), chatWith=username, newMessageSize=0, stream=[]).create()
            UserChatNotification.createNotification(
                session.get("username"), username, None)

            userFriendship.update(friends=userFriends,
                                  outgoing=userOutgoing)
            UserChatMessage(username=username, chatWith=session.get(
                "username"), newMessageSize=0, stream=[]).create()
            UserChatNotification.createNotification(
                username, session.get("username"), None)

            FriendshipNotification.createNotification(
                username, f"{session.get('username')}, accepted the friendship request you sent")

            return jsonify(successful=True, message=ControllerTextConstants.FRIENDSHIP_ACCEPTED_REQUEST)

        def __ignore(self):
            username = self.__parameters.get("username")

            userFriendship = Friendship(username=username)

            if not userFriendship.isExistModel():
                return jsonify(successful=False, message=ControllerTextConstants.FRIENDSHIP_NO_SUCH_USER_ERR)

            sessionIncoming = self.__sessionFriendshipRead.get("incoming")

            userFriendshipRead = userFriendship.readFirst()
            userOutgoing = userFriendshipRead.get("outgoing")

            if not sessionIncoming.__contains__(username):
                return jsonify(successful=False, message=ControllerTextConstants.FRIENDSHIP_NO_SUCH_REQUEST_ERR)

            sessionIncoming.remove(username)
            userOutgoing.remove(session.get("username"))

            self.__sessionFriendship.update(incoming=sessionIncoming)
            userFriendship.update(outgoing=userOutgoing)

            return jsonify(successful=True, message=ControllerTextConstants.FRIENDSHIP_IGNORED_REQUEST)

        def __remove(self):
            username = self.__parameters.get("username")

            userFriendship = Friendship(username=username)

            if not userFriendship.isExistModel():
                return jsonify(successful=False, message=ControllerTextConstants.FRIENDSHIP_NO_SUCH_USER_ERR)

            sessionFriends = self.__sessionFriendshipRead.get("friends")

            userFriendshipRead = userFriendship.readFirst()
            userFriends = userFriendshipRead.get("friends")

            if not sessionFriends.__contains__(username):
                return jsonify(successful=False, message=ControllerTextConstants.FRIENDSHIP_NOT_FRIEND_ERR)

            sessionFriends.remove(username)
            userFriends.remove(session.get("username"))

            self.__sessionFriendship.update(friends=sessionFriends)
            UserChatMessage(username=session.get("username"),
                            chatWith=username).delete()
            UserChatNotification(username=session.get(
                "username"), sender=username).delete()

            userFriendship.update(friends=userFriends)
            UserChatMessage(username=username,
                            chatWith=session.get("username")).delete()
            UserChatNotification(
                username=username, sender=session.get("username")).delete()

            return jsonify(successful=True, message=ControllerTextConstants.FRIENDSHIP_REMOVED_FRIENDSHIP_LIST)

        def __onlineList(self):
            pass

        def __isOnline(self):
            pass
