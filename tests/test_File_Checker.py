import unittest
import tempfile
import os

class test_File_Checker(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        

    def test_asserts_file_is_writable(self):
        self.create_stub_file()
        self.assertTrue(True)


    def create_stub_file(self):
        stub_file = 'stub_file.txt'
        temporary_folder = tempfile.gettempdir()
        full_file_path = os.path.join(temporary_folder, stub_file)
        open(full_file_path, 'a+')
        print(full_file_path)


if __name__ == '__main__':
    unittest.main()

