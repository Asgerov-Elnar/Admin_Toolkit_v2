from utils.helper import run
from utils.logger import log

def ssh_status():
    log("Checked SSH status")
    return run("systemctl status ssh --no-pager")

def failed_logins():
    log("Checked failed SSH logins")
    return run("journalctl -u ssh | grep Failed | tail")

def world_writable():
    log("Scanned world writable files")
    return run("find / -type f -perm -0002 2>/dev/null | head")
