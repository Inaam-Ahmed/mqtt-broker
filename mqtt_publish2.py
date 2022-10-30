import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "broker.mqttdashboard.com"
client = mqtt.Client("Temperature_Outside")
client.connect(mqttBroker)

while True:
    randNumber = randrange(10)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
