---
title: "Are you know the difference between LXC vs LXD vs Docker Containers? let’s see it."
header:
  image: /assets/images/2022-10-22-post-lxc-lxd-docker.webp
last_modified_at: 2022-10-22
categories:
  - Docker
  - LXC
  - LXD
tags:
  - Application-Containers
  - Containers
  - System-Containers
  - Network-Automation
  - Ubuntu
  - Virtual-Machine
  - Virtualization
  - Hyper-V
  - Linux
toc: true # On this page
toc_sticky: true # Sticky Table of Contents
---


### Types of containers:

#### System containers 
System containers (as run by **LXD**) are similar to virtual or physical machines.

- They run a **full operating system** inside them, you can run any type of workload, and you manage them exactly as you would a virtual or a physical machine.
- System containers could host several applications within a single system container.
- System containers run a full operating system giving them flexibility for the workload types they support.

#### Application containers
**Application containers** (such as **Docker**), also known as process containers, as it runs a single process or a service per container.

- These containers are temporary, and you can **create**, **delete** and **replace** containers easily as needed.
- Application containers run a **single app/process**.

> **Both application and system containers share a kernel with the host operating system.**

### LXC vs LXD vs Docker

**LXC** is the technology allowing the segmentation of your system into independent containers.

**LXD** is a daemon running on top of LXC for running system containers. When it comes to storage, networking, and logging, LXD supports a variety of interfaces and features. Functionality-wise, **LXD is similar to VMWare or KVM hypervisors**, but is **much lighter on resources** and removes the usual virtualization overhead.

**Docker** is a containerization platform, specifically designed for **microservice architecture**, providing a way to **decompose and isolate individual processes**, which can then be scaled independently from the rest of the application or system they are a part of. 

### Running Docker in LXD

You can use **LXD** to create your **virtual systems** running **inside the container**s, segment them as you like, and easily **use Docker** to get the **actual service running** inside the container.
