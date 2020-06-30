class Rocket:

    def __init__(self, name, mission):
        """
        :param name: str
        :param mission: str or list
        """
        # attributes are private to class Rocket
        self.__name = name      
        self.__mission = mission

    def getMission(self): 
        """
        : return str or list
        """
        return self.__mission

    def addMission(self, mission): 
        # procedure method which adds a new mission. There can be one (str) or multiple (list) existing missions
        """
        : param mission: str
        """
        if type(self.__mission) is not list:
            self.__mission = [self.__mission]
        self.__mission.append(mission)

    def getName(self):
        """
        : return str
        """
        return self.__name

    
class Shuttle(Rocket):

    def __init__(self, name, mission, model):
        # call parent constructor to set name and mission  
        """
        :param name: str
        :param mission: str or list
        : param model: str
        """
        super().__init__(name, mission)
        self.__model = model

    def getDescription(self):
        return 'Name: {0}\nModel: {1}\nMissions: {2}'.format(self.getName(), self.__model, str(self.getMission()))


dragon = Shuttle("Crew Dragon", "Dragon 2 pad abort test", "V2")
print(dragon.getDescription(), '\n')
dragon.addMission('Dragon 2 in-flight abort test')
print(dragon.getDescription())