#!/usr/bin/python
import subprocess
import sys
import time
import RPi.GPIO as GPIO
from gpiozero import LightSensor    

sleep = time.sleep
now = time.strftime("%Y%m%d_%H%M%S", time.gmtime())

# Turns laser off using GPIO library
def laseron():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.HIGH)
    return True;

# Turns LDR sensor on and returns a reading
def sensor():
    ldr = LightSensor(4)
    return ldr.value;

# Detects if the Light sensor has become dark
def detection():
    while True:
        light = sensor()
        print light
        if light < .5:
            ledon()
            print "Intruder"
        if light > .5:
            ledoff()
        sleep(1)
    return;

# Turns LED off using GPIO library
def ledoff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.LOW)
    print "LED off"
    return True;

# Turns LED on using GPIO library
def ledon():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    print"LED on"
    return True;

# Takes a picture using the picamera and saves it to /pictures directory with timestamp
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
#laser()
detection()
#sensor()
