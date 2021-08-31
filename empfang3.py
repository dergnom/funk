#!/usr/bin/python3
from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO
import sys as sys
import pickle
import time

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]
timeStamps = []
MAX_DURATION = 5
RECEIVE_PIN = 23
SEND_PIN = 12

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RECEIVE_PIN, GPIO.IN)
    #GPIO.setup(SEND_PIN, GPIO.OUT)
    cumulative_time = 0
    beginning_time = datetime.now()
    last_time = beginning_time
    print('**Started recording**')
    while cumulative_time < MAX_DURATION:
        now = datetime.now()
        time_delta1 = now - beginning_time
        time_delta2 = now - last_time
        last_time = now
        RECEIVED_SIGNAL[0].append(time_delta2.microseconds/1000000.0)
        RECEIVED_SIGNAL[1].append(int(GPIO.input(RECEIVE_PIN)))
        cumulative_time = time_delta1.seconds
    print( '**Ended recording**')
    print(len(RECEIVED_SIGNAL[0]), 'samples recorded')
    GPIO.cleanup()
      
    print(RECEIVED_SIGNAL[0][0])
    print(RECEIVED_SIGNAL[0][23])

    print("Saving Data")
    fobj = open("/home/thomas/Python/dump.bin","w+b")
    pickle.dump(RECEIVED_SIGNAL,fobj)
    fobj.close()
       

    print('**Plotting results**')
    lastTime = 0.0
    for i in range(len(RECEIVED_SIGNAL[0])):
        lastTime = lastTime + RECEIVED_SIGNAL[0][i]
        timeStamps.append(lastTime)
        
    pyplot.plot(timeStamps, RECEIVED_SIGNAL[1])
    pyplot.axis([0, MAX_DURATION, -1, 2])
    pyplot.show()
