#!/usr/bin/python
from picamera import PiCamera
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT) #LED
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button
GPIO.setup(21, GPIO.OUT) #Buzzer

diode = GPIO.PWM(12,50)
diode.start(0)
GPIO.output(21, GPIO.HIGH)

#Camera Configuration

camera = PiCamera()
camera.rotation = 180

#Turn on diode and wait for button
diode.ChangeDutyCycle(80)
GPIO.wait_for_edge(26, GPIO.FALLING)

# Turn off diode and Turn of buzzer
diode.ChangeDutyCycle(0)
GPIO.output(21, GPIO.LOW)
#Wait 5 sec
time.sleep(5)
#Take pic and save it
camera.capture('/home/pi/photo-' + str(int(time.time())) + '.jpg')
#Turn off buzzer
GPIO.output(21, GPIO.HIGH)
