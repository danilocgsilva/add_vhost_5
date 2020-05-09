from add_vhost_5.File_Guesser_Interface import File_Guesser_Interface
from add_vhost_5.Posix_File_Guesser import Posix_File_Guesser
from add_vhost_5.Windows_File_Guesser import Windows_File_Guesser

class File_Guesser(File_Guesser_Interface):

    def set_os(self, os: str):

        if os == 'posix':
            self.file_guesser = Posix_File_Guesser()
        elif os == 'nt':
            self.file_guesser = Posix_File_Guesser()
        else:
            raise Exception('Only values of "posix" or "nt" are allowed')


    def guess_hosts_file(self):
        return self.file_guesser.guess_hosts_file()

