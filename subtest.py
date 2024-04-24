import paho.mqtt.client as mqtt
import time
import json

broker_address = "localhost"
port = 1883
topic = "test/latency"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    received_time = time.time()
    latency = received_time - message['time']
    print(f"Received message at {received_time} with latency: {latency} seconds")

client = mqtt.Client("Subscriber")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port, 60)

client.loop_forever()
