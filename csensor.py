#!/usr/bin/python
class Sensor(object):
    from gpiozero import LightSensor

    @staticmethod
    def g():
        ldr = LightSensor(4)
        print("light value: " + ldr.value)
        return ldr.value;

