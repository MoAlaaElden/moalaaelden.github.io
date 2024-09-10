---
title: "How To Start Your Network Automation Journey?"
header:
  overlay_image: /assets/images/Paramiko-Python-For-Network-Engineers.jpg
last_modified_at: 2022-10-31
categories:
  - Python
  - Paramiko
  - Netmiko
  - NAPALM
  - SSH
  - Network-Automation
tags:
  - Python
  - Paramiko
  - Netmiko
  - NAPALM
  - SSH
  - Network-Automation
toc: true # On this page
---
# How To Start Your Network Automation Journey?

- My network automation journey started in 2017 after I was promoted to network automation manager.

- This is the first presentation that I have prepared and presented to my managers in 2017 regarding network automation 🙂

I hope this information will be helpful to start your network automation journey 😉
{: .notice--info}

## IT Automation solutions
- Data Center Automation
- Network Automation
- Business Process Automation
- Cloud Automation
- Server Automation
- Database Automation
- IT Security Automation

## Network Automation

- Next-generation network architectures are growing and becoming more complex.
- Network automation is the process of automating the configuration, management, testing, deployment, and operations of physical and virtual devices within a network.
- The key to a successful network automation project is to keep your eye on tasks that are eating up a great deal of time.
- Whether your network staff is wasting time manually creating status reports for upper management, performing simple moves/adds/changes, or dealing with the same troubleshooting tasks over and over again, your goal should be to identify repetitive tasks and use tools to automate them.

## Traditional Network Design
![Traditional]({{ site.url }}{{ site.baseurl }}/assets/images/traditional-net.png)

## “vSwitches” and “Blade Switches”
![vSwitches]({{ site.url }}{{ site.baseurl }}/assets/images/vSwitches.png)

## “Container technologies” and “Linux Bridge” (lbr)
![Container]({{ site.url }}{{ site.baseurl }}/assets/images/Container.png)

## Operational efficiency

- Getting more work done in less time.
- Automation increases operational efficiency.
- Time saved = Money saved
- Automating the boring stuff and free your staff to innovate.
- Operating costs will drop.

## Henry Ford & the Assembly Line:

- On December 1, 1913, Henry ford installed the first moving assembly line for the mass production of entire automation.
- The assembly line reduced the time it took to build a car by at least 79% – from more than 12 hours to 2 hours and 30 minutes.

## Networking’s Future & How You Can Prepare

- Understanding workflow and processes.
- Any task needs to be achieved and follow some kind of workflow.
- Deeply understand the process and workflow.
- Deeply understand how things work end to end.
- Automation tooling systems.
- The ultimate future of automation networks will take several years to get to that point.
- Now is a great opportunity for network engineers to dig into automation tools and tooling.

## How to get started

- Identify repetitive and time-consuming tasks.
- Determine tasks can be automated.
- Determine what tools will best automate the process or task.
- Perform a security audit on planned automated tasks.
- Configuration and deployment strategy.
- Monitor and maintain automated tasks.
- Optimize and expand.
- Last, continue to improve and build upon your network automation processes.
- Automated tasks can build on each other to create much more complex and intelligent tasks.

## Management interfaces evolution

- VTYs
- SNMP
- Screen Scraping (scripts)
- REST APIs – (Representational state transfer)
- NETCONF protocol – (Network Configuration Protocol) & [YANG]
- NCM (Network Configuration Management)
- Open Source Configuration Management Tools

### VTYs

- Since the early dawn of networking, devices have been configured through VTYs.
- The transport has evolved from telnet to ssh
- The network is configured manually, device-by-device by a human administrator.
- Does not scale and is prone to human error.

### SNMP

- Introduced since 1988 
- The basic idea was to monitor and manage network devices using strictly-defined data structures called MIBs.
- SNMPv1 and v2c, RW community strings were sent over the wire in clear text, thus a security risk.
- SNMP was extensively used for monitoring tasks but failed for configuration tasks.

### Screen Scraping (scripts)

- Logging into devices to screen scrape configurations and state information.
- Scripts to automate specific tasks within environments (changing passwords, ssh key creation, adding/removing VLANs, adding/removing L3 configs, SNMP, NTP, backups…etc)
- Unique scripts for each OS revision that existed at that time (CatOS, IOS…). 
- You can now programmatically deploy 100s of devices with all relevant configuration (security, storage, monitoring, networking, load balancing) in minutes which, in the past, took several weeks.
- Write some scripts to automate tasks using Python libraries to simplify the process.

#### Why Python

- Plenty of libraries and frameworks have been written in Python.
- You can also add modules to Python if you’d like to extend their capabilities.
- When we look at vendor APIs, you can call them easily from Python.
- There are plenty of Python-based open-source projects with large communities and frequent updates with bug fixes and new features.
- Python is well-documented, and more articles are published for network automation, so it’s likely you’ll find the answers to your questions as you learn.

#### Some Python modules and libraries

- telnetlib – Telnet client
- getpass — Portable password input
- Paramiko – SSH
- Netmiko – Multi-vendor library to Paramiko
- Exscript – Telnet and SSH
- cli — command line tools
- Webb – Web Parser and Web Scrapping
- ciscoconfparse – Parse Cisco IOS-style config
- TextFSM – parsing semi-formatted text
- NAPALM – Network Automation and Programmability Abstraction Layer with Multivendor support

### REST APIs – (Representational state transfer)

- REST is an API that allows clients to perform read/write operations on data stored on the server.
- REST uses HTTP to perform a set of actions commonly known as CRUD: [Create – Read – Update – Delete].
- Requests [HTTP verbs GET, POST, PUT, DELETE].
- REST is NOT a protocol but a software architectural pattern.
- To put it in simple words, it describes a way to exchange information rather than the structure of that information.
- Think of it as another transport (like telnet or ssh for VTY) for payloads of any format.
- The most basic use case is a Web application with a client retrieving and updating information on a server.

### NETCONF protocol – (Network Configuration Protocol) & [YANG]

- Is a protocol defined by the IETF to “install, manipulate, and delete the configuration of network devices”. 
- NETCONF operations are realized on top of a Remote Procedure Call (RPC) layer using an XML encoding and provide a basic set of operations to edit and query configuration on a network device.
- Used for programmatic management of network devices.
- Despite being almost 10 years old
- YANG-based network configuration gains greater adoption.

#### NETCONF Capabilities

- writable-running – the running data store can be modified directly.
- candidate – the candidate data store is supported.
- confirmed-commit – the NETCONF server will support the “cancel-commit” and the “confirmed”, “confirm-timeout”, “persist”, and “persist-id” parameters for the “commit” operation.
- rollback-on-error – server will rollback the configuration to the previous state if an error is encountered.
- validate – the server will validate the requested data store or config.
- startup – the startup data store is supported.
- url – the URL data store is supported.
- xpath – filtering can be done using XPATH notation.
- notification – NETCONF asynchronous event messages.

### Junos PyEZ

- Junos PyEZ is a microframework for Python that enables you to manage and automate devices running the Junos operating system (Junos OS).
- Junos PyEZ library relies upon the Junos XML API which uses NETCONF.
- Junos PyEZ enables you to connect to devices running Junos OS using a serial console connection, telnet, or a NETCONF session over SSH using TCP port 830.

#### Junos PyEZ Example

```python
moalaa@R15-MX1# set system services netconf ssh

moalaa@Network-Automation:~$ python2.7
>>> from pprint import pprint
>>> from jnpr.junos import Device
>>> dev = Device (host='192.168.15.241', user='moalaa',password='Test123')
>>> dev.open ()
>>> print dev.facts ['version']
14.1R1.10
>>> print dev.facts ['hostname']
R15-MX1
```

### Cisco YANG Development Kit (YDK)

- A Software Development Kit that provides API’s that are modeled in YANG.
- YDK is for RFC6241 and RFC6020 compliant devices only.
- RFC6241 Network Configuration Protocol (NETCONF)
- RFC6020 YANG – A Data Modeling Language for the Network Configuration Protocol (NETCONF).
- For IOS, this means IOS-XE 16.3.1 or later.
- ServiceProvider instance used to communicate with an OpenDaylight instance.

#### Cisco YANG Development Kit (YDK) Config Example

```python
moalaa@Network-Automation:~/YDK$ sudo pip install ydk-models-cisco-ios-xe

moalaa@Network-Automation:~/YDK$ sudo pip install ydk-models-cisco-ios-xr

RP/0/0/CPU0:R11-XR1(config)#ssh server netconf port 830
RP/0/0/CPU0:R11-XR1(config)#ssh timeout 120
RP/0/0/CPU0:R11-XR1(config)#netconf-yang agent ssh
RP/0/0/CPU0:R11-XR1(config)#ssh server v2
RP/0/0/CPU0:R11-XR1#crypto key generate dsa
```

### Comparing YANG, YAML, RAML and XML

![Comparing]({{ site.url }}{{ site.baseurl }}/assets/images/yang-yaml.png)

### NCM (Network Configuration Management)

- Is the process of organizing and maintaining information about all the components of a computer network.
- When a network needs repair, modification, expansion, or upgrading, the administrator refers to the “network configuration management” database to determine the best course of action.
- This database contains the locations and network addresses of all hardware devices, as well as information about the programs, versions, and updates installed in network computers.

### Advantages of network configuration management

- Streamlining the processes of maintenance, repair, expansion, and upgrading.
- Minimizing configuration errors and downtime.
- Optimizing network security.
- Ensuring that changes made to a device or system do not adversely affect other devices or systems.
- Rolling back changes to a previous configuration if results are unsatisfactory.
- Archiving the details of all network configuration changes.
- Collect network inventory, including chassis and modules as well as serial numbers
- Report on collected network inventory
- Collect device configurations
- Keep multiple versions of device configurations
- Allow comparison between the multiple versions of device configurations
- Detect changes in device configurations (event or polling based)
- Determine which user made changes to device configurations
- Report on configuration changes
- Allow configuration changes to be batched and scheduled
- Report on existing software versions deployed on devices
- Keep a repository of device software versions
- Support upgrading of device software
- Audit configuration to help ensure compliance
- Search device configurations, software, and hardware
- Store or link to static documentation and diagrams
- Support the approval processes and workflows

### Shell Script vs CM Tool Script

![shell]({{ site.url }}{{ site.baseurl }}/assets/images/shell-script.png)

## Open Source Configuration Management Tools

![open]({{ site.url }}{{ site.baseurl }}/assets/images/open-source.png)

### CFEngine

- One of the earliest full-featured configuration management systems out there, CFEngine has gone through several iterations and maintained relevance as OS has gone from the local data center to the cloud.
- At the heart of the infrastructure automation framework, CFEngine is also a modeling and monitoring compliance engine, capable of sitting on a small footprint.
- As recommended by CFEngine, steps toward identifying an initial desired state include:
    1) model the desired state of your environment.
    2) simulate configuration changes before committing them.
    3) confirm the desired state and set for automatic self-healing.
    4) collect reports on the differences between actual and desired states.
- CFEngine has a library of reusable data-driven models that will help users model their desired states.
- These infrastructure patterns are designed to be reusable across the Enterprise.

### Chef

- Offered as both an open-source and enterprise product, Chef is a powerful tool for full IT infrastructure configuration management.
- With open-source Chef at the heart of both offerings, shared features include a flexible and scalable automation platform, access to 800+ reusable cookbooks, and integration with leading cloud providers.
- Chef also offers enterprise platform support, including Windows and Solaris, and allows you to create, bootstrap, and manage OpenStack clouds.
- It has easy installation with a ‘one-click‘ Omnibus Installer, automatic system discovery with Ohai, text-based search capabilities, and multiple environment support.
- Other notable features include the “Knife” command line interface, “Dry Run” mode for testing potential changes, and the ability to manage 10,000+ nodes on a single Chef server.
- Features only available in the enterprise version of Chef include availability as a hosted service, enhanced management console, centralized activity, and resource reporting, as well as “Push” command and control client runs.
- Multi-tenancy, role-based access control (RBAC), high availability installation support and verification, along with centralized authentication using LDAP or Active Directory are included with Chef enterprise.

### Puppet

- What started out as a popular DevOps tool has quickly become a movement.
- Written in Ruby, like Chef, Puppet also comes in both an open-source and enterprise version.
- However, where Chef has a healthy offering of features across both open-source and enterprise versions, Puppet has placed the majority of its feature set into enterprise status.
- Features that the open-source version comes with include provisioning (Amazon EC2, Google Compute Engine), configuration management (operating systems and applications) plus 2,000+ pre-built configurations on Puppet Forge.
- Considerably more features are available for the enterprise version, including the open-source features plus a graphical user interface, event inspector (visualize infrastructure changes), supported modules, and provisioning (VMware VMs).
- Configuration management (discovery, user accounts), orchestration, task automation, and role-based access control (with external authentication support) are also included.
- Puppet enterprise has a unified cross-platform installer of all components and support.

### SaltStack

- As part of a larger, enterprise-ready application, the configuration management piece of Salt is as robust and feature-full as would be expected.
- Built upon the remote execution core, execution of the system occurs on “minions” which receive commands from the central Salt master and reply with the results of said commands.
- Salt supports the simultaneous configuration of tens of thousands of hosts.
- Based upon host “states”, no programming is required to write the configuration files, which are small and easy to understand, that help identify the state of each host.
- Additionally, for those who do programs, or admins who want to have more control and familiarity with their configuration files, any language can be used to render the configurations.

### Ansible

- Ansible is a model-driven configuration management tool that leverages SSH to improve security and simplify management.
- Ansible is built on five design principles including ease of use (doesn’t require writing scripts or custom code)
- Comprehensive automation (allowing you to automate almost anything in your environment)
- Efficiency (since it runs on OpenSSH it doesn’t rely on memory or CPU resources) – Agentless
- Security (it is inherently more secure because it doesn’t require an agent, additional ports, or root-level daemons).
- Like all other open-source projects, Ansible has a paid product that comes in the form of a web UI called Ansible Tower.

## Chef vs Puppet vs Ansible vs SaltStack

![vs]({{ site.url }}{{ site.baseurl }}/assets/images/vs.png)

### Scalability

![scalability]({{ site.url }}{{ site.baseurl }}/assets/images/scalability.png)

### Ease of Setup

![Ease]({{ site.url }}{{ site.baseurl }}/assets/images/Ease.png)

### Availability

![Availability]({{ site.url }}{{ site.baseurl }}/assets/images/Availability.png)

### Management

![Management]({{ site.url }}{{ site.baseurl }}/assets/images/Management.png)

### Interoperability

![Interoperability]({{ site.url }}{{ site.baseurl }}/assets/images/Interoperability.png)

### Final Scorecard

![Scorecard]({{ site.url }}{{ site.baseurl }}/assets/images/Scorecard.png)

### More Factors

![Factors]({{ site.url }}{{ site.baseurl }}/assets/images/Factors.png)

### Configuration Language

![Language]({{ site.url }}{{ site.baseurl }}/assets/images/Language.png)

### GitHub Activity

![Activity]({{ site.url }}{{ site.baseurl }}/assets/images/Activity.png)

### Enterprise Cost Up to 100 nodes

![Enterprise]({{ site.url }}{{ site.baseurl }}/assets/images/Enterprise.png)

### Popularity

![Popularity]({{ site.url }}{{ site.baseurl }}/assets/images/Popularity.png)

### Success Story

![Success]({{ site.url }}{{ site.baseurl }}/assets/images/Success.png)

## Why we will use Ansible for network automation

1) Agentless.
2) Free and Open Source Software (FOSS).
3) Extensible.
4) Integrating into Existing DevOps Workflows.
5) Network-Wide and Ad Hoc Changes.

### 1. Agentless

- Ansible was primarily built as an automation platform for deploying Linux applications.
- Expanded to Windows since the early days.
- Ansible open-source project did NOT have the goal of automating network infrastructure.
- The truth is that the more the Ansible community understood how flexible and extensible the underlying Ansible architecture was, the easier it became to extend Ansible for their automation needs, which included networking.
- Network vendors: Arista, Juniper, Cumulus, Cisco, F5, and Palo Alto Networks.

### 2. Free and Open Source Software (FOSS)

- Ansible is open-source with all code publicly accessible on GitHub, it is absolutely free to get started using Ansible.
- It can be installed and provide value to network engineers in minutes. 
- Even Ansible, Inc. Tower is free for up to 10 devices. so, at least you can get a taste of Tower.
- AWX provides a web-based user interface, REST API, and task engine built on top of Ansible. It is the upstream project for Tower, a commercial derivative of AWX.

### 3. Extensible

- Ansible was primarily built as an automation platform for deploying Linux applications.
- Expanded to Windows since the early days.
- Ansible open source project did NOT have the goal of automating network infrastructure.
- Ansible community understood how flexible and extensible so, so they extend Ansible for their automation needs, which included networking.
- Network vendors such as Arista, Juniper, Cumulus, Cisco, F5, and Palo Alto Networks.

### 4. Integrating into Existing DevOps Workflows

- Ansible is used for application deployments within IT organizations.
- By integrating Ansible with the network infrastructure, it expands what is possible when new applications are turned up or migrated.
- Network-centric tasks can be automated and integrated into workflows that already exist within the IT organization.

### 5. Network-Wide and Ad Hoc Changes

- One of the problems solved with configuration management tools is configuration drift (when a device’s desired configuration gradually drifts, or changes, over time).
- What if an outage occurs and you need to troubleshoot it?
- You usually bypass the management system, go directly to a device, find the fix, and quickly leave for the day, right?
- At the next time interval when the agent pulls the configuration, the change made to fix the problem is overwritten.
- Because Ansible is agentless, there is NOT a default push or pull to prevent configuration drift. The tasks to automate are defined in what is called an Ansible playbook. 
- Running a playbook once by default is attractive for network engineers. It is added peace of mind that changes made manually on the device are not going to be automatically overwritten.

## Network Telemetry and Big Data Analysis

- Network Telemetry describes how information from various data sources can be collected using a set of automated communication processes and transmitted to one or more receiving equipment for analysis tasks.
- Analysis tasks may include event correlation, anomaly detection, performance monitoring, metric calculation, trend analysis, and other related processes.

### Network Telemetry data source Classification

![Telemetry]({{ site.url }}{{ site.baseurl }}/assets/images/Telemetry.png)

## Network data collectors and analyzer

- It seems these days that the marketplace is saturated with IP flow export formats.
- CISCO has NetFlow, InMon has sFlow, Juniper uses JFlow, and there are several others. 
- NetFlow is a powerful source of security and network debugging information.
- Sampling mode: helps keeps the CPU load on your router or switch down.
- If Full mode NetFlow is required, consider using a SPAN, TAP, or mirrored port, and generate NetFlow with a software tool or dedicated appliance without incurring the additional load on the router or switch. 

### NetFlow v5

- Is the most popular and most basic. 
- It is ideal if you are simply interested in seeing the classic source and destination IP addresses, source and destination ports and the bytes count of transferred data.
- What makes NetFlow v5 special compared to its predecessors is the added BGP autonomous system information and flow sequence numbers.
- One limitation of NetFlow v5 is that you can only enable ingress flow export on an interface. 
- Most Cisco devices that are running IOS 11.1 and above support v5.

### NetFlow v9

- Is an upgrade to NetFlow v5. 
- On top of the traditional flow record of v5, it was an enhancement to support different technologies such as Multi-cast, IPSec, and Multi-Protocol Label Switching (MPLS).
- These enhancements are mostly due to the support for templates which allow the content of the flows to change based on the needs of the user.
- For example, due to the router’s ability to perform DPI, layer 7 application details can be exported through the use of NBAR.
- Also, Voice over IP and video traffic metrics such as jitter, packet loss, and round trip time can also be exported.
- It also added IPv6 support as well as egress flow collection. V9 is supported in IOS 12.4 and above.

### IPFIX

- Is the Cisco proposed standard for IP Flow Information eXport and was designed based on NetFlow v9. 
- Several vendors have already adopted IPFIX (e.g. Juniper, Avaya, SonicWALL, nBox, etc.).
- It added support for variable-length strings.
- In the future, Cisco will release Application Visibility and Control (AVC) exports which will take advantage of the variable length string capability and export HTTP host (E.g. netflix.com, youtube.com, facebook.com, etc.).

### Flexible NetFlow

- Flexible NetFlow is the configuration interface on the router or switch which allows the user to take advantage of NetFlow v9 and IPFIX.
- Flexible NetFlow (FnF) allows the user to select the different elements wanted in the flow export.
- That is why it is said to be “flexible.” Most of the latest Cisco IOS releases support FnF which can be used to export NetFlow v5, v9 and IPFIX.

### sFlow

- Easily configurable through SNMP, its primary objective is to be a statistical network monitoring tool.
- Lots of different performance counters can be monitored through the sFlow.
- The biggest benefit of sFlow comes from its infinite scalability in large networks under heavy loads.

#### sFlow Disadvantages

- Unlike NetFlow, the sFlow protocol samples every N-th packet from the traffic stream, where N can be one-in-512, one-in-1024.
- This means that some communications may slip by entirely undetected, and the sFlow collector software will not know about them.
- Larger communications, such as big downloads, and online video content will stand a much bigger change of being reported, as there are many packets involved.
- The second drawback is the lack of accurate timestamping of the packet data.
- Sampled packets get forwarded as they are picked up from the datastream; however, they are not timestamped.

## Self-Driving Network

- One whose operation is totally automated.
- Advances in artificial intelligence are pushing us toward an economically feasible Self-Driving Network.
- Autonomous networks will self-configure, monitor, manage, correct, defend, and analyze, all with very little human intervention.
- They will predict performance issues before users are affected.

## “New Programming Skills” needed for Network Engineer

- Python
- REST APIs
- JSON/XML/YAML
- Linux Skills
- Ansible
- git/GitHub
- Docker

## “New Networking Skills” needed for Network Engineer

- Network Controllers
- NETCONF/YANG
- Container Networking
- Cloud Networking
- Linux Networking
- IOT
- NFV
