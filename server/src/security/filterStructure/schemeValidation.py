# Auxiliary File Of The Filter Structure

import re
import json
from flask import request


class PostRequestSchemeValidation:

    @staticmethod
    def loginValidation():
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        # Check Control

        if not all([username, password]):
            return False

        # Password Field Control

        minPasswordLength = 8
        maxPasswordLenght = 16

        if len(password) < minPasswordLength or len(password) > maxPasswordLenght:
            return False

        return True

    @staticmethod
    def registerValidation():
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        # Check Control

        if not all([username, password, email]):
            return False

        # Password Field Control

        minPasswordLength = 8
        maxPasswordLenght = 16

        if len(password) < minPasswordLength or len(password) > maxPasswordLenght:
            return False

        # Email Control

        emailRegex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

        if not re.match(emailRegex, email):
            return False

        return True

    @staticmethod
    def generalValidation():
        data = request.get_json()

        action = data.get("action")
        parameters = data.get("parameters")

        # Check Control

        if not all([action, parameters]):
            return False

        # Parameters Control

        try:
            json.loads(parameters)
        except json.decoder.JSONDecodeError:
            return False

        return True
