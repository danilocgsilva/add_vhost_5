import unittest
import sys
import os
import tempfile
import shutil
sys.path.append("..")
from add_vhost_5.File_Guesser import File_Guesser
from add_vhost_5.Os_Definition_Exception import Os_Definition_Exception

class test_File_Guesser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_File_Guesser, self).__init__(*args, **kwargs)
        self.file_guesser = File_Guesser()


    def test_exception_wrong_os_assing(self):
        with self.assertRaises(Exception):
            self.file_guesser.set_os('not_exists_this_os')


    def test_exception_another_wrong_os_assing(self):
        with self.assertRaises(Exception):
            self.file_guesser.set_os('another_non_existing_system')


    def test_exception_wrong_os_assing_custom_exception(self):
        with self.assertRaises(Os_Definition_Exception):
            self.file_guesser.set_os('not_exists_with_custom_exception')


    def test_exception_another_wrong_os_assing_custom_exception(self):
        with self.assertRaises(Os_Definition_Exception):
            self.file_guesser.set_os('another_failling_trial')


    def test_get_correct_host_from_mac(self):

        path_components = ['etc', 'hosts']
        self.create_folder_for_host_file_in_test_location(path_components)
        
        base_path = os.path.join(tempfile.gettempdir(), 'base_testing_folder')
        expected_path = os.path.join(base_path, path_components[0], path_components[1])

        self.file_guesser.set_os('darwin')
        self.file_guesser.set_root(base_path)
        returned_path = self.file_guesser.guess_hosts_file()
        self.assertEqual(expected_path, returned_path)


    def test_get_correct_host_from_linux(self):

        path_components = ['etc', 'hosts']
        self.create_folder_for_host_file_in_test_location(path_components)

        base_path = os.path.join(tempfile.gettempdir(), 'base_testing_folder')
        expected_path = os.path.join(base_path, path_components[0], path_components[1])

        self.file_guesser.set_os('linux')
        self.file_guesser.set_root(base_path)
        returned_path = self.file_guesser.guess_hosts_file()
        self.assertEqual(expected_path, returned_path)


    def test_get_correct_host_from_windows(self):

        path_components = ['System32', 'drivers', 'hosts']
        self.create_folder_for_host_file_in_test_location(path_components)

        base_path = os.path.join(tempfile.gettempdir(), 'base_testing_folder')
        expected_path = os.path.join(base_path, path_components[0], path_components[1], path_components[2])

        self.file_guesser.set_os('win32')
        self.file_guesser.set_root(base_path)
        returned_path = self.file_guesser.guess_hosts_file()
        self.assertEqual(expected_path, returned_path)


    def create_folder_for_host_file_in_test_location(self, components: list):
        
        folder_components = components[:-1]
        file_to_create = components[-1]

        base_testing_folder = os.path.join(tempfile.gettempdir(), 'base_testing_folder')

        if os.path.isdir(base_testing_folder):
            shutil.rmtree(base_testing_folder, ignore_errors=False, onerror=None)

        directory_to_create = os.path.join(base_testing_folder)

        for folder in folder_components:
            directory_to_create = os.path.join(directory_to_create, folder)
            os.makedirs(directory_to_create)

        open(os.path.join(directory_to_create, file_to_create), 'a').close()


if __name__ == '__main__':
    unittest.main()
