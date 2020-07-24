import os

class Linux_VHost_Guesser:

    def guess_vhost_configuration(self, hostname):
        base_fedora = os.sep + os.path.join('etc', 'httpd', 'conf', 'vhosts')
        base_debian = os.sep + os.path.join('etc', 'apache2', 'sites-enabled')
        host_configuration_file_name = hostname + '.conf'

        if os.path.isdir(base_fedora):
            return os.path.join(base_fedora, host_configuration_file_name)

        if os.path.isdir(base_debian):
            return os.path.join(base_debian, host_configuration_file_name)

        raise Exception('I could not any valid path for vhost configuration.')
