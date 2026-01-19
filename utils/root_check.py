import os, sys

def require_root():
    if os.geteuid() != 0:
        print("[!] This tool MUST be run as ROOT")
        print("[!] Use: sudo python3 main.py")
        sys.exit(1)
