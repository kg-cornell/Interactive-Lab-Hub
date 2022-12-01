import RPi.GPIO as GPIO          
from time import sleep

in1 = 5 #change me to actual GPIO physical pin number
in2 = 6 #change me to actual GPIO physical pin number

in3 = 20 #change me to actual GPIO physical pin number
in4 = 21 #change me to actual GPIO physical pin number

#Set the intended pins as inputs/outputs for the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

#Set the initial outputs to be low so the motors are not in motion prematurely
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

print("device is prepared to run")
sleep(2)

#This loop goes on forever
while(1):
    print("in loop")
    
    print("move forward")
    sleep(2)
    #Move forward
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    sleep(10)

    print("stop")
    sleep(2)
    #Stop
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    sleep(5)
    
    print("turn left")
    sleep(2)
    #Turn Left
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(10)

    print("stop")
    sleep(2)
    #Stop
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    sleep(5)
    
    print("move backward")
    sleep(2)
    #Move backward
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(10)

    print("stop")
    sleep(2)
    #Stop
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    sleep(5)
    
    print("turn right")
    sleep(2)
    #Turn Right
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    sleep(10)
    
    print("stop")
    sleep(2)
    #Stop
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    sleep(5)
    break
