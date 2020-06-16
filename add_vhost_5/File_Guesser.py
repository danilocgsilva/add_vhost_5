from add_vhost_5.File_Guesser_Interface import File_Guesser_Interface
from add_vhost_5.Windows_File_Guesser import Windows_File_Guesser
from add_vhost_5.Os_Definition_Exception import Os_Definition_Exception
import os

class File_Guesser(File_Guesser_Interface):

    def set_os(self, os: str):

        if os not in ['linux', 'darwin', 'win32']:
            raise Os_Definition_Exception('The only aceptable values for this method is "linux", "darwin" or "win32"')

        self.os = os
        
        return self


    def guess_hosts_file(self) -> str:

        self.config_root()

        if self.os == 'win32':
            expected_file = self.root + os.path.join('System32', 'drivers', 'hosts')
        else:
            expected_file = self.root + os.path.join('etc', 'hosts')

        if not os.path.isfile(expected_file):
            raise Exception("I do not have found the expected file in the system.")

        return expected_file


    def set_root(self, root: str):
        self.root = root + os.sep
        return self


    def guess_vhosts_configuration_path(self) -> str:

        self.config_root()

        if self.os == 'win32':
            virtual_host_file_path = self.root + os.path.join('wamp64', 'bin', 'apache', 'apache2.4.41', 'conf', 'extra', 'httpd-vhosts.conf')
        else:
            raise Exception("Other operational systems than Windows still not implemented.")

        return virtual_host_file_path


    def config_root(self):

        if self.os == 'win32':
            self.set_root_if_not_setted("C:" + os.sep)
        else:
            self.set_root_if_not_setted(os.sep)



    def set_root_if_not_setted(self, root: str):
        if not hasattr(self, 'root'):
            self.root = root
        return self