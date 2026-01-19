# 🛠️ Admin Tool V2 (ROOT Only)

LX Admin Tool is a **modular, root-only Linux administration toolkit** written in Python.  
It is designed for **system administrators, security engineers, DevOps engineers, and power users** who need a clean and practical CLI tool for daily Linux administration tasks.

This project is **not a toy** — it uses real system commands and requires **root privileges** to operate.

---

## ⚠️ Important Notice

- This tool **ONLY works with root privileges**
- Designed for **Linux systems** or **Windows via WSL**
- ❌ Not supported on Windows CMD / PowerShell directly

---

## 📸 Screenshots

> Create a `screenshots/` directory and add images

```text
screenshots/
├── menu.png
├── system_info.png
├── network.png
├── security.png

![Main Menu](screenshots/menu.png)
![System Info](screenshots/system_info.png)
```
🚀 Features
🖥 System Information

OS & Kernel details

CPU, RAM, Disk usage

Uptime & hostname

🌐 Network

Network interfaces

Open ports

ARP scan (connected devices)

👤 User Management (Root Only)

List system users

Add users

Delete users

⚙️ Service Management

List running services

Restart services

🔐 Security

SSH service status

Failed SSH login attempts

World-writable file detection

📁 File System

Disk usage overview

Large file detection (>100MB)

📝 Logging

All actions are logged

Log file: logs/admin.log

---

## Project Structure
```text
lx_admin_tool/
│
├── main.py
│
├── core/
│   ├── system.py
│   ├── network.py
│   ├── users.py
│   ├── services.py
│   ├── security.py
│   └── files.py
│
├── utils/
│   ├── helper.py
│   ├── logger.py
│   └── root_check.py
│
├── logs/
│   └── admin.log
│
├── screenshots/
│
├── README.md
└── LICENSE
```
---

## 🔐 Root Requirement

```bash
sudo python3 main.py
```
---

## 🧑‍💻 Installation

```bash
git clone https://github.com/YOUR_USERNAME/lx-admin-tool.git
cd Admin_toolkit_v2
sudo python3 main.py
```
