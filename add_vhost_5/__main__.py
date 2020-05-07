from add_vhost_5.File_Checker import File_Checker

def main():

    file_checker = File_Checker('/etc/host')

    if file_checker.exists():
        print("The file exists")
    else:
        print("The file does not exists!!")

    if file_checker.writable():
        print("The file is writable!")
    else:
        print("No Permission to wirte in file!")


