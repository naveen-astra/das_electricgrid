import requests
import numpy as np
import time

THINGSPEAK_API_KEY = "0OGUIHLEXSKSD6C6"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

def send_mock_data():
    for _ in range(20):  # Simulate 20 data points
        strain_value = np.sin(time.time()) + np.random.normal(0, 0.1)  # Mock strain signal
        payload = {"api_key": THINGSPEAK_API_KEY, "field1": strain_value}
        response = requests.post(THINGSPEAK_URL, data=payload)
        print(f"📡 Sent {strain_value}, Response: {response.text}")
        time.sleep(2)  # Send every 10 seconds

if __name__ == "__main__":
    send_mock_data()
