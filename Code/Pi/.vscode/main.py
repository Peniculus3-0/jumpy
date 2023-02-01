print("hello vincent")
import ultime
from machine import Pin

motor = Pin(2, Pin.OUT)

def stopmotor():
    motor.low()

def startmotor():
    motor.high() 


