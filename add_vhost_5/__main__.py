from add_vhost_5.File_Checker import File_Checker
from add_vhost_5.File_Guesser import File_Guesser
from add_vhost_5.File_Writter import File_Writter
from add_vhost_5.VHost_Contents import VHost_Contents
from sys import platform
import sys

def main():

    if not first_argument_provided():
        print("The first argument has not been provided.")
        exit()

    file_guesser = File_Guesser().set_os(platform)
    file_checker = File_Checker()

    host_file_path = file_guesser.guess_hosts_file()
    exit_if_not_writable(file_checker, host_file_path, "The hosts file " + host_file_path + " is not writable. Needs higher privileges to execute the action.")

    host_name = get_first_argument()

    vhost_configuration_file_path = file_guesser.guess_vhosts_configuration_path(host_name)
    exit_if_not_writable(file_checker, vhost_configuration_file_path, "The virtual host file configuration " + vhost_configuration_file_path + " is not writable. Needs higher privileges to execute the action.")

    file_guesser.set_hostname(host_name)

    full_physical_www_path = file_guesser.get_full_physical_path()
    welcome_index = file_guesser.get_welcome_index()

    file_writter = File_Writter()
    file_contents = VHost_Contents().\
        set_hostname(host_name).\
        set_vhost_root_folder(full_physical_www_path)

    file_writter.set_file_path(host_file_path)\
        .write(
            file_contents.get_host_file_entries()
        )

    file_writter.set_file_path(vhost_configuration_file_path)\
        .write(
            file_contents.get_vhost_configurations()
        )

    file_writter.set_file_path(welcome_index)\
        .new()\
        .write(
            file_contents.get_welcome_html()
        )

    print("Finished! Restart your running webserver service. Access http://" + host_name)
    print("You can find your virtualhost index in the " + welcome_index)
    
    
def exit_if_not_writable(file_checker: File_Checker, file: str, message: str):
    if not file_checker.set_file(file).is_writable():
        print(message)
        exit()


def first_argument_provided():
    try:
        sys.argv[1]
        return True
    except(IndexError):
        return False


def get_first_argument():
    return sys.argv[1]

