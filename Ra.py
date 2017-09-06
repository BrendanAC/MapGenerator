import RPi.GPIO as GPIO
import time
class ServoControl:
    def __init__(self,pin):
        GPIO.setmod(GPIO.BOARD)
        GPIO.setup(pin,GPIO.OUT)
        self.p=GPIO.PWM(pin,50)


    def rotate(self,whatFloor):
        self.p.start(7.5)
        if(whatFloor==0):
            self.p.ChangeDutyCycle(2.5)
        elif whatFloor==1:
            self.p.ChangeDutyCycle(12.5)
        time.sleep(1)


