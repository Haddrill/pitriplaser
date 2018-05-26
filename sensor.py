#!/usr/bin/python

from gpiozero import LightSensor    

ldr = LightSensor(4)

print(ldr.value)
