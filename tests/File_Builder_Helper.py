import os
import tempfile
import shutil

class File_Builder_Helper:

    def __init__(self):
        self.base_testing_folder = 'base_testing_folder'


    def create_testing_file(self, path_components: str):

        folder_components = path_components[:-1]
        file_to_create = path_components[-1]

        base_testing_folder = os.path.join(tempfile.gettempdir(), self.base_testing_folder)

        if os.path.isdir(base_testing_folder):
            shutil.rmtree(base_testing_folder, ignore_errors=False, onerror=None)

        directory_to_create = os.path.join(base_testing_folder)

        for folder in folder_components:
            directory_to_create = os.path.join(directory_to_create, folder)
            os.makedirs(directory_to_create)

        open(os.path.join(directory_to_create, file_to_create), 'a').close()


    def get_base_testing_folder(self):
        return os.path.join(tempfile.gettempdir(), self.base_testing_folder)
