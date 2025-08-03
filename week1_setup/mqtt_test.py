"""
mqtt_test.py

This script publishes messages to a local MQTT broker (Mosquitto) on two different topics.
It's designed to test a simple control lab setup where Node-RED acts as the subscriber.

Requirements:
- Mosquitto broker running locally on port 1883
- paho-mqtt Python package (`pip install paho-mqtt`)
"""

import paho.mqtt.client as mqtt
import time

# Define the MQTT broker (localhost for local testing)
broker = "localhost"

# Define topics to publish to
topics = ["lab/test", "test/lab"]

# Messages corresponding to each topic
messages = ["Dean's control lab test message 1", "Dean's control lab test message 2"]

# Initialize the MQTT client and connect to broker
client = mqtt.Client()
client.connect(broker)

try:
    # Publish each message to its corresponding topic in a loop
    for i in range(len(topics)):
        msg = messages[i]
        client.publish(topics[i], msg)
        print(f"Published to {topics[i]}: {msg}")
        time.sleep(3)
except KeyboardInterrupt:
    print("Stopped Publisher")
    client.disconnect()

