---
title: "DevOps - The Twelve Factor App methodology"
header:
  image: /assets/images/12-Factor-App/12-factor-app.png
last_modified_at: 2024-12-13
categories:
  - DevOps
tags:
  - Apps
  - DevOps
toc: true # On this page
toc_sticky: true # Sticky Table of Contents
---

# DevOps - The Twelve Factor App methodology

The 12-Factor App methodology provides a set of best practices for building cloud-native applications that are scalable, resilient, and easy to maintain.

In the modern era, Software is commonly delivered as a service: called web apps, or software-as-a-service. The twelve-factor app is a methodology for building software-as-a-service apps that:

- Use `declarative` formats for setup automation, to minimize time and cost for new developers joining the project;
- Have a `clean contract` with the underlying operating system, offering `maximum portability` between execution environments;
- Are suitable for `deployment` on modern `cloud platforms`, obviating the need for servers and systems administration;
- `Minimize divergence` between development and production, enabling `continuous deployment` for maximum agility;
- And can `scale up` without significant changes to tooling, architecture, or development practices.

The twelve-factor methodology can be applied to apps written in any programming language, and which use any combination of backing services (database, queue, memory cache, etc).

# The Twelve Factors
# 1. Codebase
One codebase tracked in revision control, many deploys

![Codebase1]({{ site.url }}{{ site.baseurl }}/assets/images/12-Factor-App/1-Codebase1.png)

Multiple apps sharing the same code is a violation of twelve-factor.

![Codebase2]({{ site.url }}{{ site.baseurl }}/assets/images/12-Factor-App/1-Codebase2.png)

The solution here is to factor shared code into libraries which can be included through the dependency manager.

![Codebase3]({{ site.url }}{{ site.baseurl }}/assets/images/12-Factor-App/1-Codebase3.png)

There is only one codebase per app, but there will be many deploys of the app. A deploy is a running instance of the app. This is typically a production site, and one or more staging sites.

![Codebase4]({{ site.url }}{{ site.baseurl }}/assets/images/12-Factor-App/1-Codebase4.png)

# 2. Dependencies
Explicitly declare and isolate dependencies

### Dependency Isolation 

![Dependencies1]({{ site.url }}{{ site.baseurl }}/assets/images/12-Factor-App/2-Dependencies1.png)

- Libraries installed through a packaging system can be installed `system-wide` (known as `site packages`) or scoped into the directory containing the app (known as `vendoring` or `bundling`).
- A twelve-factor app never relies on implicit existence of `system-wide` packages, it uses a dependency isolation tool during execution such as `python3-venv`. 

- Check My Tutorial for [How to Create an Isolated Python Development Environment using venv](https://moalaa.com/python/venv/virtual-environment/network-automation/how-to-create-an-isolated-python-development-environment-using-venv/)

```bash
➜  12-Factor-App git:(main) ✗ python3 -m venv venv
➜  12-Factor-App git:(main) ✗ ls
app.py  requirements.txt  venv
➜  12-Factor-App git:(main) ✗
➜  12-Factor-App git:(main) ✗ source venv/bin/activate
(venv) ➜  12-Factor-App git:(main) ✗
```

- It declares all dependencies, completely and exactly, via a dependency declaration manifest.

```python
(venv) ➜  12-Factor-App git:(main) ✗ cat app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcomeToMoAlaa():
    return "Welcome to MoAlaa"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

(venv) ➜  12-Factor-App git:(main) ✗
```

```bash
(venv) ➜  12-Factor-App git:(main) ✗ cat requirements.txt
flask==2.1.3
Werkzeug==2.2.2
(venv) ➜  12-Factor-App git:(main) ✗
```
### System Tools Isolation 

![Dependencies2]({{ site.url }}{{ site.baseurl }}/assets/images/12-Factor-App/2-Dependencies2.png)

- If the app needs to shell out to a `system tool` such as `curl`, that tool should be vendored into the app.
- Docker provides the ability to package and run an application in a loosely isolated environment called a container. 
- The isolation and security lets you run many containers simultaneously on a given host.

```bash
(venv) ➜  12-Factor-App git:(main) ✗ ls
Dockerfile  app.py  requirements.txt  venv
```
```bash
(venv) ➜  12-Factor-App git:(main) ✗ cat Dockerfile
FROM python:3:10-alpine
WORKDIR /12-Factor-App
COPY requirements.txt /12-Factor-App
RUN pip install -r requirements.txt --no-cache-dir
COPY . /12-Factor-App
CMD python app.py
(venv) ➜  12-Factor-App git:(main) ✗ 
```
- Check My Tutorials for Docker [Here](https://moalaaelden.wordpress.com/category/docker/) and [Here](https://moalaa.com/categories/#docker)

# 3. Config
Store config in the environment

**App Configuration Basics: The Easy Way to Manage Settings**

![Config1]({{ site.url }}{{ site.baseurl }}/assets/images/12-Factor-App/3-Config1.png)

When building apps, it’s important to manage settings (called *configuration*) that can change based on where your app is running—like on your laptop, a test server, or live for users. Here's what you need to know:

### What is App Configuration?
It includes:
- Connections to services like databases or file storage.
- Passwords or keys for tools like Twitter or AWS.
- Deployment-specific details like website addresses.

### Why Avoid Hardcoding Config?
Some apps store these settings directly in their code. That’s risky because:
- It’s hard to update settings without changing the code.
- It could expose sensitive info if someone sees your code.

### What's Wrong with Config Files?
Using files to store settings (like `config.yml`) is better than hardcoding but has issues:
- They can be accidentally shared with your code.
- Config files are often scattered and hard to manage.
- They might only work with specific programming languages.

### The Best Solution: Environment Variables
Environment variables are simple settings stored outside your app’s code. They’re:
- Easy to update without touching code.
- Safe from accidentally being shared in your codebase.
- Supported by all programming languages and systems.

```bash
(venv) ➜  12-Factor-App git:(main) ✗ cat .env
HOST="0.0.0.0"
DEBUG="True"
```

```python
(venv) ➜  12-Factor-App git:(main) ✗ cat app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def welcomeToMoAlaa():
    return "Welcome to MoAlaa"

if __name__ == "__main__":
    app.run(host=os.getenv('HOST'), debug=os.getenv('DEBUG'))

```

### Keep It Simple
Instead of grouping settings by environment (like "staging" or "production"), treat each setting as its own piece. This makes scaling up your app to more servers or users easier over time.

Using these tips will make managing your app’s settings simpler, safer, and ready for any situation!

# 4. Backing services
Treat backing services as attached resources
# 5. Build, release, run
Strictly separate build and run stages
# 6. Processes
Execute the app as one or more stateless processes
# 7. Port binding
Export services via port binding
# 8. Concurrency
Scale out via the process model

**Scaling Python Apps Made Simple**  

When building apps in Python, you need a plan for handling tasks (concurrency) and growing your app to handle more users (scaling). Here’s a simple guide:  

---

### What Are Processes?  
A process is just a running program. Apps can have one or more processes, each doing different tasks. For example:  
- A **web process** handles user requests (e.g., with Django or Flask).  
- A **worker process** handles background jobs (e.g., with Celery or RQ).  

---

### Why Use Multiple Processes?  
Using multiple processes lets your app:  
1. **Handle Different Workloads**: Assign specific tasks to different processes (e.g., web requests vs. background tasks).  
2. **Scale Easily**: Add more processes to handle more traffic without changing your app’s code.  

---

![Concurrency1]({{ site.url }}{{ site.baseurl }}/assets/images/12-Factor-App/8-Concurrency1.png)

### How to Manage Concurrency in Python  
Python has tools to handle tasks efficiently:  
- **Threads**: For lightweight tasks within one process.  
- **Async/await**: For event-driven tasks (e.g., `asyncio`).  
- **Processes**: For running independent tasks in parallel (`multiprocessing`).  

---

### How to Scale Your App  
1. **Add More Processes**: Instead of making one process bigger, run more processes across different machines (horizontal scaling).  
   - Example: Use multiple web servers with a load balancer to share traffic.  

![Concurrency2]({{ site.url }}{{ site.baseurl }}/assets/images/12-Factor-App/8-Concurrency2.png)

2. **Organize Processes**: Define what each process does (e.g., web or worker) and how many of each to run.  

---

### Tools to Simplify Scaling  
- **Gunicorn**: Manages web processes for Python frameworks like Django.  
- **Celery**: Runs background tasks (like sending emails).  
- **Foreman** or **Honcho**: Helps manage multiple processes during development.  

---

### Best Practices  
- Let the OS or tools like **Docker** or **systemd** handle process restarts and logs.  
- Avoid manually managing processes (e.g., no PID files).  

---

By using multiple processes and the right tools, you can make your Python app scalable, efficient, and ready for any workload!  

# 9. Disposability
Maximize robustness with fast startup and graceful shutdown
# 10. Dev/prod parity
Keep development, staging, and production as similar as possible
# 11. Logs
Treat logs as event streams
# 12. Admin processes
Run admin/management tasks as one-off processes

[References from 12factor](https://12factor.net/ "12factor")