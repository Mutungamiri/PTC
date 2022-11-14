from random import uniform
import time
import paho.mqtt.client as mqtt
import datetime

localhost = '127.0.0.1'
port = 1883
timeout = 60
topic = "/test/podtest"
Qos = 0

def on_connect(client, userdata, flags, rc):
    print("error = " + str(rc))

for i in range(5):
    obecny = datetime.datetime.now()
    zm1 = obecny.strftime("%d.%m.%Y %H:%M:%S ")
    zm2 = round(uniform(0,10),2)
    message_payload = zm1+str(zm2)

    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(localhost, port, timeout)
    client.publish(topic, message_payload, 0)

    time.sleep(5)

client.disconnect()