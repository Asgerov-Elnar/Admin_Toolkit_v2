from datetime import datetime

LOG_FILE = "logs/admin.log"

def log(action):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {action}\n")
