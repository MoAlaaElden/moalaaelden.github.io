---
title: "Bash script for Ubuntu Server Initial Setup and Package Installation Script"
header:
  image: /assets/images/bash-script-ubuntu-server-initial-setup-and-package-installation-script.png
last_modified_at: 2024-12-05
categories:
  - Bash-Script
  - Linux
  - Ubuntu
  - Server
tags:
  - Bash-Script
  - Linux
  - Filesystem
  - Ubuntu
  - Root
toc: true # On this page
toc_sticky: true # Sticky Table of Contents
---

# Ubuntu Server Initial Setup and Package Installation Script

This is a Bash script to update and upgrade Ubuntu, and install the necessary packages. I'll create a comprehensive script that includes best practices for server setup.

```bash
#!/bin/bash

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root (use sudo)" 
   exit 1
fi

# Update package lists
echo "Updating package lists..."
apt update

# Upgrade existing packages
echo "Upgrading existing packages..."
apt upgrade -y

# Install essential utilities
echo "Installing essential utilities..."
apt install -y \
    net-tools \
    wget \
    curl \
    software-properties-common \
    ca-certificates \
    gnupg \
    lsb-release

# Install Docker dependencies
echo "Preparing to install Docker..."
# Remove any existing Docker installations
apt-get remove -y docker docker-engine docker.io containerd runc

# Add Docker's official GPG key
mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up the Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package lists again to include Docker repository
apt update

# Install Docker Engine, Containerd, and Docker Compose
echo "Installing Docker and Docker Compose..."
apt install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin

# Check the status of Docker Engine
systemctl status docker

# Link Docker Compose to the executable and grant execution permissions.
ln -s /usr/libexec/docker/cli-plugins/docker-compose /usr/bin/docker-compose
chmod u+x /usr/bin/docker-compose

# Detect the current user (for non-root operations)
CURRENT_USER=$(logname)

# Add current user to docker group
usermod -aG docker $CURRENT_USER

# Activate the changes to groups
newgrp docker

# Clean up
echo "Cleaning up..."
apt autoremove -y
apt autoclean

echo "Server setup complete!"
echo "Installed: net-tools, Docker, Docker-Compose"

# Check Docker version
docker-compose -v

# Check Docker Compose version
docker -v

```

## Here's a breakdown of what the script does:

1. Checks if the script is run with sudo/root privileges
2. Updates package lists
3. Upgrades all existing packages
4. Installs essential utilities
5. Removes any existing Docker installations
6. Adds Docker's official repository and GPG key
7. Installs Docker Engine, Docker CLI, Containerd, and Docker Compose
8. Cleans up unnecessary packages

## A few important notes:
- The script uses `-y` to automatically answer "yes" to prompts
- It follows Docker's official installation instructions for Ubuntu

## To use the script:
1. Save it to a file (e.g., `ubuntu-setup.sh`)
2. Make it executable: `chmod +x ubuntu-setup.sh`
3. Run with sudo: `sudo ./ubuntu-setup.sh`


[Reference and more details:](https://moalaaelden.wordpress.com/2022/10/24/install-docker-engine-on-ubuntu-18-04-lts-20-04-lts-21-10-lts-22-04-lts-2/ "MoAlaaElden")