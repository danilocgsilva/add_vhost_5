from add_vhost_5.File_Guesser_Interface import File_Guesser_Interface
from add_vhost_5.Os_Definition_Exception import Os_Definition_Exception
from add_vhost_5.Linux_VHost_Guesser import Linux_VHost_Guesser
from add_vhost_5.File_Writter import File_Writter
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
            expected_file = self.root + os.path.join('Windows', 'System32', 'drivers', 'etc', 'hosts')
        else:
            expected_file = self.root + os.path.join('etc', 'hosts')

        if not os.path.isfile(expected_file):
            raise Exception("I do not have found the expected file in the system.")

        return expected_file

    def set_root(self, root: str):
        self.root = root + os.sep
        return self

    def get_root_with_separator(self):
        return self.root

    def get_full_physical_path(self):
        self.config_root()
        self.config_www()
        return self.root + os.path.join(self.www, self.hostname)

    def get_welcome_index(self) -> str:
        return os.path.join(self.get_full_physical_path(), 'index.html')
        
    def guess_vhosts_configuration_path(self, hostname = None) -> str:

        self.config_root()
        self.config_www()

        if self.os == 'win32':
            virtual_host_file_path = self.root + os.path.join(self.base_vhost_app, 'bin', 'apache', 'apache2.4.41', 'conf', 'extra', 'httpd-vhosts.conf')
        elif self.os == 'darwin':
            virtual_host_file_path = self.root + os.path.join(self.base_vhost_app, 'XAMPP', 'xamppfiles', 'etc', 'extra', 'httpd-vhosts.conf')
        elif self.os == 'linux':
            virtual_host_file_path = Linux_VHost_Guesser().guess_vhost_configuration(hostname)
            if self.is_debian_like():
                File_Writter().set_file_path(virtual_host_file_path).new()
            else:
                raise Exception("Adding virtual hosts for linux that are not Debian like still is not supported.")
        else:
            raise Exception("Other operational systems than Windows, Mac or Linux still not implemented.")

        if not os.path.isfile(virtual_host_file_path):
            raise Exception("I do not have found the virtual host file on the system.")

        return virtual_host_file_path

    def set_hostname(self, hostname):
        self.hostname = hostname
        return self


    def config_root(self):

        if self.os == 'win32':
            self.set_root_if_not_setted("C:" + os.sep)
        else:
            self.set_root_if_not_setted(os.sep)

    def set_root_if_not_setted(self, root: str):
        if not hasattr(self, 'root'):
            self.root = root
        return self

    def config_www(self):
        if self.os == 'win32':
            self.base_vhost_app = 'wamp64'
            self.www = os.path.join(self.base_vhost_app, 'www')
        elif self.os == 'darwin':
            self.base_vhost_app = 'Applications'
            self.www = os.path.join(self.base_vhost_app, 'www')
        elif self.os == 'linux':
            self.base_vhost_app = ''
            self.www = ''
        else:
            raise Exception("Still not working for other systems than Windows.")

    def is_debian_like(self) -> bool
        return True
