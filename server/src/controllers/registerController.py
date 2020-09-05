from datetime import datetime
from flask import request, session, jsonify
from .controller import Controller
from src.models.userModel import User
from src.models.userLogModel import UserLog
from src.models.friendshipModel import Friendship
from src.etc.constants import ControllerTextConstants


class RegisterController(Controller):
    
    def __init__(self):
        super().__init__(self)
        
    class Post:
        
        def __init__(self):
            data = request.get_json()
            
            self.__username = data.get("username")
            self.__password = data.get("password")
            self.__email = data.get("email")
            
        def handler(self):
            if bool(session):
                return jsonify(None)
            
            if not User(username=self.__username).isExistModel() and not User(email=self.__email).isExistModel():
                date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                User(username=self.__username, password=self.__password, email=self.__email).create()
                UserLog(username=self.__username, nextUsernameReplacementDate=date, nextEmailReplacementDate=date).create()
                Friendship(username=self.__username, friends=[], incoming=[], outgoing=[]).create()
                
                return jsonify(successful=True, message=ControllerTextConstants.REGISTER_SUCCESSFUL_MSG)
            
            return jsonify(successful=False, message=ControllerTextConstants.REGISTER_ERR) 