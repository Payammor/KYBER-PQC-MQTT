import paho.mqtt.client as mqtt
import time
import json

broker_address = "localhost"
port = 1883
topic = "test/latency"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client("Publisher")
client.on_connect = on_connect
client.connect(broker_address, port, 60)

def publish_message():
    while True:  # Loop to send messages at intervals
        message = {
            'time': time.time(),
            'data': 'Hello, MQTT!'
        }
        client.publish(topic, json.dumps(message))
        print(f"Message sent at {message['time']}")
        time.sleep(5)  # Sends a message every 5 seconds

# Optionally, use client.loop_start() to run the network loop in a separate thread
client.loop_start()
publish_message()  # Call the function to start sending messages
