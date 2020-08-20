from add_vhost_5.File_Checker import File_Checker
from add_vhost_5.File_Guesser import File_Guesser
from add_vhost_5.File_Writter import File_Writter
from add_vhost_5.VHost_Contents import VHost_Contents
from add_vhost_5.Environment import Environment
from add_vhost_5.Steps_Checker import Steps_Checker
from sys import platform
import sys

def avhost():

    if not first_argument_provided():
        print("The first argument has not been provided.")
        exit()

    file_guesser = File_Guesser().set_os(platform)
    file_checker = File_Checker()
    steps_cheker = Steps_Checker()

    results = steps_cheker.check_host(platform)
    if not results["status"] == "Ok":
        if results["status"] == "Partial":
            print("The host file has been found, but is not writable. Try to run the script with elevated privileges over hosts files.")
        elif results["status"] == "Problem":
            print("The host file has not been found in the system.")
        else:
            raise Exception("I did not understood the Steps_Checker response. Sorry.")
        exit()

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

    environment = Environment()
    if not environment.restart_webserver():
        print("I could not restart the environment, sorry. You need to do it manually.")


def avhostcheck():
    steps_cheker = Steps_Checker()
    results = steps_cheker.check_host()
    if results["status"] == "Ok":
        print("The host file has been found and is writable by the system.")
    elif results["status"] == "Partial":
        print("The host file has been found, but have no permissions to write in. Tries to use an user with elevated privileges.")
    elif results["status"] == "Problem":
        print("I have not found the hosts file in the system.")
    else:
        raise Exception("Do not understood the Steps_Checker response result. Sorry.")


def first_argument_provided():
    try:
        sys.argv[1]
        return True
    except(IndexError):
        return False


def get_first_argument():
    return sys.argv[1]

