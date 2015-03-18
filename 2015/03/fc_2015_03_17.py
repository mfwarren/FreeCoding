#!/usr/bin/env python3
# imports go here
import pika
import multiprocessing
import time
import logging

#
# Free Coding session for 2015-03-17
# Written by Matt Warren
#


logger = logging.getLogger(__name__)


def talker():
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.exchange_declare(exchange='chat', type='fanout')

    for i in range(10):
        channel.basic_publish(exchange='chat', routing_key='', body=('%d' % i))
        time.sleep(1)

    connection.close()


def start_listening():
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.exchange_declare(exchange='chat', type='fanout')
    queue = channel.queue_declare(exclusive=True)  # creates a fresh new queue

    # bind the queue to our chat exchange
    channel.queue_bind(exchange='chat', queue=queue.method.queue)

    def print_messages(ch, method, properties, body):
        # callback for consuming from queue
        print(str(body))

    channel.basic_consume(print_messages, queue=queue.method.queue, no_ack=True)
    channel.start_consuming()


def listener():
    p = multiprocessing.Process(target=start_listening)
    p.start()


if __name__ == '__main__':
    listener()
    listener()
    talker()
