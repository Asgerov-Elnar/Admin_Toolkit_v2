from utils.root_check import require_root
from utils.helper import clear
from core import system, network, users, services, security, files

require_root()

while True:
    clear()
    print("""
==== LX ADMIN TOOL (ROOT ONLY) ====

1. System Info
2. Network Interfaces
3. Open Ports
4. ARP Scan
5. List Users
6. Add User
7. Delete User
8. Running Services
9. Restart Service
10. SSH Status
11. Failed Logins
12. World Writable Files
13. Disk Usage
14. Big Files
0. Exit
""")

    c = input("> ")

    if c == "1": print(system.info())
    elif c == "2": print(network.interfaces())
    elif c == "3": print(network.open_ports())
    elif c == "4": print(network.arp_scan())
    elif c == "5": print(users.list_users())
    elif c == "6": users.add_user(input("Username: "))
    elif c == "7": users.del_user(input("Username: "))
    elif c == "8": print(services.running())
    elif c == "9": services.restart(input("Service: "))
    elif c == "10": print(security.ssh_status())
    elif c == "11": print(security.failed_logins())
    elif c == "12": print(security.world_writable())
    elif c == "13": print(files.disk_usage())
    elif c == "14": print(files.big_files())
    elif c == "0": break

    input("\nEnter to continue...")
