# Installation Guide

## Overview

This document describes how to install and configure the AI-Powered Security Operations Center (SOC) project.

---

# Requirements

Hardware

- Intel Core i5 or higher
- Minimum 8 GB RAM
- 50 GB Free Storage

Software

- Windows 10/11
- Ubuntu 24.04 LTS
- Kali Linux
- VMware Workstation
- Python 3
- Cowrie Honeypot
- Ollama
- Git

---

# Step 1 - Clone Repository

```bash
git clone https://github.com/anmollohtia30/AI-SOC-with-Cowrie-Ollama.git
```

---

# Step 2 - Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 3 - Install Cowrie

```bash
git clone https://github.com/cowrie/cowrie.git
```

Create a virtual environment:

```bash
python3 -m venv cowrie-env
```

Activate it:

```bash
source cowrie-env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Step 4 - Configure Cowrie

Copy the example configuration file.

Update:

- SSH port
- Logging
- Authentication settings

---

# Step 5 - Install Ollama

Install Ollama on the Windows host.

Start the service:

```cmd
ollama serve
```

Download the model:

```cmd
ollama pull llama3.2:3b
```

---

# Step 6 - Configure Telegram

Create a bot using BotFather.

Obtain:

- Bot Token
- Chat ID

Update `monitor.py`:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
OLLAMA_URL = "http://YOUR_WINDOWS_IP:11434/api/generate"
```

---

# Step 7 - Run the Project

Start Cowrie:

```bash
bin/cowrie start
```

Start the monitoring script:

```bash
python3 monitor.py
```

---

# Step 8 - Simulate an Attack

From Kali Linux:

```bash
ssh root@<Ubuntu-IP> -p 2222
```

Enter any password.

---

# Step 9 - Verify the Output

Successful execution should produce:

- Cowrie log entry
- AI-generated analysis
- Telegram notification

---

# Troubleshooting

## Cowrie is not generating logs

- Verify Cowrie is running.
- Check the log file path.

## Ollama is not responding

- Verify `ollama serve` is running.
- Check the API URL.

## Telegram alerts are not received

- Verify the Bot Token.
- Verify the Chat ID.