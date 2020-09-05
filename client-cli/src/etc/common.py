import os
import sys
from time import sleep


class Common:

    # Color Constants

    __RED_COLOR = "\u001b[31m"
    __GREEN_COLOR = "\u001b[32m"
    __YELLOW_COLOR = "\u001b[33m"
    __CYAN_COLOR = "\u001b[36m"
    __DEFAULT_COLOR = "\u001b[0m"
    
    # Other Constants
    
    __PROGRAM_SLEEP_TIME_SECOND = 2.5

    # Print Text Functions
    
    @staticmethod
    def printNegativeText(text):
        print(f"{Common.__RED_COLOR}{text}{Common.__DEFAULT_COLOR}")

    @staticmethod
    def printPositiveText(text):
        print(f"{Common.__GREEN_COLOR}{text}{Common.__DEFAULT_COLOR}")
    
    @staticmethod
    def printNotificationText(text):
        print(f"{Common.__YELLOW_COLOR}{text}{Common.__DEFAULT_COLOR}")
    
    @staticmethod
    def printStandartText(text):
        print(f"{Common.__DEFAULT_COLOR}{text}")
        
    @staticmethod
    def printChatLabelText(text):
        print(f"{Common.__CYAN_COLOR}{text}{Common.__DEFAULT_COLOR}", end=" ")
        
    # Clear Terminal Function
    
    @staticmethod
    def clearTerminal():
        if sys.platform == "linux" or sys.platform == "darwin":
            os.system("clear")
        elif sys.platform == "win32":
            os.system("cls")
        
    # Program Sleep Function
    
    @staticmethod
    def programSleep():
        sleep(Common.__PROGRAM_SLEEP_TIME_SECOND)