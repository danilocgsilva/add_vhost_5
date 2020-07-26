import subprocess

class Environment:

    def restart_webserver(self):

        process = subprocess.Popen(['service', 'apache2', 'restart']);
        try:
            process.communicate()
            return True
        except Exception:
            return False
