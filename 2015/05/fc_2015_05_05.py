#!/usr/bin/env python3
# imports go here
import paho.mqtt.client as mqtt
import threading
import random
import time
#
# Free Coding session for 2015-05-05
# Written by Matt Warren
#


def mqtt_connected(client, userdata, flags, rc):
    client.subscribe('#')

def mqtt_message(client, userdata, msg):
    print(msg)

def publisher():

    client = mqtt.Client()
    client.connect('localhost', 1883, 60)

    for i in range(10):
        time.sleep(random.randint(0, 5))
        client.publish('temperature', '20.5')
        client.loop()

    client.disconnect()

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = mqtt_connected
    client.on_message = mqtt_message

    client.connect('localhost', 1883, 60)

    threads = []
    for i in range(10):
        t = threading.Thread(target=publisher)
        threads.append(t)
        t.start()

    client.loop_forever()

    for t in threads:
        t.join()
