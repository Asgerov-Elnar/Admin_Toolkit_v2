from utils.helper import run
from utils.logger import log

def interfaces():
    log("Viewed network interfaces")
    return run("ip a")

def open_ports():
    log("Checked open ports")
    return run("ss -tulnp")

def arp_scan():
    log("ARP scan")
    return run("ip neigh")
