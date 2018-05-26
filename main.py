#!/usr/bin/python
import subprocess
import sys
import time
import RPi.GPIO as GPIO
from gpiozero import LightSensor    

sleep = time.sleep
start = time.strftime("%Y%m%d_%H%M%S", time.gmtime())

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

# Send an email using specified email script
def email(now):
    script = 'mailgun.sh'
    # if a different email script is used, the options below will most likely need to be modified.
    subprocess.call([script, '-s', 'Tripped laser', '-b', "Tripped: " + now, '-a', '/pictures/' + now + '.jpg'])
    return True;

# Detects if the Light sensor has become dark
def detection():
    while True:
        light = sensor()
        print light
        if light < .5:
            print "Tripped"
            now = time.strftime("%Y%m%d_%H%M%S", time.gmtime())
            ledon()
            camera(now)
            email(now)
        if light >= .5:
            ledoff()
        sleep(1)
    return;

# Turns LED off using GPIO library
def ledoff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.LOW)
    #print "LED off"
    return True;

# Turns LED on using GPIO library
def ledon():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    #print"LED on"
    return True;

# Takes a picture using the picamera and saves it to /pictures directory with timestamp
def camera(filename):
    from picamera import PiCamera
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture("/pictures/" + filename + ".jpg")
    camera.stop_preview()
    return;

#camera()
#ledon()
#laser()
detection()
#sensor()
