import os

class File_Checker:
    def __init__(self, file: str):
        self.file = file

    def exists(self) -> bool:
        return os.path.isfile(self.file)

    def writable(self) -> bool:
        try:
            open(self.file, 'a+')
            return True
        except PermissionError:
            return False