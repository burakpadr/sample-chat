import re
from getpass import getpass
from src.etc.constants import FormTextConstants


class RegisterForm:

    def __init__(self):
        self.__username = None
        self.__password = None
        self.__confirmatoryPassword = None
        self.__email = None

        self.__validationMessage = None

    def fillTheForm(self):
        self.__username = input("Username -> ")
        self.__password = getpass("Password -> ")
        self.__confirmatoryPassword = getpass("Password (again) -> ")
        self.__email = input("Email -> ")

    def validation(self):
        # Null Check

        if not all([self.__username, self.__password, self.__confirmatoryPassword, self.__email]):
            self.__validationMessage = FormTextConstants.ELEMENTS_NULL_ERR

            return False

        # Password Field Check

        minPasswordLength = 8
        maxPasswordLength = 16

        if len(self.__password) < minPasswordLength or len(self.__password) > maxPasswordLength:
            self.__validationMessage = FormTextConstants.PASSWORD_LENGTH_ERR

            return False
        elif self.__password != self.__confirmatoryPassword:
            self.__validationMessage = FormTextConstants.PASSWORDS_NOT_MATCHED_ERR

            return False

        # Email Field Check

        emailRegex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

        if not re.match(emailRegex, self.__email):
            self.__validationMessage = FormTextConstants.EMAIL_FORMAT_ERR

            return False

        return True

    def getValidationMessage(self):
        return self.__validationMessage

    def getData(self):
        return {
            "username": self.__username,
            "password": self.__password,
            "email": self.__email
        }
