import abc

class File_Guesser_Interface(abc.ABC):

    @abc.abstractmethod
    def guess_hosts_file(self) -> str:
        pass

    
    @abc.abstractmethod
    def guess_vhosts_configuration_path(self) -> str:
        pass