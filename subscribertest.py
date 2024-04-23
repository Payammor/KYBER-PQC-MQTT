import paho.mqtt.client as mqtt
import time
import json
import schedule

broker_address = "localhost"
port = 1883
topic = "test/latency"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client("Publisher")
client.on_connect = on_connect
client.connect(broker_address, port, 60)

def publish_message():
    message = {
        'time': time.time(),
        'data': 'Hello, MQTT!'
    }
    client.publish(topic, json.dumps(message))
    print(f"Message sent at {message['time']}")

# Set up a schedule to run the publish_message function every 5 seconds
schedule.every(5).seconds.do(publish_message)

# Start the loop
client.loop_start()

while True:
    schedule.run_pending()
    time.sleep(1)
