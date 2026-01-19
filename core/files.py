from utils.helper import run
from utils.logger import log

def disk_usage():
    log("Checked disk usage")
    return run("du -sh /* 2>/dev/null")

def big_files():
    log("Checked big files")
    return run("find / -type f -size +100M 2>/dev/null | head")
