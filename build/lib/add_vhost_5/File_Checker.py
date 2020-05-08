import os

class File_Checker:
    def __init__(self, file: str = ""):
        if file is not "":
            self.file = file

    def set_file(self, file: str):
        self.file = file

    def exists(self) -> bool:
        return os.path.isfile(self.file)

    def is_writable(self) -> bool:
        try:
            file_resorce = open(self.file, 'a+')
            file_resorce.close()
            return True
        except PermissionError:
            return False