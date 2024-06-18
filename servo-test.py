from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels=16)


def servo1():
    # for a in range(80,100):
        kit.servo[10].angle = 90
        # sleep(0.008)
        
    # for a in range(100,80,-1):
    #     kit.servo[10].angle = a
    #     sleep(0.008)
        
def servo2():
    # for a in range(80,100):
        kit.servo[11].angle = 90
        sleep(0.008)
        
    # for a in range(100,80,-1):
    #     kit.servo[11].angle = a
    #     sleep(0.008)
        
def servo3():
    # for a in range(80,100):
        kit.servo[14].angle = 90
    #     sleep(0.008)
        
    # for a in range(100,80,-1):
    #     kit.servo[14].angle = a
    #     sleep(0.008)
        
def servo4():
    # for a in range(80,100):
        kit.servo[15].angle = 90
    #     sleep(0.008)
        
    # for a in range(100,80,-1):
    #     kit.servo[15].angle = a
    #     sleep(0.008)
        
        
# Servo 10: upper left leg  
# Servo 14: lower right leg
# Servo 15: upper right leg


while True:
    servo1()
    servo2()
    # servo3()
    # servo4()
