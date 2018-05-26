#!/usr/bin/python
import subprocess
import sys
import time
import RPi.GPIO as GPIO
from datetime import datetime

sleep = time.sleep
now = time.strftime("%Y%m%d_%H%M%S", time.gmtime())

def laser():
    from gpiozero import DigitalOutputDevice
    laser = DigitalOutputDevice(17)
    laser.on()
    return True;

def laseron():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.HIGH)
    return True;

def sensor():
    from gpiozero import LightSensor    
    ldr = LightSensor(4)
    return ldr.value;

def detection():
    from gpiozero import LightSensor    
    ldr = LightSensor(4)
    ldr.when_dark = lambda: print("intruder")
    return True;

def led():
    from gpiozero import LED
    led = LED(18)
    led.on()
    return True;

def ledoff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.LOW)
    return True;

def ledon():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    print"Laser on"
    return True;

def camera():
    from picamera import PiCamera
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture("/pictures/tripwire-" + now + ".jpg")
    camera.stop_preview()
    return;

#camera()
#ledon()
#led()
#laser()
print detection()
#sensor()
