import unittest
import sys
import os
sys.path.append("..")
from add_vhost_5.VHost_Contents import VHost_Contents

class test_VHost_Contents(unittest.TestCase):

    def setUp(self):
        self.vhost_contents = VHost_Contents()


    def test_correct_host_entry(self):

        vhost_name_sample = "my_local_vhost"

        expected_vhost_entry = "\n127.0.0.1 " + vhost_name_sample + "\n"
        expected_vhost_entry += "::1 " + vhost_name_sample

        self.vhost_contents.set_hostname(vhost_name_sample)
        produced_entry = self.vhost_contents.get_host_file_entries()

        self.assertEqual(expected_vhost_entry, produced_entry)


    def test_correct_host_entry_name_2(self):

        vhost_name_sample = "local.phpmyadmin"

        expected_vhost_entry = "\n127.0.0.1 " + vhost_name_sample + "\n"
        expected_vhost_entry += "::1 " + vhost_name_sample

        self.vhost_contents.set_hostname(vhost_name_sample)
        produced_entry = self.vhost_contents.get_host_file_entries()

        self.assertEqual(expected_vhost_entry, produced_entry)


    def test_get_vhost_entries_without_hotname_setted(self):
        with self.assertRaises(Exception):
            self.vhost_contents.get_host_file_entries()


    def test_get_vhost_configurations_without_vhost_root_folder(self):
        with self.assertRaises(Exception):
            self.vhost_contents.get_vhost_configurations()


    def test_get_vhost_configuration_content(self):

        sample_vhost_name = "local.testing_vhost"
        sample_path = os.path.join("var", "www", sample_vhost_name)

        expected_vhost_configuration = "\n" +\
            "<VirtualHost *:80>\n" +\
            "  DocumentRoot " + sample_path + "\n" +\
            "  ServerName " + sample_vhost_name + "\n" +\
            "  <Directory />\n" +\
            "    Require all granted\n" +\
            "    Options FollowSymLinks\n" +\
            "    AllowOverride All\n" +\
            "  </Directory>\n" +\
            "</VirtualHost>\n"

        self.vhost_contents.set_vhost_root_folder(sample_path)
        self.vhost_contents.set_hostname(sample_vhost_name)
        configurations_getted = self.vhost_contents.get_vhost_configurations()

        self.assertEqual(expected_vhost_configuration, configurations_getted)
