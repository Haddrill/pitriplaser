#!/usr/bin/python

from gpiozero import DigitalOutputDevice
from time import sleep

laser = DigitalOutputDevice(17)

while True:
    #print('laser on')
    laser.toggle()

    sleep(0.01)
