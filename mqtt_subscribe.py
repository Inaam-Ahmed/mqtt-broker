import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "broker.mqttdashboard.com"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)


client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(1)
# client.loop_stop()
