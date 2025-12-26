---
title: "Part 8 — Monitoring, Telemetry & Observability"
header:
 image: /assets/images/Telemetry.png
last_modified_at: 2025-12-26
categories:
 - NetDevOps
 - Observability
tags:
 - Prometheus
 - Grafana
toc: true
toc_sticky: true
---

## From Monitoring to Observability
Traditional monitoring answers "Is the device up?" Observability helps answer "Why did this happen?" — the difference is critical for mature NetDevOps operations.

### SNMP vs Streaming Telemetry
**SNMP (Polling):** mature but coarse-grained and high-latency.

**Streaming Telemetry:** devices push rich, near-real-time telemetry to collectors for anomaly detection and fine-grained analysis.

### Prometheus: The Monitoring Backend
Prometheus scrapes metrics from exporters and stores time-series data.

Example `prometheus.yml` snippet:

```yaml
global:
 scrape_interval: 15s

scrape_configs:
 - job_name: 'network-devices'
  static_configs:
   - targets: ['10.1.1.1:9161']
    labels:
     device: 'R1'
```

### Grafana: Visualization and Dashboards
Grafana reads Prometheus and visualizes metrics (utilization, BGP status, interface errors) and configures alerts.

### Logs, Metrics, Traces
Collect:
- Metrics: Prometheus
- Logs: Grafana Loki / ELK
- Traces: Jaeger

Combined, these provide deep observability for troubleshooting and automation-driven remediation.

### Alerting Best Practices
Good alerts detect real issues and avoid noise. Example:

{% raw %}
```yaml
alert: HighCPUUsage
expr: device_cpu_usage_percent > 95
for: 5m
annotations:
  summary: "{{ $labels.device }} CPU high"
```
{% endraw %}

**Try this now:** Stand up Prometheus + Grafana in a sandbox, add an SNMP exporter for one device, and build a dashboard that shows interface utilization over time.