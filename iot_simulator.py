import time
import json
import random
from google.cloud import pubsub_v1
from google.oauth2 import service_account

# ===== CONFIG =====
project_id = "steel-league-483016-f0"
topic_id = "temperature-readings"
credentials_path = "key.json"

# ===== AUTH =====
credentials = service_account.Credentials.from_service_account_file(
    credentials_path
)

publisher = pubsub_v1.PublisherClient(credentials=credentials)
topic_path = publisher.topic_path(project_id, topic_id)

print("Simulated IoT device started...")

while True:
    temperature = round(random.uniform(20.0, 35.0), 2)

    payload = {
        "device_id": "sim-device-001",
        "temperature": temperature,
        "timestamp": time.time()
    }

    data = json.dumps(payload).encode("utf-8")

    future = publisher.publish(topic_path, data)
    print(f"Published: {payload}")

    time.sleep(5)