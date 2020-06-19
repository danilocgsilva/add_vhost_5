import unittest
import sys
import os
sys.path.append("..")
from add_vhost_5.File_Guesser import File_Guesser

class test_File_Guesser_Linux(unittest.TestCase):

    def test_guess_vhost_file(self):
        server_name = 'my_testing_name_server'
        expected_path = os.sep + os.path.join('etc', 'httpd', 'conf', 'vhosts', server_name + '.conf')
        file_guesser = File_Guesser()
