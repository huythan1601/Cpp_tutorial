import yaml

class config_handler:
    def __init__(self, configFile:str):
        self.__projectName = ""
        self.__projectPath = ""
        self.get_configuration(configFile=configFile)
        pass

    def get_configuration(self, configFile:str):
        # Open and read the YAML file
        with open(configFile, "r") as file:
            data = yaml.safe_load(file)
        self.__projectPath:str = data["Project_Name"]
        self.__projectName = self.__projectPath.replace("/", "_")

    def get_projectPath(self):
        return self.__projectPath
    
    
    def get_projectName(self):
        return self.__projectName
        

