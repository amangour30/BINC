import time
import RPi.GPIO as GPIO
import imutils

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
pwmTop=GPIO.PWM(18,50)
pwmBottom = GPIO.PWM(11, 50)
pwmTop.start(1)
pwmBottom.start(1)


def updateTop(angle):
	dutyTop = float(angle) / 10.0 + 2.5
        pwmTop.ChangeDutyCycle(dutyTop)

def updateBottom(angle):
	dutyBottom = float(angle) / 10.0 + 2.5
        pwmBottom.ChangeDutyCycle(dutyBottom)

def goToBin(bin):
	if bin is 1:
		updateBottom(0)
	elif bin is 2:
		updateBottom(45)
	elif bin is 3:
		updateBottom(90)
	time.sleep(2)

def drop():
	updateTop(50)
	time.sleep(2)
	updateTop(-5)
	time.sleep(2)

def dropIn(item):
	goToBin(item)
	drop()
	

dropIn(3)
dropIn(2)
dropIn(1)

GPIO.cleanup()
