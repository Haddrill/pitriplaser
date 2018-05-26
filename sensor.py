#!/usr/bin/python

from gpiozero import LightSensor    
from time import sleep

ldr = LightSensor(4)

while True:
    print(ldr.value)
    sleep(1)
