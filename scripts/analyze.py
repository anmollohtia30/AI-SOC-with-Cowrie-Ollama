import json
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
# TELEGRAM FUNCTION
# ==========================

def send_telegram(message):
    url = f"TELEGRAM API"

    data = {
        "chat_id":CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)

    print("\n========== TELEGRAM ==========")
    print("Status:", response.status_code)
    print("Response:", response.text)
    print("==============================\n")


# ==========================
# READ LAST COWRIE EVENT
# ==========================

with open(LOG_FILE, "r") as f:
    lines = f.readlines()

if len(lines) == 0:
    print("No Cowrie logs found.")
    exit()

last_event = json.loads(lines[-1])

print("=" * 60)
print("Latest Cowrie Event")
print("=" * 60)
print(json.dumps(last_event, indent=4))


# ==========================
# CREATE AI PROMPT
# ==========================

prompt = f"""
You are an expert SOC analyst.

Analyze the following Cowrie honeypot event.

Return:

1. Attack Summary
2. Threat Level (Low / Medium / High)
3. MITRE ATT&CK Technique
4. Recommended Action

Event:

{json.dumps(last_event, indent=4)}
"""

payload = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False
}

print("\nSending event to Ollama...\n")

response = requests.post(OLLAMA_URL, json=payload)

if response.status_code != 200:
    print("Ollama Error")
    print(response.status_code)
    print(response.text)
    exit()

result = response.json()

analysis = result["response"]

print("=" * 60)
print("AI ANALYSIS")
print("=" * 60)
print(analysis)


# ==========================
# TELEGRAM MESSAGE
# ==========================

telegram_message = f"""
🚨 AI SOC Alert 🚨

Source IP: {last_event.get("src_ip")}

Protocol: {last_event.get("protocol")}

Event: {last_event.get("eventid")}

Time: {last_event.get("timestamp")}

AI Analysis:

{analysis}
"""


send_telegram(telegram_message)

print("✅ Finished.")
