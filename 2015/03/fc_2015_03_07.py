#!/usr/bin/env python3
# imports go here
import socket
import multiprocessing
import time

#
# Free Coding session for 2015-03-07
# Written by Matt Warren
#


def start_server():
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_address = ('::1', 10000)
    sock.bind(server_address)
    sock.listen(1)

    while True:
        print("server waiting")
        conn, client_addr = sock.accept()
        try:
            while True:
                data = conn.recv(32)
                if data:
                    conn.sendall(data)
                else:
                    break
        finally:
            conn.close()

if __name__ == '__main__':

    p = multiprocessing.Process(target=start_server)
    p.start()

    time.sleep(1)  # time to spin up server

    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_address = ('::1', 10000)
    sock.connect(server_address)

    try:
        message = b"going to send this message to the receiving socket"
        sock.sendall(message)

        received = 0
        expected = len(message)

        while received < expected:
            data = sock.recv(32)
            received += len(data)
            print(data)
    finally:
        sock.close()
