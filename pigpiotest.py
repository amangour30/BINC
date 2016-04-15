import time
 
import pigpio
 
servos = [24,17] #GPIO number
 
pi=pigpio.pi()
#pulsewidth can only set between 500-2500
try:
    while True:
 
        pi.set_servo_pulsewidth(servos[0], 500) #servo 1 to 0 degree
        print("Servo {} {} micro pulses".format(servos, 500))
        time.sleep(1)
       # pi.set_servo_pulsewidth(servos[1], 1500) #servo 2 to 90 degree
        #print("Servo {} {} micro pulses".format(servos, 1500))
        #time.sleep(1)
        pi.set_servo_pulsewidth(servos[0], 1500)
        print("Servo {} {} micro pulses".format(servos, 1500))
        time.sleep(1)
        #pi.set_servo_pulsewidth(servos[1], 500)
        #print("Servo {} {} micro pulses".format(servos, 500))
        #time.sleep(1)
 
   # switch all servos off
except KeyboardInterrupt:
    for s in servos:
 
        pi.set_servo_pulsewidth(s, 0);
 
pi.stop()
