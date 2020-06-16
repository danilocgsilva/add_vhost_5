import os

class File_Writter:

    def set_file_path(self, file_path: str):

        if not os.path.isfile(file_path):
            raise Exception("File setted does not exists.")

        self.file_path = file_path

        return self


    def write(self, content: str):
        self.halt_if_file_not_setted()
        file = open(self.file_path, 'a')
        file.write(content + "\n")
        file.close()


    def is_file_writable(self) -> bool:
        self.halt_if_file_not_setted()
        try:
            open(self.file_path, 'a+').close()
            return True
        except:
            return False


    def halt_if_file_not_setted(self):
        if not hasattr(self, "file_path"):
            raise Exception("You first need to set a file to write!")
