import os
from email import header

from dotenv import load_dotenv
import requests

load_dotenv()

url = os.getenv("WATCH_URL")

headers = {
    "Content-Type": "application/json"
}

def send_metrics(data):
    try:
        response = requests.post(url, headers=headers, json=data)
        print("Status Code:", response.status_code)
        print("Response:", response.text)

    except requests.exceptions.RequestException as e:
        print("Error sending request:", e)