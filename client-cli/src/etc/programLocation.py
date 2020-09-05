class ProgramLocation:
    
    def __init__(self):
        self.__location = None
        self.__locationParamteres = {}

    def setLocation(self, controller):
        self.__location = controller.__name__
    
    def setLocationParameters(self, **kwargs):
        self.__locationParamteres = kwargs
        
    def getLocation(self):
        return self.__location

    def getLocationParameters(self):
        return self.__locationParamteres
    

programLocation = ProgramLocation()