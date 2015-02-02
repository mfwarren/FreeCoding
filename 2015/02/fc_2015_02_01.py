#!/usr/bin/env python3
# imports go here
import RPi.GPIO as GPIO
import time

#
# Free Coding session for 2015-02-01
# Written by Matt Warren
#


GPIO.setmode(GPIO.BOARD)

CONTROL_PINS = [7, 11, 13, 15]

for pin in CONTROL_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.ouput(pin, 0)


# half-stepping pin sequence
seq = [[1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1],
       [1, 0, 0, 1]]

for i in range(512):
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(CONTROL_PINS[pin], seq[halfstep][pin])
        time.sleep(0.001)

GPIO.cleanup()
