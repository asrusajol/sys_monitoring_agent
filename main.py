import json
import os
import time
from dotenv import load_dotenv
from services.get_resource_uese import get_resource_status
from services.get_service_status import get_service_status
from services.send_metrics import send_metrics


if __name__ == "__main__":
    load_dotenv()
    while True:
        client_name = os.getenv("CLIENT_NAME")
        statuses = get_service_status()
        resources_uses = get_resource_status()

        status = {
            "client_name": client_name,
            "services": statuses,
            "resources": resources_uses
        }

        send_metrics(status)
        print(json.dumps(status, indent=2))
        print("########################################################")
        time.sleep(1)