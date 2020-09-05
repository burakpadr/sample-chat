import json
from datetime import datetime
from flask import request, session, jsonify
from .controller import Controller
from src.etc.constants import ControllerTextConstants, OtherConstants
from src.models.friendshipModel import Friendship
from src.models.userChatMessageModel import UserChatMessage
from src.models.userChatNotificationModel import UserChatNotification


class ChatController(Controller):

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

            if self.__action == "chat-permission":
                return self.__chatPermission()
            elif self.__action == "stream":
                return self.__stream()
            elif self.__action == "send-message":
                return self.__sendMessage()
            elif self.__action == "new-incoming-messages":
                return self.__newIncomingMessages()
            elif self.__action == "delete-stream":
                return self.__deleteStream()
            else:
                return jsonify(None)

        def __chatPermission(self):
            chatWith = self.__parameters.get("chatWith")

            if not self.__isFriend(chatWith):
                return jsonify(successful=False, message=ControllerTextConstants.CHAT_CONTROL_NOT_FRIENDS)

            return jsonify(successful=True, message=None)

        def __stream(self):
            chatWith = self.__parameters.get("chatWith")

            if not self.__isFriend(chatWith):
                return jsonify(successful=False, message=ControllerTextConstants.CHAT_CONTROL_NOT_FRIENDS)
            
            # Configure user chat message model

            userChatMessageModel = UserChatMessage(
                username=session.get("username"), chatWith=chatWith)
            userChatMessageRead = userChatMessageModel.readFirst()

            userChatMessageRead["newMessageSize"] = 0

            userChatMessageModel.update(
                newMessageSize=userChatMessageRead.get("newMessageSize"))
            
            # Configure user chat notification model
            
            UserChatNotification(username=session.get("username"), sender=chatWith).update(content=None)

            return jsonify(successful=True, stream=userChatMessageRead.get("stream"))

        def __sendMessage(self):
            receiver = self.__parameters.get("receiver")
            message = self.__parameters.get("message")

            if not self.__isFriend(receiver):
                return jsonify(successful=False, message=ControllerTextConstants.CHAT_CONTROL_NOT_FRIENDS)

            # Configure user chat message model

            sessionUserChatMessageModel = UserChatMessage(
                username=session.get("username"), chatWith=receiver)
            sessionUserChatMessageRead = sessionUserChatMessageModel.readFirst()

            receiverUserChatMessageModel = UserChatMessage(
                username=receiver, chatWith=session.get("username"))
            receiverUserChatMessageRead = receiverUserChatMessageModel.readFirst()

            sessionUserChatMessageRead["stream"].append(
                {"sender": "__session__", "date": datetime.now().strftime(OtherConstants.DATE_FORMAT), "message": message})
            receiverUserChatMessageRead["stream"].append(
                {"sender": session.get("username"), "date": datetime.now().strftime(OtherConstants.DATE_FORMAT), "message": message})
            receiverUserChatMessageRead["newMessageSize"] += 1

            sessionUserChatMessageModel.update(
                stream=sessionUserChatMessageRead.get("stream"))
            receiverUserChatMessageModel.update(stream=receiverUserChatMessageRead.get(
                "stream"), newMessageSize=receiverUserChatMessageRead.get("newMessageSize"))

            # Configure user chat notification model

            receiverUserChatNotificationModel = UserChatNotification(
                username=receiver, sender=session.get("username"))
            receiverUserChatNotificationRead = receiverUserChatNotificationModel.readFirst()

            receiverUserChatNotificationRead[
                "content"] = f"There are {receiverUserChatMessageRead.get('newMessageSize')} unread messages from {session.get('username')}"
            receiverUserChatNotificationRead["date"] = datetime.now().strftime(
                OtherConstants.DATE_FORMAT)

            receiverUserChatNotificationModel.update(date=receiverUserChatNotificationRead.get("date"),
                                                     content=receiverUserChatNotificationRead.get("content"),
                                                     isRead=False)

            return jsonify(successful=True, message=None)

        def __newIncomingMessages(self):
            chatWith = self.__parameters.get("chatWith")

            if not self.__isFriend(chatWith):
                return jsonify(successful=False, message=ControllerTextConstants.CHAT_CONTROL_NOT_FRIENDS)

            userChatMessageModel = UserChatMessage(
                username=session.get("username"), chatWith=chatWith)
            userChatMessageRead = userChatMessageModel.readFirst()

            reversedStream = userChatMessageRead.get("stream")[::-1]
            newIncomingMessages = reversedStream[:userChatMessageRead.get(
                "newMessageSize")]

            userChatMessageRead["newMessageSize"] = 0

            userChatMessageModel.update(
                newMessageSize=userChatMessageRead.get("newMessageSize"))

            return jsonify(successful=True, newIncomingMessages=newIncomingMessages)

        def __deleteStream(self):
            chatWith = self.__parameters.get("chatWith")

            if not self.__isFriend(chatWith):
                return jsonify(successful=False, message=ControllerTextConstants.CHAT_CONTROL_NOT_FRIENDS)
            
            # Configure user chat message model

            UserChatMessage(username=session.get("username"),
                            chatWith=chatWith).update(stream=[])

            # Configure user chat notification model
            
            UserChatNotification(username=session.get("username"), sender=chatWith).update(content=None)

            return jsonify(successful=True, message=ControllerTextConstants.CHAT_DELETE_STREAM_SUCCESSFUL)

        @ staticmethod
        def __isFriend(username):
            return Friendship(username=session.get("username")).readFirst().get("friends").__contains__(username)
