import requests
import random
import time
import datetime

# 🔹 Replace with your Firebase Realtime Database URL (NO trailing /)
FIREBASE_URL = "https://geopulse-khs2025-default-rtdb.asia-southeast1.firebasedatabase.app"

def send_all_sensors():
    try:
        # Current time in milliseconds
        timestamp_ms = int(time.time() * 1000)

        # Generate random values (simulate sensors)
        data = {
            "Gyro": random.randint(500, 1000),
            "Moisture": random.randint(500, 1000),
            "Rainfall": random.randint(500, 1000),
            "Vibration": random.randint(500, 1000),
            "Roll": round(random.uniform(-180, 180), 5),
            "Pitch": round(random.uniform(-90, 90), 5),
            "Yaw": round(random.uniform(0, 360), 5),
            "RainPerMinute": round(random.uniform(0.0, 1.0), 4),
            "timestamp": timestamp_ms  # ✅ milliseconds
        }

        # 🔹 Update ONLY the root (no History node touched)
        url = f"{FIREBASE_URL}/.json"
        requests.patch(url, json=data)

        print(f"✅ Updated latest values: {data}")

    except Exception as e:
        print(f"❌ Error sending data: {e}")

def main():
    while True:
        send_all_sensors()
        time.sleep(1)

if __name__ == "__main__":
    main()
