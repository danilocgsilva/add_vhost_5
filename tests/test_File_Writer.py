import os
import shutil
import sys
import tempfile
import unittest
sys.path.append("..")
from add_vhost_5.File_Writter import File_Writter

class test_File_Writer(unittest.TestCase):

    def setUp(self):
        self.file_writter = File_Writter()

    
    def test_if_halts_when_writting_to_non_existing_file(self):
        self.file_writter.set_file_path("non_existing_file")
        with self.assertRaises(Exception):
            self.file_writter.write("Any content")


    def test_halts_when_tries_to_write_without_file_definition(self):
        with self.assertRaises(Exception):
            self.file_writter.write("Any content")


    def test_added_line_count(self):

        self.create_physical_file_for_testing()

        initial_content_length = self.count_file_lines(self.temporary_file_location)

        self.file_writter.set_file_path(self.temporary_file_location)
        self.file_writter.write("Some content")

        new_length = self.count_file_lines(self.temporary_file_location)

        self.assertEqual(initial_content_length, new_length - 1)


    def test_add_multiple_content_lines(self):
        self.create_physical_file_for_testing()
        self.file_writter.set_file_path(self.temporary_file_location)
        self.file_writter.write("Test Content")
        self.file_writter.write("Second line content")
        self.file_writter.write("Third line")
        line_file_counting = self.count_file_lines(self.temporary_file_location)
        self.assertEqual(3, line_file_counting)


    def test_add_single_content_lines(self):
        self.create_physical_file_for_testing()
        self.file_writter.set_file_path(self.temporary_file_location)
        self.file_writter.write("Test Content single line")
        line_file_counting = self.count_file_lines(self.temporary_file_location)
        self.assertEqual(1, line_file_counting)

    
    def test_is_file_writable_exception_case_file_not_setted(self):
        with self.assertRaises(Exception):
            self.file_writter.is_file_writable()


    def test_file_is_writable(self):
        self.create_physical_file_for_testing()
        self.file_writter.set_file_path(self.temporary_file_location)
        self.assertTrue(self.file_writter.is_file_writable())


    def create_physical_file_for_testing(self):
        self.temporary_file_location = os.path.join(tempfile.gettempdir(), 'tempfile')

        if os.path.isfile(self.temporary_file_location):
            os.remove(self.temporary_file_location)

        open(self.temporary_file_location, 'a').close()


    def count_file_lines(self, file) -> int:

        file = open(file, "r")
        content_list = file.readlines()
        file.close()

        return len(content_list)


    def test_new(self):

        file_to_be_created = os.path.join(
            tempfile.gettempdir(), 'just_created_file.txt'
        )

        self.file_writter.set_file_path(file_to_be_created).new()

        self.assertTrue(os.path.isfile(file_to_be_created))


    def test_new_long_folder_string(self):

        just_created_file_base = os.path.join(tempfile.gettempdir(), 'just_created_file')

        if os.path.exists(just_created_file_base):
            shutil.rmtree(just_created_file_base, ignore_errors=False, onerror=None)

        file_to_be_created = os.path.join(
            just_created_file_base, 'little', 'longer', 'folder', 'path.txt'
        )

        self.file_writter.set_file_path(file_to_be_created).new()

        self.assertTrue(os.path.isfile(file_to_be_created))