import sys
sys.path.insert(1, "..")
from add_vhost_5.Environment import Environment

environment = Environment()
environment.restart_webserver()

