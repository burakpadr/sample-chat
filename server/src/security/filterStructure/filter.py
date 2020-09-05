# Main File Of The Filter Structure


from flask import request
from .schemeValidation import PostRequestSchemeValidation


class Filter:

    __POST_REQUEST_SCHEME = {
        "LoginController": {
            "elements": ["username", "password"],
            "validation": PostRequestSchemeValidation.loginValidation
        },
        "RegisterController": {
            "elements": ["username", "password", "email"],
            "validation": PostRequestSchemeValidation.registerValidation
        },
        "ChatController": {
            "elements": ["action", "parameters"],
            "validation": PostRequestSchemeValidation.generalValidation
        },
        "FriendshipController": {
            "elements": ["action", "parameters"],
            "validation": PostRequestSchemeValidation.generalValidation
        },
        "NotificationController": {
            "elements": ["action", "parameters"],
            "validation": PostRequestSchemeValidation.generalValidation
        },
        "ProfileController": {
            "elements": ["action", "parameters"],
            "validation": PostRequestSchemeValidation.generalValidation
        }
    }

    @staticmethod
    def postRequestCompatibility(controller):
        controllerName = controller.__class__.__name__
        incomingRequestData = request.get_json()

        for requiredElement in Filter.__POST_REQUEST_SCHEME.get(controllerName).get("elements"):
            if not incomingRequestData.__contains__(requiredElement):
                return False

        return Filter.__POST_REQUEST_SCHEME.get(controllerName).get("validation")()
