#!/usr/bin/python3

from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO
import sys as sys
import pickle
import time

RECEIVED_SIGNAL = [[], []]  #[[time of reading], [signal reading]]
MAX_DURATION = 5
SEND_PIN = 12


print("Loading Data")
file = open("/home/thomas/Python/dump.bin","rb")
signals = pickle.load(file)
print(len(signals[1]), " samples loaded from file")

print('**Plotting results**')
lastTime = 0.0
timeStamps = []
for i in range(len(signals[0])):
    lastTime = lastTime + signals[0][i]
    timeStamps.append(lastTime)
    
pyplot.plot(timeStamps, signals[1])
pyplot.axis([0, MAX_DURATION, -1, 2])
pyplot.show()
