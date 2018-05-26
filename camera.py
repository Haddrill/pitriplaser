#!/usr/bin/python

from picamera import PiCamera
import time

sleep = time.sleep
now = time.strftime("%Y%m%d_%H%M%S", time.gmtime())
camera = PiCamera()

camera.start_preview()
sleep(5)

camera.capture('/pictures/' + now + '.jpg')

camera.stop_preview()
