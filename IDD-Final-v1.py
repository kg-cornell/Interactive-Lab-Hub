import RPi.GPIO as GPIO          
from time import sleep

in1 = 24 #change me to actual GPIO physical pin number
in2 = 23 #change me to actual GPIO physical pin number

in3 = 10 #change me to actual GPIO physical pin number
in4 = 11 #change me to actual GPIO physical pin number

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

#This loop goes on forever
while(1):
    #Rotate the 1 motor in the direction of "IN-1"
    GPIO.output(in1,GPIO.HIGH)

    #Make sure the direction "IN-2" is off
    GPIO.output(in2,GPIO.LOW)
    sleep(10) #Let the motor run for x amount of seconds

    GPIO.output(in1,GPIO.LOW)
    #Make sure the direction "IN-2" is off
    GPIO.output(in2,GPIO.LOW)
    sleep(3) #Let the motor run for x amount of seconds

    #Rotate the 1 motor in the direction of "IN-2"
    GPIO.output(in2,GPIO.HIGH)
    #Make sure the direction "IN-1" is off
    GPIO.output(in1,GPIO.LOW)
    sleep(10) #Let the motor run for x amount of seconds
   
    #Rotate the 1 motor in the direction of "IN-3"
    GPIO.output(in3,GPIO.HIGH)

    #Make sure the direction "IN-4" is off
    GPIO.output(in4,GPIO.LOW)
    sleep(10) #Let the motor run for x amount of seconds

    GPIO.output(in3,GPIO.LOW)
    #Make sure the direction "IN-4" is off
    GPIO.output(in4,GPIO.LOW)
    sleep(3) #Let the motor run for x amount of seconds

    #Rotate the 1 motor in the direction of "IN-4"
    GPIO.output(in4,GPIO.HIGH)
    #Make sure the direction "IN-3" is off
    GPIO.output(in3,GPIO.LOW)
    sleep(10) #Let the motor run for x amount of seconds
