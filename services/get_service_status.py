import os
import json
import subprocess
from dotenv import load_dotenv

def get_service_status():
    load_dotenv()

    try:
        services = json.loads(os.getenv("SERVICES", "[]"))
    except json.JSONDecodeError:
        return {"error": "Invalid SERVICES format in .env"}

    if not services:
        return {"error": "No services defined"}

    try:
        result = subprocess.run(
            ["systemctl", "is-active", *services],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        outputs = result.stdout.strip().split("\n")

        # Map each service to its status
        return {svc: status for svc, status in zip(services, outputs)}

    except Exception as e:
        return {"error": str(e)}
