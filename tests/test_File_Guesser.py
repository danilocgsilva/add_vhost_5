import unittest
import sys
import os
import tempfile
sys.path.append("..")
from tests.File_Builder_Helper import File_Builder_Helper
from add_vhost_5.File_Guesser import File_Guesser
from add_vhost_5.Os_Definition_Exception import Os_Definition_Exception

class test_File_Guesser(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_File_Guesser, self).__init__(*args, **kwargs)
        self.file_guesser = File_Guesser()
        self.file_builder_helper = File_Builder_Helper()


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
        self.file_builder_helper.create_testing_file(path_components)
        
        base_path = self.file_builder_helper.get_base_testing_folder()
        expected_path = os.path.join(base_path, path_components[0], path_components[1])

        self.file_guesser.set_os('darwin')
        self.file_guesser.set_root(base_path)
        returned_path = self.file_guesser.guess_hosts_file()
        self.assertEqual(expected_path, returned_path)


    def test_get_correct_host_from_linux(self):

        path_components = ['etc', 'hosts']
        self.file_builder_helper.create_testing_file(path_components)

        base_path = self.file_builder_helper.get_base_testing_folder()
        expected_path = os.path.join(base_path, path_components[0], path_components[1])

        self.file_guesser.set_os('linux')
        self.file_guesser.set_root(base_path)
        returned_path = self.file_guesser.guess_hosts_file()
        self.assertEqual(expected_path, returned_path)


    def test_get_correct_host_from_windows(self):

        path_components = ['System32', 'drivers', 'hosts']
        self.file_builder_helper.create_testing_file(path_components)

        base_path = self.file_builder_helper.get_base_testing_folder()
        expected_path = os.path.join(base_path, path_components[0], path_components[1], path_components[2])

        self.file_guesser.set_os('win32')
        self.file_guesser.set_root(base_path)
        returned_path = self.file_guesser.guess_hosts_file()
        self.assertEqual(expected_path, returned_path)


    def test_create_folder_for_vhost_conf_test_location_in_mac(self):

        path_components = ['Applications', 'XAMPP', 'xamppfiles', 'etc', 'extra', 'httpd-vhosts.conf']
        self.file_builder_helper.create_testing_file(path_components)

        base_path = self.file_builder_helper.get_base_testing_folder()
        expected_path = os.path.join(base_path, path_components[0], path_components[1], path_components[2], path_components[3], path_components[4], path_components[5])

        self.file_guesser.set_os('darwin')
        self.file_guesser.set_root(base_path)
        returned_path = self.file_guesser.guess_vhosts_configuration_path()
        self.assertEqual(expected_path, returned_path)


    def test_create_folder_for_vhost_conf_test_location_in_windows(self):

        path_components = ['wamp64', 'bin', 'apache', 'apache2.4.41', 'conf', 'extra', 'httpd-vhosts.conf']
        self.file_builder_helper.create_testing_file(path_components)

        base_path = self.file_builder_helper.get_base_testing_folder()
        expected_path = os.path.join(base_path, path_components[0], path_components[1], path_components[2], path_components[3], path_components[4], path_components[5], path_components[6])

        self.file_guesser.set_os('win32')
        self.file_guesser.set_root(base_path)
        returned_path = self.file_guesser.guess_vhosts_configuration_path()
        self.assertEqual(expected_path, returned_path)


    def test_fail_tries_get_vhost_config_without_setting_os(self):
        with self.assertRaises(Exception):
            self.file_guesser.guess_vhosts_configuration_path()


    def test_fail_when_file_does_not_exists_for_mac(self):
        base_path = self.file_builder_helper.get_base_testing_folder()
        self.file_builder_helper.create_testing_file(['non', 'sense', 'way.txt'])

        self.file_guesser.set_os('darwin')
        self.file_guesser.set_root(base_path)

        with self.assertRaises(Exception):
            self.file_guesser.guess_vhosts_configuration_path()


    def test_fail_when_file_does_not_exists_for_windows(self):
        base_path = self.file_builder_helper.get_base_testing_folder()
        self.file_builder_helper.create_testing_file(['non', 'sense', 'way.txt'])

        self.file_guesser.set_os('win32')
        self.file_guesser.set_root(base_path)

        with self.assertRaises(Exception):
            self.file_guesser.guess_vhosts_configuration_path()


    def test_fail_when_file_does_not_exists_for_windows_hosts(self):
        base_path = self.file_builder_helper.get_base_testing_folder()
        self.file_builder_helper.create_testing_file(['non', 'sense', 'way.txt'])

        self.file_guesser.set_os('win32')
        self.file_guesser.set_root(base_path)

        with self.assertRaises(Exception):
            self.file_guesser.guess_hosts_file()
        

if __name__ == '__main__':
    unittest.main()
