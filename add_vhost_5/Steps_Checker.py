from add_vhost_5.Checking_Steps_Result import Checking_Steps_Result
from add_vhost_5.File_Guesser import File_Guesser
from add_vhost_5.File_Checker import File_Checker

class Steps_Checker:

    def __init__(self):
        self.vhost_configuration_file_path = None
        self.file_guesser = File_Guesser()

    def check_host(self, platform: str) -> dict:
        checking_steps_result = Checking_Steps_Result()
        try:
            self.file_guesser.set_os(platform)
            host_file_path = self.file_guesser.guess_hosts_file()
        except Exception:
            checking_steps_result.setProblem()
            checking_steps_result.setMessage("The host file has not been found in the system.")
            return checking_steps_result.getResponseResult()

        file_checker = File_Checker()
        file_checker.set_file(host_file_path)
        if file_checker.is_writable():
            checking_steps_result.setOk()
            return checking_steps_result.getResponseResult()
        else:
            checking_steps_result.setPartial() 
            checking_steps_result.setMessage("The hosts file exists, but have no permission to write. Try to execute with a user with elevated privileges over the hosts file.")
            return checking_steps_result.getResponseResult()

    def check_configuration_file(self, host_name: str) -> dict:
        checking_steps_result = Checking_Steps_Result()
        try:
            self.vhost_configuration_file_path = self.file_guesser.guess_vhosts_configuration_path(host_name)
            checking_steps_result.setOk()
            return checking_steps_result.getResponseResult()
        except Exception as ex:
            checking_steps_result.setProblem()
            checking_steps_result.setMessage(str(ex))
            return checking_steps_result.getResponseResult()

    def get_vhost_configuration_file_path(self) -> str:
        return self.vhost_configuration_file_path



