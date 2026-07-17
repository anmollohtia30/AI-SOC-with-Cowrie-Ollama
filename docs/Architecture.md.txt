# System Architecture

## Overview

The AI-Powered Security Operations Center (SOC) is designed to automate the detection, analysis, and reporting of suspicious activities using a Cowrie Honeypot, Python automation, Ollama Large Language Model (LLM), and Telegram Bot API.

The architecture follows a modular approach where each component performs a specific task and communicates with the next component in the workflow.

---

## Architecture Diagram



---

## Components

### 1. Kali Linux (Attacker)

Kali Linux is used to simulate attacker activities by initiating SSH connections to the Cowrie Honeypot. It represents the attacker's machine in the lab environment.

Responsibilities:
- Perform SSH login attempts
- Execute commands
- Generate attack events

---

### 2. Cowrie Honeypot

Cowrie is an SSH and Telnet honeypot designed to capture attacker behavior.

Responsibilities:
- Capture login attempts
- Record executed commands
- Log session details
- Store events in JSON format

Output File:

```
cowrie.json
```

---

### 3. Python Monitoring Script

The `monitor.py` script continuously monitors the Cowrie JSON log file.

Responsibilities:
- Detect new events
- Parse JSON logs
- Send data to Ollama
- Receive AI analysis
- Forward alerts to Telegram

---

### 4. Ollama LLM

Ollama hosts the Llama 3.2 language model locally.

Responsibilities:
- Analyze Cowrie events
- Generate attack summaries
- Estimate threat level
- Suggest mitigation steps

---

### 5. Telegram Bot

The Telegram Bot API delivers AI-generated alerts to the administrator.

Responsibilities:
- Receive formatted messages
- Notify the administrator in real time

---

### 6. SOC Administrator

The administrator receives the AI-generated incident report and can take appropriate action based on the analysis.

---

## Data Flow

1. Attacker initiates SSH connection.
2. Cowrie captures the activity.
3. Cowrie stores the event in `cowrie.json`.
4. `monitor.py` detects the new event.
5. Event is sent to Ollama.
6. Ollama generates an AI incident report.
7. Report is sent to Telegram.
8. Administrator receives the alert.

---

## Advantages

- Real-time monitoring
- AI-assisted incident analysis
- Automated alerting
- Easy deployment
- Beginner-friendly
- Open-source implementation
