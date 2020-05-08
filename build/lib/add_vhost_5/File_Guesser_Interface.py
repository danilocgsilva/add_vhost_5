import abc

class File_Guesser_Interface(abc.ABC):

    @abc.abstractmethod
    def guess_hosts_file(self) -> str:
        pass