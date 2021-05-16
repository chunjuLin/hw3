import paho.mqtt.client as paho
import time

import serial
import time
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 9600)

# https://os.mbed.com/teams/mqtt/wiki/Using-MQTT#python-client

# MQTT broker hosted on local machine
mqttc = paho.Client()

# Settings for connection
# TODO: revise host to your IP
host = "172.20.10.5"
topic = "Mbed"

angle = 0

# Callbacks
def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
   # if int.from_bytes(msg.payload) >= 30:
    recieved_msg = str(msg.payload).split('\\')[0][2:]
    print(recieved_msg)
    mode = int(recieved_msg.split(',')[0])
    value = int(recieved_msg.split(',')[1])
    if mode == 1:
        s.write(bytes("/Gesture_ui/run 0 \r", 'UTF-8'))
    elif mode == 2:
        s.write(bytes("/Tilt_angle/run 0 \r", 'UTF-8'))
    print("[Received] Topic: " + msg.topic + ", Message: " + str(msg.payload) + "\n")

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")

# Set callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

# Connect and subscribe
print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)

#Publish messages from Python
# num = 0
# while num != 5:
#     ret = mqttc.publish(topic, "/gesture_ui/run 0 \r\n", qos=0)
#     if (ret[0] != 0):
#             print("Publish failed")
#     mqttc.loop()
#     time.sleep(1.5)
#     num += 1

# Loop forever, receiving messages
mqttc.loop_forever()
