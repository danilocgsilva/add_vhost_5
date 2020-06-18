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

        path_components = ['Windows', 'System32', 'drivers', 'etc', 'hosts']
        self.file_builder_helper.create_testing_file(path_components)

        base_path = self.file_builder_helper.get_base_testing_folder()
        expected_path = os.path.join(base_path, path_components[0], path_components[1], path_components[2], path_components[3], path_components[4])

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


    def test_fluent_interface_set_os(self):
        file_guesser = self.file_guesser.set_os('darwin')
        self.assertTrue(isinstance(file_guesser, File_Guesser))

    
    def test_get_root_with_separator(self):
        path = os.path.join('any', 'root', 'path')
        self.file_guesser.set_root(path)
        path_with_sep = self.file_guesser.get_root_with_separator()

        self.assertEqual(path + os.sep, path_with_sep)


    def test_get_full_physical_path_folder_windows(self):
        my_host = 'testing_host_name'

        expected_path = "C:" + os.sep + os.path.join('wamp64', 'www', my_host)

        self.file_guesser.set_os('win32')
        returned_www_path = self.file_guesser\
            .set_hostname(my_host)\
            .get_full_physical_path()
        self.assertEqual(expected_path, returned_www_path)


    def test_set_hostname_fluent_interface(self):
        my_host = 'testing_host_name'
        file_guesser = self.file_guesser.set_hostname(my_host)
        self.assertTrue(isinstance(file_guesser, File_Guesser))
        

    def test_fail_get_full_physical_path_without_hostname(self):
        self.file_guesser.set_os('win32')

        with self.assertRaises(Exception):
            self.file_guesser.get_full_physical_path()


    def test_get_welcome_index_path_for_windows(self):
        self.file_guesser.set_os('win32')
        hostname = 'my_testing_hostname'
        expected_path = "C:" + os.sep + os.path.join('wamp64', 'www', hostname, 'index.html')
        self.file_guesser.set_hostname(hostname)
        returned_index_path = self.file_guesser.get_welcome_index()
        self.assertEqual(expected_path, returned_index_path)
        

if __name__ == '__main__':
    unittest.main()
