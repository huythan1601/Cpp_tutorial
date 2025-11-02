import os


class file_handler:
    def __init__(self, filePath):
        self.__filePath = filePath
        pass

    def set_filePath(self, filePath):
        self.__filePath = filePath

    def get_filePath(self):
        return self.__filePath
    
    def check_fileExistence(self):
        if os.path.exists(self.__filePath):
            return True
        else:
            return False
        
    def create_file(self):
        if self.check_fileExistence() == False:
            ## File doesn't exist so it can be created
            with open(self.__filePath, "w") as file:
                file.write("")
                print(f"Created {self.__filePath} file successfully")
        else:
            ## File already exists
            print(f"{self.__filePath} file already exists")

    
    def read_file(self, returnType:str = "string"):
        if self.check_fileExistence() == True:
            ## File exists
            with open(self.__filePath, "r") as file:
                if returnType == "string":
                    return file.read()
                elif returnType == "list":
                    return file.readlines()
                else:
                    raise Exception ("The 'returnType' input is not valid")
        else:
            ## File doesn't exist
            raise Exception ("The target file does not exist")
    
    def write_toFile(self, content:str = "", writingMode:str = "overwrite"):
        if self.check_fileExistence() == True:
            ## File exists
            if writingMode == "overwrite":   ## overwrite the file by the content
                with open(self.__filePath, "w") as file:
                    file.write(content)
            elif writingMode == "appendix":  ## append the content to the last line of file
                with open(self.__filePath, "a") as file:
                    file.write(content)
            else:                            
                ## invalid writing mode
                raise Exception ("The 'writingMode' input is not valid")    
        else:
            ## File doesn't exist
            raise Exception ("The target file does not exist")



