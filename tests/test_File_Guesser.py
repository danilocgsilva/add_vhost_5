import unittest
import sys
sys.path.append("..")
from add_vhost_5.File_Guesser import File_Guesser


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


if __name__ == '__main__':
    unittest.main()
