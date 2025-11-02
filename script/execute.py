from pathlib import Path

from common.cmake_handler import cmake_handler
from common.config_handler import config_handler
from common.file_handler import file_handler
from common.util import util


## Declare neccessary path
rootPath = Path(__file__).resolve().parent.parent
codeFolderPath =  f"{rootPath}/code"
configFilePath = f"{rootPath}/Config.yml"

def execute_code(executablePath):
    if util().check_pathExistence(executablePath) == True:
        print(f"-----Start to execute source code-----")
        util().run_executableFile(executablePath)
    else:
        print(f"Error: {executablePath} does not exist")

if __name__ == "__main__":
    ## Get executable file infor
    configObject = config_handler(configFilePath)
    projectName = configObject.get_projectName()
    projectFolderPath = configObject.get_projectPath()
    targetProjectPath = f"{codeFolderPath}/{projectFolderPath}"
    targetExecutablePath = f"{targetProjectPath}/build/{projectName}"

    ## run executable file
    execute_code(targetExecutablePath)