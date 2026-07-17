import json
import time
import requests

# ==========================
# CONFIGURATION
# ==========================

LOG_FILE = "/home/cowrie/cowrie/var/log/cowrie/cowrie.json"

OLLAMA_URL = "http://OLLAMA_URL:11434/api/generate"

MODEL = "llama3.2:3b"

BOT_TOKEN = "TELEGRAM_BOT_TOKEN"
CHAT_ID = "CHAT_ID"

# ==========================
# TELEGRAM
# ==========================

def send_telegram(message):
    url = f"TELEGRAM API"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    r = requests.post(url, data=data)

    print("Telegram Status:", r.status_code)
    print(r.text)


# ==========================
# OLLAMA
# ==========================

def analyze_event(event):

    prompt = f"""
You are an expert SOC analyst.

Analyze this Cowrie honeypot event.

Return:

1. Attack Summary
2. Threat Level
3. MITRE ATT&CK Technique
4. Recommended Action

Event:

{json.dumps(event, indent=4)}
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        print("Ollama Error")
        print(response.text)
        return

    analysis = response.json()["response"]

    print("\n==============================")
    print("AI ANALYSIS")
    print("==============================")
    print(analysis)

    telegram_message = f"""
🚨 AI SOC ALERT 🚨

Source IP: {event.get("src_ip","N/A")}

Protocol: {event.get("protocol","N/A")}

Event: {event.get("eventid","N/A")}

Time: {event.get("timestamp","N/A")}

Threat Analysis:

{analysis}
"""

    send_telegram(telegram_message)


# ==========================
# START MONITORING
# ==========================

print("="*60)
print("Monitoring Cowrie...")
print("="*60)

with open(LOG_FILE, "r") as f:

    # Skip old logs
    f.seek(0, 2)

    while True:

        line = f.readline()

        if not line:
            time.sleep(1)
            continue

        try:
            event = json.loads(line)

            print("\nNew Event Detected")
            print(event.get("eventid"))

            analyze_event(event)

        except Exception as e:
            print("Error:", e)
