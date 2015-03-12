#!/usr/bin/env python3
# imports go here
import pika
import multiprocessing
import time

#
# Free Coding session for 2015-03-11
# Written by Matt Warren
#


def start_producer():
    connection = pika.BlockingConnection()
    channel = connection.channel()
    while True:
        channel.basic_publish(exchange='exchange',
                              routing_key='test',
                              body='Test Message')
        time.sleep(1)
    connection.close()

if __name__ == '__main__':
    p = multiprocessing.Process(target=start_producer)
    p.start()
    time.sleep(1)

    connection = pika.BlockingConnection()

    channel = connection.channel()
    channel.queue_declare(queue='test')

    for method_frame, properties, body in channel.consume('test'):
        print(method_frame)
        print(properties)
        print(body)
        channel.basic_ack(method_frame.delivery_tag)

        if method_frame.delivery_tag == 10:
            break

    requeued_messages = channel.cancel()
    connection.close()
