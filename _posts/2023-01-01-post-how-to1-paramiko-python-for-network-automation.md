---
title: "How To(1) Paramiko & Python for Network Automation"
header:
  image: /assets/images/Paramiko-Python-For-Network-Engineers.jpg
last_modified_at: 2023-01-01
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
toc_sticky: true # Sticky Table of Contents
---
# How To(1) Paramiko & Python for Network Automation

In this tutorial, we’ll see how to initiate SSH from Paramiko Python library to Cisco Device.

[Paramiko](https://www.paramiko.org/) is a pure-Python implementation of the SSHv2 protocol, providing both client and server functionality.

It is better to first understand Paramiko and then look into other network automation tools such as “Netmiko, NAPALM, Nornir, etc…” so that you will get a clear understanding of SSH connection details from Python.

Upon [Paramiko API documentation](https://docs.paramiko.org/en/stable/) you will find multiple “Core SSH protocol classes” and the one that we will deal with is the Client class.

And here [Client](https://docs.paramiko.org/en/stable/api/client.html) they have given us a sample script, as shown below:

```python
# Initializing SSH Client.
client = SSHClient()

# Loading system hosts keys
client.load_system_host_keys()

# Connecting to Linux server "ssh.example.com".
client.connect('ssh.example.com')

# Executing the command "ls -l" in a Linux server.
stdin, stdout, stderr = client.exec_command('ls -l')
```
From the above example, The method they are using is ```exec_command()```

This ```exec_command()``` method is suitable for connecting to Linux servers because that is having the intelligence to identify **the standard input, output, and error** based on the response type **stdout** as it will print the data. 
For example, if you are getting an error, it will come in **stderr** automatically.

```python
exec_command(command, bufsize=-1, timeout=None, get_pty=False, environment=None)

# Execute a command on the SSH server. 
# A new Channel is opened and the requested command is executed. 
# The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.
```
But to interact with **Network Devices** such as Routers and Switches, it is better to use ```invoke_shell()``` method.

Because that will initiate an **interactive shell** session on the SSH “server” in our case it will be our **Router or Switch** and we will send a stream of data “In our case Commands“, and then this will be just **printing the output**.

> **In this case, Paramiko doesn’t check whether it is an error message or a success message, It will just print as it is.**

## First code:

Now, let’s go to our python terminal and start writing our first code:

If you need to build your **Separated and Isolated Python Development Environment for Learning**.

So, you can follow my latest tutorial.

### Install Paramiko

First, we need to Install Paramiko:

```terminal
pip install paramiko

OR

python3 -m pip install paramiko
```

### Check reachability and accessibility

Then, check Cisco Router reachability and accessibility:

```bash
moalaa@devnet-automation-01:~$ ping R1.MoAlaa.com -c 2
PING R1.MoAlaa.com (192.168.100.101) 56(84) bytes of data.
64 bytes from R1.MoAlaa.com (192.168.100.101): icmp_seq=1 ttl=255 time=1.35 ms
64 bytes from R1.MoAlaa.com (192.168.100.101): icmp_seq=2 ttl=255 time=2.69 ms

moalaa@devnet-automation-01:~$ ssh moalaa@R1.MoAlaa.com
Password: 
C

             ____             _   _      _   
            |  _ \  _____   _| \ | | ___| |_ 
            | | | |/ _ \ \ / /  \| |/ _ \ __|
            | |_| |  __/\ V /| |\  |  __/ |_ 
            |____/ \___| \_/ |_| \_|\___|\__|
                                             
    _         _                        _   _             
   / \  _   _| |_ ___  _ __ ___   __ _| |_(_) ___  _ __  
  / _ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
 / ___ \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | |
/_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|

R1-ASR1#
```

### Start the Python shell

Then, start the Python shell, simply type python3 and hit Enter in the terminal:

```python
(MoAlaa_DevNet_env) moalaa@devnet-automation-01:~$ python3
Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

### Import Paramiko

Then, we need to import Paramiko:

```python
>>> from paramiko import client
>>> 
```

### Host details
Then, we will define the host details.

Defining a string **hostname**. So the device’s name is “R1.MoAlaa.com“.
Either, we can give the IP Address or Hostname here.

```python
>>> hostname = "R1.MoAlaa.com"
```

Defining a string “username“. So the device’s username is “moalaa“.

```python
>>> username = "moalaa"
```

Defining a string “password“. So the device’s password is “cisco“.

```python
>>> password = "cisco"
```

Now we’ll create SSH client “ssh_client“. So that will be `client.SSHClient()`.

```python
>>> ssh_client = client.SSHClient()
```

Set policy “AutoAddPolicy” to use when connecting to devices without a known host key.

```python
>>> ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
```

Now, let’s connect to our Router:

```python
>>> ssh_client.connect(hostname=hostname,
...                    port=22,
...                    username=username,
...                    password=password,
...                    look_for_keys=False, allow_agent=False)
>>> 
```

Now, it should be connected successfully.

> Now, if you want to execute a command, such as “show interfaces description”.

We need first initiate, ```invoke_shell()``` or the ```exec_command()``` method.

So, we will create another variable “device_access” and using ```invoke_shell()``` method.

```python
>>> device_access = ssh_client.invoke_shell()
```

Now, we’ll try to send the commands ```terminal len 0``` and `show interfaces description` directly and see what happens.
We have a method called `send()` which will use the initiated SSH channel and just send the data “command” in our case.

```python
>>> device_access.send("terminal len 0\n")
15
>>> 
>>> device_access.send("show interfaces description\n")
28
>>> 
```
Now, we’ll try receiving the data “output”.

So, we will create another variable “output ” and using `recv()` method.

We need to set the bytes of data that we need to receive. So we will give the maximum “65535“

```python
>>> output = device_access.recv(65535)
```

Now, we’ll try printing the output on our screen.

> Note: We need to use the `decode()` method to convert the output 
**bytes** into a **human-readable** format.

```python
>>> print(output.decode())
C

             ____             _   _      _   
            |  _ \  _____   _| \ | | ___| |_ 
            | | | |/ _ \ \ / /  \| |/ _ \ __|
            | |_| |  __/\ V /| |\  |  __/ |_ 
            |____/ \___| \_/ |_| \_|\___|\__|
                                             
    _         _                        _   _             
   / \  _   _| |_ ___  _ __ ___   __ _| |_(_) ___  _ __  
  / _ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
 / ___ \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | |
/_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|


R1-ASR1#terminal len 0
R1-ASR1#show interfaces description
Interface                      Status         Protocol Description
Gi1                            up             up       
Gi1.12                         up             up       Connection to R2-ASR2
Gi1.13                         up             up       Connection to R3-ASR3
Gi1.14                         up             up       Connection to R4-ASR4
Gi1.15                         up             up       Connection to R5-ASR5
Gi2                            up             up       "MANAGEMENT INTERFACE - DON'T TOUCH ME"
Gi3                            admin down     down     "MNG - Int - PFSense FW"
Lo0                            up             up       
Lo7                            up             up       
Lo8                            up             up       
Lo100                          up             up       
Lo101                          up             up       Configured with nornir-netmiko
Lo102                          up             up       Configured with nornir-netmiko
Lo200                          up             up       
Lo201                          up             up       Configured with nornir-scrapli
Lo202                          up             up       Configured with nornir-scrapli
Lo300                          up             up       
Lo301                          up             up       Configured with nornir-napalm
Lo400                          up             up       
Lo1000                         up             up       
R1-ASR1#
>>> 
```
### Finally

We need to close this SSH connection by using `close()` method.

```python
>>> ssh_client.close()
>>>
```

## I hope this was helpful for you to understand how to initiate SSH session from Paramiko toward any Network Device.