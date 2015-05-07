#!/usr/bin/env python3
# imports go here
import paho.mqtt.client as mqtt
import threading
import random
import time
import json

#
# Free Coding session for 2015-05-06
# Written by Matt Warren
#


def mqtt_connected(client, userdata, flags, rc):
    client.subscribe('temperatures')

def mqtt_message(client, userdata, msg):
    print(msg.payload.decode('utf8'))
    data = json.loads(msg.payload.decode('utf8'))
    client.publish('%s/thanks' % data['number'])

def publisher(number):

    def pub_connected(client, userdata, flags, rc):
        client.subscribe('%s/thanks' % number)

    def pub_on_message(client, userdata, msg):
        print("got a thank you!")

    client = mqtt.Client()
    client.on_connect = pub_connected
    client.on_message = pub_on_message
    client.connect('localhost', 1883, 60)

    for i in range(10):
        time.sleep(random.randint(0, 5))
        client.publish('temperatures', '{"val": 20.5, "number": %s}' % number)
        client.loop()
    client.loop()

    client.disconnect()

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = mqtt_connected
    client.on_message = mqtt_message

    client.connect('localhost', 1883, 60)

    threads = []
    for i in range(10):
        t = threading.Thread(target=publisher, args=[i])
        threads.append(t)
        t.start()

    client.loop_forever()

    for t in threads:
        t.join()
