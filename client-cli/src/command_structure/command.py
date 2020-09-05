from src.etc.common import Common
from src.etc.constants import CommandStructureConstants
from .commandConfig import CommandConfig


class Command:

    def __init__(self, controller, command):
        self.__controller = controller
        self.__controllerName = controller.__name__
        self.__command = command

    def handler(self):
        if self.commandStructureCompatibility():
            if CommandConfig.insideTheCommonCommands(self.__command):
                CommandConfig.getCommonCommands().get(self.__command).get("function")(controller=self.__controller)
            elif CommandConfig.insideTheSpecialCommands(self.__controller, self.__command):
                CommandConfig.getSpecialCommands(self.__controllerName).get(self.__command).get("function")()
            else:
                Common.printNegativeText(
                    CommandStructureConstants.NO_SUCH_COMMAND_ERR)
        else:
            Common.printNegativeText(
                CommandStructureConstants.COMMAND_STRUCTURE_COMPATIBILITY_ERR)

    def commandStructureCompatibility(self):
        return self.__command.startswith(CommandStructureConstants.COMMAND_PREFIX) and len(self.__command.split(" ")) == 1
