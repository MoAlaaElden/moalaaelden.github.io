---
title: "Bash script for Network Automation Python Development Environment Setup"
header:
  image: /assets/images/bash-script-for-network-automation-python-development-environment-setup.jpg
last_modified_at: 2024-12-05
categories:
  - Bash-Script
  - Python
  - Paramiko
  - Netmiko
  - NAPALM
  - Network-Automation
  - NetDevOps
tags:
  - Bash-Script
  - Python
  - Paramiko
  - Netmiko
  - NAPALM
  - Network-Automation
  - NetDevOps
toc: true # On this page
toc_sticky: true # Sticky Table of Contents
---

This is a comprehensive Bash script for setting up a Python virtual environment tailored for network automation engineers.

```bash
#!/bin/bash

# Ensure the script is run with sudo privileges
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root (use sudo)" 
   exit 1
fi

# Detect the current user (for non-root operations)
CURRENT_USER=$(logname)

# Update package lists
echo "Updating package lists..."
apt update

# Install system dependencies
echo "Installing system dependencies..."
apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    graphviz \
    libgraphviz-dev \
    pkg-config \
    snmp \
    libsnmp-dev \
    git \
    wget \
    curl

# Create a directory for Python projects
echo "Creating Python projects directory..."
mkdir -p /home/$CURRENT_USER/python-projects/network-automation
cd /home/$CURRENT_USER/python-projects/network-automation

# Create a virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip and setuptools
echo "Upgrading pip and setuptools..."
pip install --upgrade pip setuptools wheel

# Install network automation libraries
echo "Installing network automation libraries..."
pip install \
    netmiko \
    napalm \
    nornir \
    pyats[full] \
    networkx \
    textfsm \
    python-dotenv \
    pyyaml \
    easysnmp \
    graphviz \
    paramiko \
    jinja2 \
    netaddr \
    scapy \
    ansible \
    requests \
    rich \
    tabulate \
    pandas \
    pytest \
    black \
    pylint \
    mypy

# Additional useful libraries for network engineers
echo "Installing additional useful libraries..."
pip install \
    ipython \
    ipdb \
    openpyxl \
    xlrd \
    cryptography \
    netmiko \
    nornir-netmiko \
    nornir-utils

# Create a requirements.txt file
echo "Creating requirements.txt file..."
pip freeze > requirements.txt

# Set up Git configuration (optional)
echo "Configuring Git..."
git config --global user.name "Mohamed Alaa"
git config --global user.email "mohammed.3laa@gmail.com"

# Deactivate virtual environment
deactivate

# Set proper permissions
chown -R $CURRENT_USER:$CURRENT_USER /home/$CURRENT_USER/python-projects

# Create a startup script to activate the venv
echo "Creating venv activation script..."
cat << EOF > /home/$CURRENT_USER/.network-automation-venv.sh
#!/bin/bash
source /home/$CURRENT_USER/python-projects/network-automation/venv/bin/activate
EOF
chmod +x /home/$CURRENT_USER/.network-automation-venv.sh

# Optionally add to .bashrc
echo "Adding venv activation to .bashrc..."
echo '# Activate Network Automation Python venv' >> /home/$CURRENT_USER/.bashrc
echo '[ -f ~/.network-automation-venv.sh ] && source ~/.network-automation-venv.sh' >> /home/$CURRENT_USER/.bashrc

# Final instructions
echo "Python Network Automation Environment Setup Complete!"
echo "Virtual Environment Location: /home/$CURRENT_USER/python-projects/network-automation/venv"
echo "To activate: source ~/python-projects/network-automation/venv/bin/activate"

```

Here's a breakdown of what the script does:

1. Checks for sudo privileges
2. Installs system-level dependencies
3. Creates a dedicated directory for Python projects
4. Sets up a Python virtual environment
5. Installs a comprehensive set of network automation libraries:
   - Core network automation libraries: Netmiko, NAPALM, Nornir, pyATS
   - Data manipulation: NetworkX, TextFSM, PyYAML
   - Utility libraries: python-dotenv, graphviz
   - Additional networking tools: Paramiko, Scapy, Netaddr
   - Development tools: Black, Pylint, Pytest
   - Extras: Pandas, Rich, Tabulate

Key features:
- Creates a virtual environment in `~/python-projects/network-automation/venv`
- Generates a `requirements.txt` file
- Adds a startup script to automatically activate the venv
- Sets up basic Git configuration

To use the script:
1. Save it as `network-automation-setup.sh`
2. Make it executable: `chmod +x network-automation-setup.sh`
3. Run with sudo: `sudo ./network-automation-setup.sh`

Post-installation:
- Restart your terminal or run `source ~/.bashrc`
- The virtual environment will automatically activate when you open a new terminal

