from adafruit_servokit import ServoKit
import math
from time import sleep
kit = ServoKit(channels=16)

LeftLower = 10
LeftUpper = 11
RightLower = 14
RightUpper = 15

def servo1():
    for a in range(80,100):
        kit.servo[10].angle = 90
        sleep(0.008)
        
    for a in range(100,80,-1):
        kit.servo[10].angle = a
        sleep(0.008)
        
def servo2():
    for a in range(80,100):
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



def calculateLegJointsInDeg(x, y, z):
    lowerLeg = 100
    upperLeg = 100
    lowerLegOffset = 24.24

    #Put leg offset logic here
    #something like: y = y + lowerLegOffset
    if (y == 0):
        y = 0.00001
  
    if (x == 0):
        x = 0.00001

    #Different calculation incase of no Z offset.
    if (z == 0):
        s = y
        shoulderLegAngle = -0.5*math.pi
    else:
        s = math.sqrt((y*y)+(z*z))
        shoulderLegAngle = math.atan(y/z)

    #Refer to Readme.md for explanation.
    lowerLegAngle = math.acos((x*x + s*s - lowerLeg*lowerLeg - upperLeg*upperLeg)/(2*lowerLeg*upperLeg))
    upperLegAngle = math.atan(s/x)-math.atan((upperLeg*math.sin(lowerLegAngle))/(lowerLeg+upperLeg*math.cos(lowerLegAngle)))
    
    #Radians to degrees + fysical offsets.
    upperLegAngle = 225 + ((upperLegAngle*180)/math.pi)
    lowerLegAngle = 180 - ((lowerLegAngle*180)/math.pi)
    shoulderLegAngle = 180 + ((shoulderLegAngle*180)/math.pi)

    #Put leg offset logic here.

    #Calculates angle difference due to upper leg state.
    diffUpperLeg = upperLegAngle - 90
    lowerLegAngle = lowerLegAngle - diffUpperLeg 

    #Invert upperLegAngle due to inverted motor rotation.
    upperLegAngle = 180 - upperLegAngle

    #If angles are negative turn into positive values.
    #Needed because sinus and cosinus functions have possibilities in positive and negative values.
    #Real world always need positive values.
    if(upperLegAngle <= 0):
        upperLegAngle = 180 + upperLegAngle
    if(lowerLegAngle <= 0):
        lowerLegAngle = 180 + lowerLegAngle

    return lowerLegAngle, upperLegAngle, shoulderLegAngle
        

def revCalculateLegJointsInDeg(x, y, z):
    lowerLeg = 100
    upperLeg = 100
    lowerLegOffset = 24.24

    #Put leg offset logic here
    #something like: y = y + lowerLegOffset
    if (y == 0):
        y = 0.00001
  
    if (x == 0):
        x = 0.00001

    #Different calculation incase of no Z offset.
    if (z == 0):
        s = y
        shoulderLegAngle = -0.5*math.pi
    else:
        s = math.sqrt((y*y)+(z*z))
        shoulderLegAngle = math.atan(y/z)

    #Refer to Readme.md for explanation.
    lowerLegAngle = math.acos((x*x + s*s - lowerLeg*lowerLeg - upperLeg*upperLeg)/(2*lowerLeg*upperLeg))
    upperLegAngle = math.atan(s/x)-math.atan((upperLeg*math.sin(lowerLegAngle))/(lowerLeg+upperLeg*math.cos(lowerLegAngle)))
    
    #Radians to degrees + fysical offsets.
    upperLegAngle = 225 + ((upperLegAngle*180)/math.pi)
    lowerLegAngle = 180 - ((lowerLegAngle*180)/math.pi)
    shoulderLegAngle = 180 + ((shoulderLegAngle*180)/math.pi)

    #Put leg offset logic here.

    #Calculates angle difference due to upper leg state.
    diffUpperLeg = upperLegAngle - 90
    lowerLegAngle = lowerLegAngle - diffUpperLeg 

    #Invert upperLegAngle due to inverted motor rotation.
    upperLegAngle = 180 - upperLegAngle
    # lowerLegAngle = 180 - lowerLegAngle

    #If angles are negative turn into positive values.
    #Needed because sinus and cosinus functions have possibilities in positive and negative values.
    #Real world always need positive values.
    if(upperLegAngle <= 0):
        upperLegAngle = 180 + upperLegAngle
    if(lowerLegAngle <= 0):
        lowerLegAngle = 180 + lowerLegAngle

    return lowerLegAngle, upperLegAngle, shoulderLegAngle

# Servo 11: lower left leg
# Servo 10: upper left leg  
# Servo 14: lower right leg
# Servo 15: upper right leg

def setServo(servo: int, angle: float):
    kit.servo[servo].angle = angle

min = 70
max = 120

def changeHeight(newVal: float, oldVal: float):
     for a in range(oldVal*10, newVal*10, 1):
        b = a/10
        leftLowerValue, leftUpperValue, unused = calculateLegJointsInDeg(20, -1*b, 0)
        setServo(LeftLower, leftLowerValue)
        setServo(LeftUpper, leftUpperValue)
        setServo(RightLower, 180 - leftLowerValue)
        setServo(RightUpper, 180 - leftUpperValue)
        sleep(0.008)

while True:
    changeHeight(120, 70)
    changeHeight(70, 120)
    # print("up")
    # for a in range(min,max):
    #     leftLowerValue, leftUpperValue, unused = calculateLegJointsInDeg(20, -1*a, 0)
    #     # print("LeftLower: ", leftLowerValue, "LeftUpper: ", leftUpperValue)
    #     setServo(LeftLower, leftLowerValue)
    #     setServo(LeftUpper, leftUpperValue)
    #     # print("LeftLower: ", leftLowerValue, "LeftUpper: ", leftUpperValue)
    #     setServo(RightLower, 180 - leftLowerValue)
    #     setServo(RightUpper, 180 - leftUpperValue)
    #     sleep(0.06)
    # print("down")
    # for a in range(max,min,-1):
    #     leftLowerValue, leftUpperValue, unused = calculateLegJointsInDeg(20, -1*a, 0)
    #     # print("LeftLower: ", leftLowerValue, "LeftUpper: ", leftUpperValue)
    #     setServo(LeftLower, leftLowerValue)
    #     setServo(LeftUpper, leftUpperValue)
    #     setServo(RightLower, 180 - leftLowerValue)
    #     setServo(RightUpper, 180 - leftUpperValue)
    #     sleep(0.06)
    # for a in range(90,120):
    #     leftLowerValue, leftUpperValue, unused = calculateLegJointsInDeg(0, -1*a, 0)
    #     setServo(RightLower, leftLowerValue)
    #     setServo(RightUpper, leftUpperValue)
    #     sleep(0.03)
    # for a in range(110,90,-1):
    #     leftLowerValue, leftUpperValue, unused = calculateLegJointsInDeg(0, -1*a, 0)
    #     setServo(RightLower, leftLowerValue)
    #     setServo(RightUpper, leftUpperValue)
    #     sleep(0.03)
    # leftLowerValue, leftUpperValue, unused = calculateLegJointsInDeg(0, -100, 0)
    # setServo(LeftLower, leftLowerValue)
    # setServo(LeftUpper, leftUpperValue)
    # setServo(RightLower, 180-leftLowerValue)
    # setServo(RightUpper, 180-leftUpperValue)
    # sleep(0.03)
    # servo1()
    # servo2()
    # servo3()
    # servo4()
