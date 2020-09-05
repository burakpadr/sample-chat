from flask import request, session, jsonify
from .controller import Controller
from src.models.userModel import User
from src.etc.constants import ControllerTextConstants


class LoginController(Controller):
    
    def __init__(self):
        super().__init__(self)
        
    class Post:
        
        def __init__(self):
            data = request.get_json()
            
            self.__username = data.get("username")
            self.__password = data.get("password")
            
        def handler(self):
            if bool(session):
                return jsonify(None)

            if User(username=self.__username, password=self.__password).isExistModel():
                session["username"] = self.__username
                
                return jsonify(successful= True, message=ControllerTextConstants.LOGIN_SUCCESSFUL_MSG)
            
            return jsonify(successful=False, message=ControllerTextConstants.LOGIN_ERR)