#!/usr/bin/python3

import RPi.GPIO as GPIO
import time as time
import datetime

SEND_PIN = 12
SWITCH_PIN = 13

#Kanal A-Ein
A_on = '0001100010111000000011111010010000'
A_off = '0001100010111000000011101010010100'

short = 0.00028
long = 0.0008
gap = 0.0096
retries = 16

def senden(signal):
    startTime = datetime.datetime.now()
    
    for j in range(retries):
        for i in signal:
            if i=='0':
                GPIO.output(SEND_PIN,1)
                time.sleep(short)
                GPIO.output(SEND_PIN,0)
                time.sleep(long)
            elif i=='1':
                GPIO.output(SEND_PIN,1)
                time.sleep(long)
                GPIO.output(SEND_PIN,0)
                time.sleep(short)
            else:
                continue
        GPIO.output(SEND_PIN,0)
        time.sleep(gap)
    
    stopTime = datetime.datetime.now()
    
    #print("Execution Time: ", stopTime-startTime)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SEND_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN)

oldStatus = False

while True:
    newStatus = bool(GPIO.input(SWITCH_PIN))
    if oldStatus != newStatus:
        if newStatus:
            print("Licht geht an ...")
            senden(A_on)
        else:
            print("Licht geht aus ...")
            senden(A_off)
        oldStatus = newStatus
    time.sleep(0.1)

    









