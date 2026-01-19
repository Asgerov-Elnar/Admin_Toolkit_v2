import platform
from utils.helper import run
from utils.logger import log

def info():
    log("Viewed system info")
    return f"""
OS: {platform.system()} {platform.release()}
Kernel: {platform.version()}
Uptime: {run("uptime -p")}
CPU: {run("lscpu | grep 'Model name'")}
RAM:
{run("free -h")}
Disk:
{run("df -h")}
"""
