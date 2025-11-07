import os
import subprocess
import shutil

class util:
    def __init__(self):
        pass

    def check_pathExistence(self, path:str):
        if os.path.exists(path):
            return True
        else:
            return False
        
    def create_folder(self, folderPath:str):
        if os.path.exists(folderPath):
            shutil.rmtree(folderPath)
        os.makedirs(folderPath, exist_ok=True)

    def execute_command(self, commandList:list, workingDirectory:str):
        res = subprocess.run(commandList, cwd = workingDirectory)
        return res.returncode 
    
    def run_executableFile(self, filePath:str):
        subprocess.run([filePath])

    
    
