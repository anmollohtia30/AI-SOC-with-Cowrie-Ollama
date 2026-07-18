# Wazuh Installation and Integration

## Overview

Wazuh is an open-source Security Information and Event Management (SIEM) and Extended Detection and Response (XDR) platform used for real-time security monitoring, log analysis, intrusion detection, and incident response.

In this project, Wazuh is integrated with the Cowrie SSH Honeypot to collect and analyze attack logs. It provides centralized log management, custom detection rules, and enhanced visibility into attacker activities before the logs are processed by the AI analysis module.

---

## Environment

- Ubuntu 24.04 LTS
- Wazuh Manager
- Cowrie SSH Honeypot
- Python 3
- Ollama (Llama 3.2)
- Telegram Bot API
- VMware Workstation

---

## Wazuh Installation

Install Wazuh Manager on Ubuntu by following the official Wazuh installation guide.

After installation, verify that the services are running:

```bash
sudo systemctl status wazuh-manager
sudo systemctl status wazuh-dashboard
sudo systemctl status wazuh-indexer
```

---

## Cowrie Log Integration

Configure Wazuh to monitor the Cowrie JSON log file.

Example log location:

```text
/home/cowrie/cowrie/var/log/cowrie/cowrie.json
```

Add the log path to the Wazuh configuration:

```xml
<localfile>
  <log_format>json</log_format>
  <location>/home/cowrie/cowrie/var/log/cowrie/cowrie.json</location>
</localfile>
```

Restart the Wazuh Manager:

```bash
sudo systemctl restart wazuh-manager
```

---

## Custom Rules

Custom Wazuh rules can be created to detect SSH login attempts, failed authentication, executed commands, and suspicious attacker behavior from Cowrie logs.

These rules help classify events based on severity and generate alerts for further analysis.

---

## Workflow

```
Attacker (Kali Linux)
        │
        ▼
Cowrie SSH Honeypot
        │
        ▼
Cowrie JSON Logs
        │
        ▼
Wazuh SIEM
        │
        ▼
Python Monitoring Script
        │
        ▼
Ollama (Llama 3.2)
        │
        ▼
AI Attack Analysis
        │
        ▼
Telegram Alert Notification
```

---

## Features

- Real-time log collection using Wazuh
- Integration with Cowrie SSH Honeypot
- Centralized security event monitoring
- Custom detection rules for honeypot events
- AI-powered attack analysis using Ollama
- Instant Telegram alert notifications
- Modular and scalable architecture

---

## Result

The integration of Wazuh with Cowrie provides centralized monitoring and security event detection. The collected attack logs are further analyzed by the Ollama Large Language Model, which generates human-readable attack summaries and automatically sends real-time alerts through Telegram. This architecture combines traditional SIEM capabilities with AI-powered threat analysis to improve incident detection and response.