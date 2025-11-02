from pathlib import Path

from common.cmake_handler import cmake_handler
from common.config_handler import config_handler
from common.file_handler import file_handler
from common.util import util


## Declare neccessary path
rootPath = Path(__file__).resolve().parent.parent
codeFolderPath =  f"{rootPath}/code"
configFilePath = f"{rootPath}/Config.yml"
cmakeFileName = "CmakeLists.txt"

 

def create_cmakeListsFile(projectName:str, targetProjectPath:str):
    ## Get content of CmakeLists.txt file
    cmakeObject = cmake_handler(projectName = projectName)
    cmakeContent = cmakeObject.get_cmakeContent()

    ## create CmakeLists.txt file and write prepared content to it
    cmakeFilePath = f"{targetProjectPath}/{cmakeFileName}"
    cmakeFileObject = file_handler(cmakeFilePath)
    cmakeFileObject.create_file()
    cmakeFileObject.write_toFile(content = cmakeContent, writingMode = "overwrite")

def build_source(targetProjectPath:str):
    continueFlag = True
    ## create folder "build"
    buildFolderPath = f"{targetProjectPath}/build"
    utilObject = util()
    utilObject.create_folder(buildFolderPath)

    ## execute CmakeLists
    res = utilObject.execute_command(["cmake", ".."], workingDirectory = buildFolderPath)
    if (res != 0):
        print("failed in build")
        continueFlag = False

    if continueFlag == True:
        ## execute makeFile
        res = utilObject.execute_command(["make"], workingDirectory = buildFolderPath)
        if (res != 0):
            print("failed in build")
            continueFlag = False

    if continueFlag == True:
        print("Build successfuly")

    
    





if __name__ == "__main__":
    ## Get project infor
    configObject = config_handler(configFilePath)
    projectName = configObject.get_projectName()
    projectFolderPath = configObject.get_projectPath()
    targetProjectPath = f"{codeFolderPath}/{projectFolderPath}"

    create_cmakeListsFile(projectName=projectName, targetProjectPath=targetProjectPath)
    build_source(targetProjectPath=targetProjectPath)



