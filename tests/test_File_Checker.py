import unittest
import tempfile
import os
import sys
sys.path.append("..")
from add_vhost_5.File_Checker import File_Checker

class test_File_Checker(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_File_Checker, self).__init__(*args, **kwargs)
        self.file_checker = File_Checker()


    def test_asserts_file_is_writable(self):
        file_resource, full_file_path = self.create_stub_file_in_tmp_directory('stub_file.txt')
        self.file_checker.set_file(full_file_path)
        self.assertTrue(self.file_checker.is_writable())
        file_resource.close()
        os.remove(full_file_path)


    def create_stub_file_in_tmp_directory(self, file_name):
        temporary_folder = tempfile.gettempdir()
        full_file_path = os.path.join(temporary_folder, file_name)
        file_resource = open(full_file_path, 'a+')
        return file_resource, full_file_path


if __name__ == '__main__':
    unittest.main()

