print("hello vincent")
import FaBo9Axis_MPU9250
import time
import sys
from machine import Pin

motor = Pin(2, Pin.OUT)

def stopmotor():
    motor.low()

def startmotor():
    motor.high()


