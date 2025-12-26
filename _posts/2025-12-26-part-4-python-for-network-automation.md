---
title: "Part 4 — Python for Network Automation (Beginner-Friendly)"
header:
 image: /assets/images/python-virtual-environment.webp
last_modified_at: 2025-12-26
categories:
 - NetDevOps
 - Python
tags:
 - Netmiko
 - NAPALM
toc: true
toc_sticky: true
---

## Removing the Fear of Coding
Many network engineers have never written code beyond bash scripts. The thought of "becoming a programmer" feels daunting. Here's the reality: you don't need to be a programmer to write effective network automation. You need to understand basic programming concepts and know the libraries that exist.

### Python Basics for Networking
**Why Python specifically?** Python's syntax closely resembles English and requires minimal boilerplate compared to many other languages.

**Fundamental Concepts (Network Context):**

Variables, lists, dictionaries, loops, and conditionals are the building blocks:

```python
router_ip = "192.168.1.1"
username = "admin"
password = "cisco123"

routers = ["192.168.1.1", "192.168.2.1", "192.168.3.1"]

device = {
  "host": "192.168.1.1",
  "username": "admin",
  "password": "cisco123",
  "device_type": "cisco_ios"
}

for router in routers:
  # connect to router and run commands
  pass

if device_uptime < 1000:
  alert("Device rebooted!")
```

### Netmiko: SSH Automation Library
Netmiko abstracts SSH complexity, handling device prompts, command execution, and response parsing, making multi-device SSH automation trivial.

```python
from netmiko import ConnectHandler

device = {
  "device_type": "cisco_ios",
  "host": "192.168.1.1",
  "username": "admin",
  "password": "password"
}

connection = ConnectHandler(**device)
routes = connection.send_command("show ip route")
print(routes)
connection.disconnect()
```

### NAPALM: Multi-Vendor Abstraction
NAPALM provides vendor-agnostic getters and configuration helpers:

```python
from napalm import get_network_driver

driver = get_network_driver("ios")
connection = driver("192.168.1.1", "admin", "password")
connection.open()
facts = connection.get_facts()
print(facts)
```

### Practical Use Cases
**Pre/Post Change Validation** — gather baseline and compare after a change.

```python
from netmiko import ConnectHandler

conn = ConnectHandler(**device)
routes_before = conn.send_command("show ip route")
# apply change
routes_after = conn.send_command("show ip route")
if routes_before != routes_after:
  print("⚠️ Routes changed!")
```

**Automated Config Backup**

```python
from netmiko import ConnectHandler
from datetime import datetime
import os

devices = [{"device_type": "cisco_ios", "host": "10.1.1.1", "username": "admin", ...}]
backup_dir = f"backups/{datetime.now().strftime('%Y-%m-%d')}"
os.makedirs(backup_dir, exist_ok=True)

for device in devices:
  conn = ConnectHandler(**device)
  config = conn.send_command("show running-config")
  with open(f"{backup_dir}/{device['host']}.config", 'w') as f:
    f.write(config)
  conn.disconnect()
```

**Automated Compliance Checks**

```python
from napalm import get_network_driver

def check_ntp_configured(device):
  driver = get_network_driver(device["os"])
  conn = driver(device["host"], device["user"], device["pass"])
  conn.open()
  config = conn.get_config()
  return "ntp" in config.lower()
```

### Key Takeaway
Python for network automation is about knowing which libraries to use and getting comfortable with small, repeatable scripts that solve real problems.

**Try this now:** Write a short script that connects to one device with Netmiko, runs `show version`, and appends a line to `devices_report.md` with hostname and OS version.

**Next:** Part 5 — Ansible for network automation.