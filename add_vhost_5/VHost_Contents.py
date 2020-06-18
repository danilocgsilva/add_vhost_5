import os

class VHost_Contents:

    def set_hostname(self, hostname: str):
        self.hostname = hostname
        return self


    def set_vhost_root_folder(self, vhost_root_folder: str):
        self.vhost_root_folder = vhost_root_folder
        return self


    def get_host_file_entries(self) -> str:

        vhost_entry = "\n127.0.0.1 " + self.hostname + "\n"
        vhost_entry += "::1 " + self.hostname

        return vhost_entry


    def get_vhost_configurations(self) -> str:

        vhost_configuration_content = "\n" +\
            "<VirtualHost *:80>\n" +\
            "  DocumentRoot " + self.vhost_root_folder + "\n" +\
            "  ServerName " + self.hostname + "\n" +\
            "  <Directory />\n" +\
            "    Require all granted\n" +\
            "    Options FollowSymLinks\n" +\
            "    AllowOverride All\n" +\
            "  </Directory>\n" +\
            "</VirtualHost>\n"
        
        return vhost_configuration_content


    def get_welcome_html(self) -> str:
        return 'Hello (world)! Welcome to the first sight of your virtual host ' + self.hostname
