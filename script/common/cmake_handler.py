


## Define fixed data for CmakeLists
cmakeVersion = "cmake_minimum_required(VERSION 3.22.1)\n"
cmakeExecution = "\
## add header files directory\n\
include_directories(\"src/inc\")\n\
\n\
## add source file to target build \"SRC_FILES\"\n\
file(GLOB SRC_FILES \"src/*.cpp\")\n\
\n\
## compile executable files\n\
add_executable(${PROJECT_NAME} main.cpp \n\
                               ${SRC_FILES})\n"


class cmake_handler:
    def __init__(self, projectName:str):
        self.__cmakeContent = ""
        self.__cmakeProject = ""
        self.set_cmakeProject(projectName=projectName)
        self.__prepare_cmakeContent()
        pass


    def set_cmakeProject(self, projectName:str):
        self.__cmakeProject = f"project({projectName})\n"


    def __prepare_cmakeContent(self):
        self.__cmakeContent = cmakeVersion + self.__cmakeProject + cmakeExecution
    

    def get_cmakeContent(self):
        return self.__cmakeContent




    