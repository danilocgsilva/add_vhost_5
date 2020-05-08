from add_vhost_5.File_Checker import File_Checker
from add_vhost_5.Windows_File_Guesser import Windows_File_Guesser
from add_vhost_5.Posix_File_Guesser import Posix_File_Guesser

def main():

    windows_file_guesser = Windows_File_Guesser()
    posix_file_guesser = Posix_File_Guesser()

    file_checker = File_Checker(windows_file_guesser.guess_hosts_file())

    if file_checker.exists():
        print("The file exists")
    else:
        print("The file does not exists!!")

    if file_checker.is_writable():
        print("The file is writable!")
    else:
        print("No Permission to wirte in file!")


