import paho.mqtt.client as mqtt
import time, threading
import random

def on_connect(client, userdata, flags, rc):
	 print("Connected with result code "+str(rc))
	 client.publish("cloudmqtt/status",payload="Online", qos=0, retain=True)


def on_message(client, userdata, message):
   print("Message Recieved: "+message.payload.decode())

def on_publish(mosq, obj, mid):
    print("Publish count: " + str(mid))


client = mqtt.Client()
client.username_pw_set("yxlhuqjo", "MMLsMSP-IUSv")
client.connect('postman.cloudmqtt.com', 13872, 60)


client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.loop_start()

ticker = threading.Event()


while not ticker.wait(5):
	flow2 = random.uniform(160,168)
	flow = flow2 - random.uniform(1,2)
	power = random.uniform(32,33)
	pressure = random.uniform(57,58)
	pressure2 = random.uniform(2.9,3.1)
	client.publish("/cloudmqtt/flow", flow)
	client.publish("/cloudmqtt/flow2", flow2)
	client.publish("/cloudmqtt/power", power)
	client.publish("/cloudmqtt/pressure", pressure)
	client.publish("/cloudmqtt/pressure2", pressure2)

