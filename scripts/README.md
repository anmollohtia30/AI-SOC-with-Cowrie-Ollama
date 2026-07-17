# Scripts

This folder contains the Python scripts used in the AI-Powered Security Operations Center (SOC) project.

## Files

### monitor.py
This is the main monitoring script of the project.

Functions:
- Continuously monitors the Cowrie JSON log file.
- Detects newly generated security events.
- Sends the event to the Ollama Large Language Model (LLM) for analysis.
- Receives the AI-generated incident summary.
- Sends the analysis to the administrator through the Telegram Bot API.

### analyze.py
This script was used during the development and testing phase.

Functions:
- Reads the latest event from the Cowrie log file.
- Sends the event to Ollama.
- Displays the AI-generated incident analysis in the terminal.
- Helps verify that the AI integration is working correctly.

## Requirements

Install the required Python package before running the scripts.

```bash
pip install -r ../requirements.txt
```

## Notes

- Update the TELEGRAM_BOT_TOKEN, CHAT_ID and TELEGRAM API values before running the project.
- Update the OLLAMA_URL according to your system.
- Ensure Ollama is running before executing monitor.py.
- Ensure Cowrie Honeypot is generating logs.

##Lines that u change
OLLAMA_URL = "http://OLLAMA_URL:11434/api/generate"
BOT_TOKEN = "TELEGRAM_BOT_TOKEN"
CHAT_ID = "CHAT_ID"
url = f"TELEGRAM API"
"chat_id":CHAT_ID,