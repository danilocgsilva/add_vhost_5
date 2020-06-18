import os

class File_Writter:

    def set_file_path(self, file_path: str):

        self.file_path = file_path

        return self


    def write(self, content: str):
        self.halt_if_file_not_setted()

        if not os.path.isfile(self.file_path):
            raise Exception("File setted does not exists.")

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


    def new(self):

        folders_string = self.file_path.split(os.sep)[:-1]
        full_path_loop = ""
        for path_pass in folders_string:
            full_path_loop += path_pass + os.sep
            if not os.path.isdir(full_path_loop):
                os.makedirs(full_path_loop)

        open(self.file_path, 'a').close()
        return self
