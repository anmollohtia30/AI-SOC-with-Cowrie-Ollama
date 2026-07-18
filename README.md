# AI-Powered Security Operations Center (SOC) using Cowrie Honeypot, Ollama LLM, and Telegram Alerting System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-orange)
![Cowrie](https://img.shields.io/badge/Honeypot-Cowrie-green)
![Ollama](https://img.shields.io/badge/AI-Ollama-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# Overview

The AI-Powered Security Operations Center (SOC) is an intelligent cybersecurity monitoring system developed to automatically detect, analyze, and report suspicious activities captured by a Cowrie SSH Honeypot.

Traditional Security Operations Centers require security analysts to manually investigate large volumes of security logs. This process is time-consuming and often delays incident response.

This project enhances the traditional workflow by integrating Artificial Intelligence using the Ollama Large Language Model (LLM). Instead of manually reading log files, the AI automatically summarizes security incidents, identifies the attack behavior, estimates the threat level, and recommends mitigation actions.

Whenever an attacker interacts with the Cowrie Honeypot, the generated JSON logs are continuously monitored by a Python automation script. The script forwards newly detected events to Ollama for analysis and immediately sends an AI-generated incident report to the administrator through Telegram.

The project demonstrates how Artificial Intelligence can be combined with Honeypot technology to build an intelligent, low-cost, and automated Security Operations Center suitable for cybersecurity learning, research, and laboratory environments.

---

# Project Objectives

The primary objectives of this project are:

- Build an AI-powered Security Operations Center using open-source technologies.
- Deploy a Cowrie SSH Honeypot for capturing attacker activities.
- Monitor Cowrie log files automatically.
- Perform AI-based incident analysis using Ollama.
- Generate easy-to-understand security summaries.
- Notify administrators instantly using Telegram.
- Reduce manual log analysis.
- Improve incident response efficiency.
- Demonstrate practical SOC automation.

---

# Key Features

✔ SSH Honeypot using Cowrie

✔ Real-time log monitoring

✔ Automatic JSON log parsing

✔ AI-powered incident analysis

✔ Threat level identification

✔ MITRE ATT&CK mapping (basic)

✔ Telegram alert notifications

✔ Python automation

✔ Beginner-friendly implementation

✔ Open-source technologies

✔ Local AI processing (No cloud API required)

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Automation Scripts |
| Ubuntu 24.04 LTS | Honeypot Server |
| VMware Workstation | Virtualization |
| Cowrie Honeypot | Attack Capture |
| Wazuh SIEM | Log Collection |
| Ollama | Local AI Engine |
| Llama 3.2 | AI Incident Analysis |
| Telegram Bot API | Alert Notifications |
| JSON | Log Format |
| Requests Library | HTTP Communication |
| Git | Version Control |
| GitHub | Project Hosting |

---

# Project Architecture

```

```
                   +----------------+
                   | Kali Linux VM  |
                   | (Attacker)     |
                   +--------+-------+
                            |
                            |
                       SSH Attack
                            |
                            ▼
                 +----------------------+
                 | Cowrie Honeypot      |
                 | Ubuntu 24.04 LTS     |
                 +----------+-----------+
                            |
                    Generates JSON Logs
                            |
                            ▼
                   cowrie.json Log File
                            |
                            ▼
                 Python Monitoring Script
                      (monitor.py)
                            |
                     HTTP API Request
                            |
                            ▼
                 Ollama (Llama 3.2 LLM)
                            |
                  AI Incident Analysis
                            |
                            ▼
                   Telegram Bot API
                            |
                            ▼
                Security Administrator
```

---

# Project Workflow

The following workflow explains how the system operates.

### Step 1

An attacker attempts to connect to the Cowrie Honeypot using SSH.

↓

### Step 2

Cowrie records every interaction including:

- Login attempts
- Username
- Password
- Executed commands
- Session information
- Source IP Address

↓

### Step 3

All events are stored inside

```

cowrie.json

```

↓

### Step 4

The Python monitoring script continuously watches the log file.

↓

### Step 5

Whenever a new event is detected, the script automatically extracts the latest event.

↓

### Step 6

The event is sent to Ollama using its REST API.

↓

### Step 7

The Large Language Model analyzes the attack and generates:

- Attack Summary
- Threat Level
- MITRE ATT&CK Technique
- Recommended Security Actions

↓

### Step 8

The generated incident summary is automatically delivered to the administrator using the Telegram Bot API.

---

# Screenshots

The following screenshots demonstrate the implementation.

- Cowrie Honeypot Running
- SSH Attack Simulation
- Cowrie JSON Logs
- AI Incident Analysis
- Telegram Alert
- Project Workflow
- System Architecture

(Place screenshots inside the **images/** folder.)

---
# Prerequisites

Before setting up the project, ensure that the following software and hardware requirements are met.

## Hardware Requirements

- Intel Core i5 (8th Generation) or higher
- Minimum 8 GB RAM (16 GB Recommended)
- At least 50 GB Free Storage
- Internet Connection
- Virtualization Support (Intel VT-x / AMD-V)

---

## Software Requirements

### Host Machine

- Windows 10 / Windows 11
- VMware Workstation
- Ollama
- Git (Optional)

### Ubuntu Virtual Machine

- Ubuntu 24.04 LTS
- Python 3
- Git
- Cowrie Honeypot

### Attacker Machine

- Kali Linux

---

# Installation Guide

The project consists of three machines.

| Machine | Purpose |
|----------|----------|
| Windows Host | Runs Ollama AI |
| Ubuntu VM | Runs Cowrie Honeypot and Python Scripts |
| Kali Linux VM | Simulates Attacks |

---

# Step 1 - Clone Repository

Clone the repository.

```bash
git clone https://github.com/anmollohtia30/AI-SOC-with-Cowrie-Ollama.git
```

Move into the project directory.

```bash
cd AI-SOC-with-Cowrie-Ollama
```

---

# Step 2 - Install Python Dependencies

Install the required Python package.

```bash
pip install -r requirements.txt
```

---

# Step 3 - Install Cowrie Honeypot

Clone the official Cowrie repository.

```bash
git clone https://github.com/cowrie/cowrie.git
```

Move to the Cowrie directory.

```bash
cd cowrie
```

Create a Python virtual environment.

```bash
python3 -m venv cowrie-env
```

Activate the virtual environment.

```bash
source cowrie-env/bin/activate
```

Install Cowrie dependencies.

```bash
pip install -r requirements.txt
```

---

# Step 4 - Configure Cowrie

Copy the sample configuration file.

```bash
cp config/cowrie.cfg.example ~/cowrie/etc/cowrie.cfg
```

Modify the configuration according to your environment.

Example:

- SSH Port
- Hostname
- Logging
- Authentication

---

# Step 5 - Configure Wazuh (Optional)

If Wazuh SIEM is being used, copy the configuration files.

```bash
sudo cp config/ossec.conf.example /var/ossec/etc/ossec.conf
```

Copy the custom rules.

```bash
sudo cp config/local_rules.xml /var/ossec/etc/rules/
```

Restart the Wazuh Manager.

```bash
sudo systemctl restart wazuh-manager
```

Verify the service.

```bash
sudo systemctl status wazuh-manager
```

---

# Step 6 - Install Ollama

Download Ollama from the official website.

Install Ollama on the Windows host machine.

Start the Ollama server.

```cmd
ollama serve
```

Download the required AI model.

```cmd
ollama pull llama3.2:3b
```

Verify the model.

```cmd
ollama list
```

Expected output:

```text
NAME
llama3.2:3b
```

---

##Note- If u have API of other Ai u can also use that Ai API instead of ollama url

# Step 7 - Create Telegram Bot

Open Telegram.

Search for

```
BotFather
```

Create a new bot.

```
/newbot
```

Choose

- Bot Name
- Bot Username

BotFather will provide a Bot Token.

Save this token securely.

Next, send a message to your newly created bot.

Retrieve the Chat ID using the Telegram Bot API.

Update the following variables inside `monitor.py`.

```python
BOT_TOKEN="YOUR_BOT_TOKEN"

CHAT_ID="YOUR_CHAT_ID"

OLLAMA_URL="http://YOUR_WINDOWS_IP:11434/api/generate"
```

---

# Running the Project

## Start Ollama

On Windows:

```cmd
ollama serve
```

---

## Start Cowrie

On Ubuntu:

```bash
cd ~/cowrie

source cowrie-env/bin/activate

bin/cowrie start
```

---

## Start Monitoring Script

Open another terminal.

```bash
cd AI-SOC-with-Cowrie-Ollama/scripts
```

Run

```bash
python3 monitor.py
```

Expected output:

```text
============================================================
Monitoring Cowrie...
============================================================
```

The monitoring script is now waiting for new Cowrie events.

---

# Simulating an Attack

Open Kali Linux.

Connect to the Cowrie Honeypot.

```bash
ssh root@<Ubuntu-IP> -p 2222
```

Example

```bash
ssh root@192.168.178.150 -p 2222
```

Enter any password.

Cowrie will record the login attempt.

The monitoring script will automatically detect the new event.

---

# Expected Output

After detecting a new attack, the monitoring script will generate an AI analysis similar to the following.

```
Attack Summary

Threat Level

MITRE ATT&CK Technique

Recommended Security Actions
```

Immediately after the AI analysis, a Telegram notification will be sent to the administrator containing the incident summary.

---
## Optional Wazuh Integration

During development, Wazuh SIEM was configured to monitor Cowrie honeypot logs by collecting events from the `cowrie.json` log file.

The final implementation reads Cowrie logs directly using the Python monitoring script (`monitor.py`) for AI analysis and Telegram notifications. Therefore, Wazuh is an optional enhancement and is not required to run this project.

---

# Troubleshooting

### monitor.py does not detect new events

- Verify that Cowrie is running.
- Verify the Cowrie log file path.
- Confirm that new events are being written to `cowrie.json`.

---

### Ollama connection failed

- Verify that `ollama serve` is running.
- Check the `OLLAMA_URL` inside `monitor.py`.
- Ensure that Windows Firewall allows access to port **11434**.

---

### Telegram alerts are not received

- Verify the Bot Token.
- Verify the Chat ID.
- Ensure that the bot has received at least one message from your Telegram account.

---

### Cowrie is not recording attacks

- Verify that SSH is listening on port **2222**.
- Confirm that Kali Linux can connect to the Ubuntu VM.
- Check the Cowrie log files for errors.
---

# Project Features

The AI-Powered Security Operations Center provides several security automation features designed to reduce manual effort while improving incident visibility.

### Real-Time Honeypot Monitoring
The system continuously monitors the Cowrie SSH Honeypot log file for newly generated security events.

### AI-Powered Incident Analysis
Each newly detected event is analyzed using the Ollama Large Language Model (LLM), which generates a human-readable incident summary.

### Automatic Threat Classification
The AI estimates the severity of the detected activity and categorizes it into an appropriate threat level.

### MITRE ATT&CK Mapping
The generated report attempts to identify the relevant MITRE ATT&CK technique associated with the observed attacker behavior.

### Telegram Alerting
Administrators receive instant notifications through the Telegram Bot API whenever a new incident is detected.

### Local AI Processing
The project uses Ollama running locally, eliminating the need for cloud-based AI services and improving privacy.

### Open-Source Components
The implementation is based entirely on open-source software including Cowrie, Ollama, Python, and Telegram Bot API.

---

# Learning Outcomes

This project helped in understanding and implementing the following cybersecurity concepts:

- Security Operations Center (SOC)
- Honeypot Deployment
- SSH Attack Monitoring
- Log Analysis
- Artificial Intelligence in Cybersecurity
- Security Automation
- Incident Response
- Threat Detection
- Python Programming
- REST API Integration
- JSON Data Processing
- Linux System Administration
- Virtual Machine Deployment
- Telegram Bot Integration

---

# Security Considerations

Before deploying this project, keep the following points in mind.

- Never expose your Telegram Bot Token publicly.
- Replace all sensitive configuration values before publishing the repository.
- Deploy the honeypot in an isolated lab environment.
- Avoid exposing the honeypot directly to production systems.
- Regularly update Cowrie and Ollama.
- Restrict unnecessary network access to the virtual machines.

---

# Future Improvements

The project can be extended with additional capabilities such as:

- Email Alert Notifications
- Web Dashboard
- Flask-Based Management Portal
- VirusTotal Integration
- AbuseIPDB Integration
- GeoIP-Based Attacker Location
- Multiple Honeypot Support
- Docker Deployment
- Threat Intelligence Integration
- SIEM Dashboard Integration
- Automatic PDF Incident Report Generation
- Multi-User Authentication
- Database Storage for Incidents
- WebSocket-Based Live Monitoring

---

# Known Limitations

- Supports only Cowrie SSH Honeypot events.
- AI analysis depends on the quality of the selected language model.
- Requires Ollama to be running before monitoring starts.
- Telegram requires an active internet connection.
- This implementation is intended for educational and research purposes.

---

# References

The following official resources were used during the development of this project.

- Cowrie Documentation
- Wazuh Documentation
- Ollama Documentation
- Python Documentation
- Telegram Bot API Documentation
- MITRE ATT&CK Framework
- Ubuntu Documentation
- VMware Documentation

---

# Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

Please ensure that your code follows good programming practices and includes appropriate documentation.

---

# Acknowledgements

I would like to express my sincere gratitude to my internship mentors, faculty members, and everyone who supported the development of this project.

Special thanks to the open-source community for providing excellent cybersecurity tools including Cowrie, Wazuh, Ollama, Python, and the Telegram Bot API.

---

# Disclaimer

This project has been developed strictly for educational, research, and cybersecurity learning purposes.

The project should only be used in authorized environments and controlled laboratory setups.

The author is not responsible for any misuse of this project.

---

# Author

**Anmol Lohtia**

Bachelor of Technology (Computer Science and Engineering)

Cybersecurity Enthusiast

GitHub: https://github.com/anmollohtia30

LinkedIn: https://www.linkedin.com/in/anmol-lohtia


---

# License

This project is licensed under the MIT License.

See the **LICENSE** file for more information.

---

## If you found this project helpful, consider giving it a ⭐ on GitHub.

Thank you for visiting this repository!