from add_vhost_5.Checking_Steps_Result import Checking_Steps_Result
from add_vhost_5.File_Guesser import File_Guesser
from add_vhost_5.File_Checker import File_Checker

class Steps_Checker:

    def check_host(self, platform: str) -> dict:

        checking_steps_result = Checking_Steps_Result()

        try:
            file_guesser = File_Guesser().set_os(platform)
            host_file_path = file_guesser.guess_hosts_file()
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




