from add_vhost_5.File_Guesser_Interface import File_Guesser_Interface

class Windows_File_Guesser(File_Guesser_Interface):
    def guess_hosts_file(self) -> str:
        return "C:\\Windows\\System32\\drivers\\etc\\hosts"