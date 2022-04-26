# MicroPython dcmotor driver

import utime
from machine import Pin

# motor left pin layout
motor1a = Pin(13, Pin.OUT)
motor1b = Pin(12, Pin.OUT)
# motor right pin layout
motor2a = Pin(11, Pin.OUT)
motor2b = Pin(10, Pin.OUT)


# motor left functions
def forward_left():
    motor1a.high()
    motor1b.low()


def backward_left():
    motor1a.low()
    motor1b.high()


def stop_left():
    motor1a.low()
    motor1b.low()


# motor left functions
def forward_right():
    motor2a.high()
    motor2b.low()


def backward_right():
    motor2a.low()
    motor2b.high()


def stop_right():
    motor2a.low()
    motor2b.low()


def forward():
    forward_left()
    forward_right()


def backward():
    backward_left()
    backward_right()


def rightward():
    forward_left()
    stop_right()


def leftward():
    stop_left()
    forward_right()


def stop():
    stop_left()
    stop_right()


# test motor left
def start_test():
    forward_left()
    utime.sleep(2)
    backward_left()
    utime.sleep(2)
    stop_left()

    forward_right()
    utime.sleep(2)
    backward_right()
    utime.sleep(2)
    stop_right()

    forward_all()
    utime.sleep(4)
    stop_all()

    backward_all()
    utime.sleep(4)
    stop_all()


# for i in range(2):
#     start_test()
