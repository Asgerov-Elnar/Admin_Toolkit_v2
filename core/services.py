import os
from utils.helper import run
from utils.logger import log

def running():
    log("Listed running services")
    return run("systemctl list-units --type=service --state=running")

def restart(s):
    log(f"Restarted service {s}")
    os.system(f"systemctl restart {s}")
