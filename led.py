import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
red=12
green=16
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

GPIO.output(red,False)
GPIO.output(green,False)

while True:
	continue

