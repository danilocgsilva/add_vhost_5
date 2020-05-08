from add_vhost_5.File_Guesser_Interface import File_Guesser_Interface

class Posix_File_Guesser(File_Guesser_Interface):
    def guess_hosts_file(self) -> str:
        return "/etc/hosts"
