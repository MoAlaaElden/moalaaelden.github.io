---
title: "Part 5 — Network Automation with Ansible"
header:
 image: /assets/images/shell-script.png
last_modified_at: 2025-12-26
categories:
 - NetDevOps
 - Ansible
tags:
 - Ansible
 - Playbooks
 - Idempotency
toc: true
toc_sticky: true
---

## Why Ansible for Networks?
Ansible is the dominant platform for network automation in enterprises. Unlike one-off Python scripts, Ansible is built to orchestrate across entire infrastructure fleets at scale.

**Key Advantages:**

- **Agentless:** No software required on network devices — Ansible connects via SSH.
- **Idempotent:** Playbooks are safe to run repeatedly and only change what needs changing.
- **Declarative:** Describe the desired state; Ansible manages the steps to get there.
- **Multi-Vendor:** The same playbook syntax can manage Cisco, Juniper, Arista, and others through vendor modules.
- **Version Controlled:** Playbooks are text files that live in Git, enabling reviews and history.

### Ansible Architecture for Networks
**Inventory:** Defines devices and connection details.

```yaml
all:
 children:
  cisco_devices:
   hosts:
    R1:
     ansible_host: 10.1.1.1
     ansible_network_os: cisco.ios.ios
    R2:
     ansible_host: 10.1.2.1
     ansible_network_os: cisco.ios.ios
  juniper_devices:
   hosts:
    J1:
     ansible_host: 10.2.1.1
     ansible_network_os: juniper.junos.junos
```

**Playbooks:** Define automation workflows.

```yaml
---
- name: Configure SNMP on routers
 hosts: cisco_devices
 gather_facts: no
 tasks:
  - name: Configure SNMP read-only community
   cisco.ios.ios_config:
    commands:
     - snmp-server community public RO
     - snmp-server location "DataCenter1"
   register: snmp_config

  - name: Verify SNMP configured
   debug:
    msg: "SNMP configured on {{ inventory_hostname }}"
```

**Modules:** Vendor-specific handlers (e.g., `cisco.ios.ios_config`, `arista.eos.eos_config`, `juniper.junos.junos_config`).

### Writing Effective Network Playbooks
**Principle 1: Idempotent Design**

Write playbooks that produce the same result whether run once or 100 times.

```yaml
---
- name: Ensure VLAN 10 exists
 hosts: switches
 gather_facts: no
 tasks:
  - name: Configure VLAN 10
   cisco.ios.ios_config:
    commands:
     - vlan 10
     - name "Management"
    match: line
```

**Principle 2: Multi-Vendor Conditionals**

```yaml
---
- name: Backup configs
 hosts: all_routers
 gather_facts: no
 tasks:
  - name: Backup Cisco config
   cisco.ios.ios_command:
    commands: show running-config
   register: ios_config
   when: ansible_network_os == 'cisco.ios.ios'

  - name: Backup Juniper config
   juniper.junos.junos_command:
    commands: show configuration
   register: junos_config
   when: ansible_network_os == 'juniper.junos.junos'

  - name: Save configs to files
   copy:
    content: "{{ ios_config.stdout_lines }}"
    dest: "backups/{{ inventory_hostname }}.cfg"
```

**Principle 3: Error Handling**

```yaml
---
- name: Deploy config with validation
 hosts: routers
 gather_facts: no
 tasks:
  - name: Apply router configuration
   cisco.ios.ios_config:
    src: configs/{{ inventory_hostname }}.j2
    save_when: changed
   register: config_result
   failed_when:
    - config_result.failed is true
    - '"invalid command" in config_result.msg'

  - name: Rollback if syntax error
   cisco.ios.ios_config:
    commands: "rollback 1"
   when: config_result.failed
```

### Real-World Playbook Example: VLAN Deployment

```yaml
---
- name: Deploy VLAN across infrastructure
 hosts: all_switches
 gather_facts: no
 vars:
  new_vlan_id: 200
  new_vlan_name: "Application_Team_A"

 tasks:
  - name: Ensure VLAN exists
   cisco.ios.ios_config:
    commands:
     - "vlan {{ new_vlan_id }}"
     - "name {{ new_vlan_name }}"
   register: vlan_config

  - name: Assign interfaces to VLAN
   cisco.ios.ios_config:
    lines:
     - "switchport mode access"
     - "switchport access vlan {{ new_vlan_id }}"
    before: "interface Ethernet1/1-48"
   register: interface_config

  - name: Verify VLAN configuration
   cisco.ios.ios_command:
    commands: "show vlan brief | include {{ new_vlan_id }}"
   register: vlan_verify
   failed_when: vlan_verify.stdout == ""

  - name: Generate documentation
   copy:
    content: "VLAN {{ new_vlan_id }} deployed on {{ inventory_hostname }}\nStatus: {{ vlan_verify.stdout }}"
    dest: "documentation/vlan_{{ new_vlan_id }}_{{ inventory_hostname }}.txt"

  - name: Notify team
   debug:
    msg: "✓ VLAN {{ new_vlan_id }} successfully deployed on {{ inventory_hostname }}"
```

Execution: 5 minutes for all sites. Automatic documentation. Automatic verification. Zero manual errors.

### Ansible Roles for Organizational Scalability
Organize repeated functionality into roles:

```
roles/
├── configure_snmp/
│  ├── tasks/
│  │  └── main.yml
│  ├── templates/
│  │  └── snmp.j2
│  └── vars/
│    └── main.yml
├── configure_ntp/
└── configure_syslog/
```

Each role encapsulates a function and helps teams scale playbooks safely.

### Key Takeaway
Ansible transforms network configuration from manual CLI work into orchestrated, version-controlled, repeatable workflows. Start small, enforce idempotency and testing, then scale with roles and CI integration.

**Try this now:** Create a role that configures NTP and test it against one lab switch.