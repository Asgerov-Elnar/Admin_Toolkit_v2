import subprocess, os

def run(cmd):
    return subprocess.getoutput(cmd)

def clear():
    os.system("clear")
