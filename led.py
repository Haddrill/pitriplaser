#!/usr/bin/python

from gpiozero import LED
from time import sleep

led = LED(18)


while True:
    #print('laser on')
    led.toggle()

    sleep(0.001)
