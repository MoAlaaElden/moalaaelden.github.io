---
title: "Part 6 — NetDevOps CI/CD Pipelines Explained"
header:
 image: /assets/images/Success.png
last_modified_at: 2025-12-26
categories:
 - NetDevOps
 - CI/CD
tags:
 - GitHub Actions
 - GitOps
toc: true
toc_sticky: true
---

## Understanding CI/CD in Network Context
Continuous Integration/Continuous Deployment represents automation of the change process itself and eliminates the slow, error-prone manual change windows common in traditional operations.

### GitOps: Git as Source of Truth
GitOps formalizes the principle: desired infrastructure state lives in Git. Any change to Git triggers automated validation, deployment, and verification.

**Benefits:** audit trail, peer review, automated testing, and instant rollback.

### GitHub Actions for Network Automation
Example workflow to validate pull requests that touch network configs:

```yaml
name: Network Configuration Validation

on:
 pull_request:
  paths:
   - 'network-configs/**'
 push:
  branches: [main]

jobs:
 validate:
  runs-on: ubuntu-latest
  steps:
   - uses: actions/checkout@v2
   - name: Set up Python
    uses: actions/setup-python@v2
    with:
     python-version: '3.9'
   - name: Validate config syntax
    run: |
     pip install pyyaml
     python scripts/validate_configs.py network-configs/
   - name: Run security checks
    run: |
     python scripts/check_security.py network-configs/
   - name: Test with Ansible linter
    run: |
     pip install ansible-lint
     ansible-lint playbooks/
```

### Pre/Post Deployment Checks
**Pre-deployment:** syntax validation, compliance checks, simulation in test environment, and peer review.

**Post-deployment:** connectivity checks, BGP neighbor validation, functional tests, and monitoring-based verification.

### Automated Testing for Network Changes
Examples of tests you can run in CI:

```python
# Test that configuration file is valid YAML
import yaml

def test_config_syntax(config_file):
  with open(config_file) as f:
    try:
      config = yaml.safe_load(f)
      assert config is not None
    except yaml.YAMLError:
      raise AssertionError(f"Invalid YAML in {config_file}")
```

```python
# Test that insecure protocols are not enabled
def test_no_telnet(config):
  assert "telnet" not in config.lower()
```

```python
# Test BGP neighbors are up
from napalm import get_network_driver

def test_bgp_neighbors_up(device):
  driver = get_network_driver(device["os"])
  conn = driver(device["host"], device["user"], device["pass"])
  conn.open()
  bgp = conn.get_bgp_neighbors()
  for neighbor in bgp['global']['peers'].values():
    assert neighbor['is_up'] == True
```

### Deployment Orchestration Example
A deploy workflow that runs on merged PRs and executes the Ansible deployment plus verification:

```yaml
name: Deploy Router Configs
on:
 pull_request_closed:
  branches: [main]

jobs:
 deploy:
  if: github.event.pull_request.merged == true
  runs-on: ubuntu-latest
  steps:
   - uses: actions/checkout@v2
   - name: Pre-deployment validation
    run: |
     python scripts/validate_configs.py
     ansible-lint playbooks/
   - name: Generate deployment report
    run: |
     git diff HEAD~1 HEAD > deployment_diff.txt
   - name: Deploy configurations
    run: |
     ansible-playbook -i inventory.yml playbooks/deploy_routers.yml
    env:
     ANSIBLE_HOST_KEY_CHECKING: False
   - name: Post-deployment verification
    run: |
     python scripts/verify_deployment.py
   - name: Notify Slack
    uses: slackapi/slack-github-action@v1
    with:
     payload: |
      { "text": "✓ Router configs deployed successfully" }
```

**Key Takeaway:** CI/CD pipelines replace slow manual change windows with fast, tested, and auditable deployments.

**Try this now:** Add an Action to lint your Ansible playbooks and run a simple `python scripts/validate_configs.py` on PRs.