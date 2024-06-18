from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels=16)


def servo1():
    for a in range(80,100):
        kit.servo[10].angle = a
        sleep(0.008)
        
    for a in range(100,80,-1):
        kit.servo[10].angle = a
        sleep(0.008)
        
def servo2():
    for a in range(80,100):
        kit.servo[9].angle = a
        sleep(0.008)
        
    for a in range(100,80,-1):
        kit.servo[9].angle = a
        sleep(0.008)
        
def servo3():
    for a in range(80,100):
        kit.servo[14].angle = a
        sleep(0.008)
        
    for a in range(100,80,-1):
        kit.servo[14].angle = a
        sleep(0.008)
        
def servo4():
    for a in range(80,100):
        kit.servo[15].angle = a
        sleep(0.008)
        
    for a in range(100,80,-1):
        kit.servo[15].angle = a
        sleep(0.008)
        
        
# Servo 10: upper left leg
        
while True:
    # servo1()
    # servo2()
    servo3()
    # servo4()
