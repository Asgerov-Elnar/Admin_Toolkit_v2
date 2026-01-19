import os
from utils.helper import run
from utils.logger import log

def list_users():
    log("Listed users")
    return run("cut -d: -f1 /etc/passwd")

def add_user(u):
    log(f"Added user {u}")
    os.system(f"useradd {u}")
    os.system(f"passwd {u}")

def del_user(u):
    log(f"Deleted user {u}")
    os.system(f"userdel -r {u}")
