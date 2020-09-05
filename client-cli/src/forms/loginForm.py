from getpass import getpass
from src.etc.constants import FormTextConstants


class LoginForm:
    
    def __init__(self):
        self.__username = None
        self.__password = None
        
        self.__validationMessage = None
    
    def fillTheForm(self):
        self.__username = input("Username -> ")
        self.__password = getpass("Password -> ")
        
    def validation(self):
        # Null Check
        
        if not all([self.__username, self.__password]):
            self.__validationMessage = FormTextConstants.ELEMENTS_NULL_ERR
            
            return False
    
        # Password Field Control
        
        minPasswordLength = 8
        maxPasswordLength = 16
        
        if len(self.__password) < minPasswordLength or len(self.__password) > maxPasswordLength:
            self.__validationMessage = FormTextConstants.PASSWORD_LENGTH_ERR
            
            return False

        return True
    
    def getValidationMessage(self):
        return self.__validationMessage
    
    def getData(self):
        return {
            "username": self.__username,
            "password": self.__password
        }