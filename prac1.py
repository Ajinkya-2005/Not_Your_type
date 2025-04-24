import RPi.GPIO as GPIO
import time 
x = 1;
numtimes=int(input("Enter the total no "))
speed = float(input("Enter length "))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

def Blink(numtimes,speed):
    for i in range(0,numtimes):
        GPIO.output(40,True)
        GPIO.output(3,True)
        print("Iteration ",(i+1))
        time.sleep(speed)
        GPIO.output(40,False)
        GPIO.output(3,False)
        time.sleep(speed)
Blink(numtimes,speed)
print('Done')
