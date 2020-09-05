import json
from requests import Session
from src.etc.settings import Settings


class Connection:

    __SESSION = Session()
    
    @staticmethod
    def sessionClose():
        Connection.__SESSION = None
        
    @staticmethod
    def isSession():
        return Connection.__SESSION is not None

    @staticmethod
    def __baseRequest(path, data):
        return Connection.__SESSION.post(f"{Settings.URL}{path}", json=data).json()

    @staticmethod
    def loginRequest(data):
        return Connection.__baseRequest("/login", data)

    @staticmethod
    def registerRequest(data):
        return Connection.__baseRequest("/register", data)
    
    @staticmethod
    def profileRequest(action, parameters):
        return Connection.__baseRequest("/profile", {"action": action, "parameters": json.dumps(parameters)})

    @staticmethod
    def friendshipRequest(action, parameters):
        return Connection.__baseRequest("/friendship", {"action": action, "parameters": json.dumps(parameters)})

    @staticmethod
    def notificationRequest(action, parameters):
        return Connection.__baseRequest("/notification", {"action": action, "parameters": json.dumps(parameters)})
    
    @staticmethod
    def chatRequest(action, parameters):
        return Connection.__baseRequest("/chat", {"action": action, "parameters": json.dumps(parameters)})