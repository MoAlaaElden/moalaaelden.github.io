---
title: "DevOps - The Twelve Factor App methodology"
header:
  image: /assets/images/12-Factor-App/1-Codebase1.png
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

The Twelve Factors
## 1. Codebase
One codebase tracked in revision control, many deploys

![Codebase1]({{ site.url }}{{ site.baseurl }}/assets/images/12-Factor-App/1-Codebase1.png)

## 2. Dependencies
Explicitly declare and isolate dependencies
## 3. Config
Store config in the environment
## 4. Backing services
Treat backing services as attached resources
## 5. Build, release, run
Strictly separate build and run stages
## 6. Processes
Execute the app as one or more stateless processes
## 7. Port binding
Export services via port binding
## 8. Concurrency
Scale out via the process model
## 9. Disposability
Maximize robustness with fast startup and graceful shutdown
## 10. Dev/prod parity
Keep development, staging, and production as similar as possible
## 11. Logs
Treat logs as event streams
## 12. Admin processes
Run admin/management tasks as one-off processes

[Reference and more details:](https://moalaaelden.wordpress.com/2022/10/24/install-docker-engine-on-ubuntu-18-04-lts-20-04-lts-21-10-lts-22-04-lts-2/ "MoAlaaElden")