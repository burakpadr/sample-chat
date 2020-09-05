from .project import Project


class ViewTextConstants:

    PREFIX = "$ "
    ACCESS_TITLE = f"{Project.NAME} {Project.VERSION}\n"
    ACCESS_SUBTITLE = "1- Login\n2- Register\n3- Forgot Password?\n4- Exit\n"
    LOGIN_TITLE = "Login area, press to CTRL + C for exit!\n"
    REGISTER_TITLE = "Register area, press to CTRL + C for exit!\n"
    PROFILE_TITLE = "Profile area, press to CTRL + C for exit!\n"
    LOBBY_TITLE = "Lobby area, say /help for help!\n"
    FRIENDSHIP_TITLE = "Friendship area, say /help for help\n"
    NOTIFICATION_TITLE = "Notification area, say /help for help\n"
    SETTINGS_TITLE = "Settings area, say /help for help\n"


class FormTextConstants:

    ELEMENTS_NULL_ERR = "Form elements cannot be empty!"
    PASSWORD_LENGTH_ERR = "Password length must be 8 between 16"
    PASSWORDS_NOT_MATCHED_ERR = "Passwords not matched!"
    EMAIL_FORMAT_ERR = "Email address must be such example@domain.com"


class CommandStructureConstants:

    COMMAND_PREFIX = "/"
    COMMAND_STRUCTURE_COMPATIBILITY_ERR = "Try -> /command"
    NO_SUCH_COMMAND_ERR = "No such command!"
