print("hello vincent")
from machine import Pin
import time

"""
motor = Pin(2, Pin.OUT)

def stopmotor():
    motor.low()

def startmotor():
    motor.high()
"""
from machine import Pin
from time import sleep


pin = Pin("LED", Pin.OUT)


