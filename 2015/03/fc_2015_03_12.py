#!/usr/bin/env python3
# imports go here
import pika
import multiprocessing
import time
import random
import json
import logging
import datetime


#
# Free Coding session for 2015-03-12
# Written by Matt Warren
#


logger = logging.getLogger(__name__)


def get_temperatures():
    return {'celcius': [random.randint(10, 20) for i in range(100)],
            'key': 'aiuh234897tyrdb189347ty',
            'taken': str(datetime.datetime.now())}


def start_measuring():
    connection = pika.BlockingConnection()
    channel = connection.channel()
    while True:
        measurement = get_temperatures()
        channel.basic_publish(exchange='', routing_key='test', body=json.dumps(measurement))
        time.sleep(1)
    connection.close()


def producer():
    # start thread to read temperatures
    p = multiprocessing.Process(target=start_measuring)
    p.start()
    time.sleep(1)


def consumer():
    # on main thread read from message queue and process them
    connection = pika.BlockingConnection()

    channel = connection.channel()
    channel.queue_declare(queue='test')  # in case it's not yet created

    for method_frame, properties, body in channel.consume('test'):
        print(str(body))
        try:
            data = json.loads(body.decode('utf-8'))
            print(data)
            channel.basic_ack(method_frame.delivery_tag)
        except ValueError as e:
            logger.exception('parsing error', e)
            logger.warn('parsing error')

        if method_frame.delivery_tag == 100:
            break

    channel.cancel()
    connection.close()

if __name__ == "__main__":
    producer()
    consumer()
