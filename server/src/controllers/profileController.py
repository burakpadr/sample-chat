import json
import re
from datetime import datetime, timedelta
from flask import request, jsonify, session
from .controller import Controller
from src.etc.constants import ControllerTextConstants, OtherConstants
from src.models.userModel import User
from src.models.userLogModel import UserLog
from src.models.friendshipModel import Friendship
from src.models.friendshipNotificationModel import FriendshipNotification
from src.models.userChatNotificationModel import UserChatNotification


class ProfileController(Controller):

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

            if self.__action == "whoami":
                return self.__whoami()
            elif self.__action == "reset-username":
                return self.__resetUsername()
            elif self.__action == "reset-password":
                return self.__resetPassword()
            elif self.__action == "reset-email":
                return self.__resetEmail()
            else:
                return jsonify(None)

        def __whoami(self):
            user = User(username=session.get("username")).readFirst()
            user.__delitem__("password")

            return jsonify(whoami=user)

        def __resetUsername(self):
            userLog = UserLog(username=session.get("username"))
            date = datetime.strptime(userLog.readFirst().get("nextUsernameReplacementDate"), OtherConstants.DATE_FORMAT)

            if datetime.now() < date:
                return jsonify(successful=False, message=f"You can change your username only once a day, you can change your username on {date.strftime(OtherConstants.DATE_FORMAT)}")

            username = self.__parameters.get("username")
            
            if username is None or username == "":
                return jsonify(successful=False, message=ControllerTextConstants.PROFILE_RESET_USERNAME_NULL_ERR)
            elif not User(username=username).isExistModel():
                User(username=session.get("username")).update(username=username)
                Friendship(username=session.get("username")).update(username=username)
                FriendshipNotification(username=session.get("username")).update(username=username)
                UserChatNotification(username=session.get("username")).update(username=username)
                userLog.update(username=username, nextUsernameReplacementDate=(datetime.now()+ timedelta(days=1)).strftime(OtherConstants.DATE_FORMAT))
                
                session["username"] = username

                return jsonify(successful=True, message=ControllerTextConstants.PROFILE_RESET_USERNAME_SUCCESSFUL)

            return jsonify(successful=False, message=ControllerTextConstants.PROFILE_RESET_USERNAME_EXIST_USER_ERR)

        def __resetPassword(self):
            password = self.__parameters.get("password")

            minPasswordLength = 8
            maxPasswordLength = 16

            if password is None:
                return jsonify(None)
            elif len(password) >= minPasswordLength and maxPasswordLength >= len(password):
                User(username=session.get("username")).update(password=password)

                return jsonify(successful=True, message=ControllerTextConstants.PROFILE_RESET_PASSWORD_SUCCESSFUL)

            return jsonify(successful=False, message=ControllerTextConstants.PROFILE_RESET_PASSWORD_LENGTH_ERR)

        def __resetEmail(self):
            userLog = UserLog(username=session.get("username"))
            date = datetime.strptime(userLog.readFirst().get("nextEmailReplacementDate"), OtherConstants.DATE_FORMAT)

            if datetime.now() < date:
                return jsonify(successful=False, message=f"You can change your email only once a day, you can change your username on {date.strftime(OtherConstants.DATE_FORMAT)}")

            email = self.__parameters.get("email")
    
            emailRegex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            
            if not re.match(emailRegex, email):
                return jsonify(successful=False, message=ControllerTextConstants.PROFILE_RESET_EMAIL_FORMAT_ERR)
            elif not User(email=email).isExistModel():
                User(username=session.get("username")).update(email=email)
                userLog.update(nextEmailReplacementDate=(datetime.now()+ timedelta(days=1)).strftime(OtherConstants.DATE_FORMAT))

                return jsonify(successful=True, message=ControllerTextConstants.PROFILE_RESET_EMAIL_SUCCESSFUL)

            return jsonify(successful=False, message=ControllerTextConstants.PROFILE_RESET_EMAIL_EXIST_USER_ERR)
