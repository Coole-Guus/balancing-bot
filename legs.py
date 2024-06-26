
from adafruit_servokit import ServoKit
import math

kit = ServoKit(channels=16)

MiddleLower = 7
MiddleUpper = 6
LeftLower = 11
LeftUpper = 10
RightLower = 14
RightUpper = 15

# resolution of the milimeters the servo travels, the higher the more steps in positions.
# comes at a cost of speed.
precision = 8

# starting point for this function retrieved from previous personal project of Guus Kleinlein
# repo: https://github.com/klaasnicolaas/Spot-Redux
def CalculateAngles(x, y, z):
    lowerLeg = 100
    upperLeg = 100
    
    #Put leg offset logic here
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

    lowerLegAngle = math.acos((x*x + s*s - lowerLeg*lowerLeg - upperLeg*upperLeg)/(2*lowerLeg*upperLeg))
    upperLegAngle = math.atan(s/x)-math.atan((upperLeg*math.sin(lowerLegAngle))/(lowerLeg+upperLeg*math.cos(lowerLegAngle)))
    
    #Radians to degrees + fysical offsets.
    upperLegAngle = 225 + ((upperLegAngle*180)/math.pi)
    lowerLegAngle = 180 - ((lowerLegAngle*180)/math.pi)
    shoulderLegAngle = 180 + ((shoulderLegAngle*180)/math.pi)

    #Calculates angle difference due to upper leg state.
    diffUpperLeg = upperLegAngle - 90
    lowerLegAngle = lowerLegAngle - diffUpperLeg 

    #Invert upperLegAngle due to inverted motor rotation.
    upperLegAngle = 180 - upperLegAngle

    if(upperLegAngle <= 0):
        upperLegAngle = 180 + upperLegAngle
    if(lowerLegAngle <= 0):
        lowerLegAngle = 180 + lowerLegAngle

    return lowerLegAngle, upperLegAngle, shoulderLegAngle
        
def setServo(servo: int, angle: float):
    kit.servo[servo].angle = angle

def changeHeight(newVal: float, oldVal: float):
    if newVal - oldVal > 0:
        for a in range(oldVal*precision, newVal*precision, 1):
            b = a/precision
            leftLowerValue, leftUpperValue, unused = CalculateAngles(0, -1*b, 0)
            setServo(LeftLower, leftLowerValue)
            setServo(LeftUpper, leftUpperValue)
            setServo(RightLower, 180 - leftLowerValue)
            setServo(RightUpper, 180 - leftUpperValue)
            middleLowerValue, middleUpperValue, unused = CalculateAngles(0, -1*b - 30, 0)
            setServo(MiddleLower, 180 - middleLowerValue)
            setServo(MiddleUpper, 180 - middleUpperValue)
            # sleep(timeQuantum/precision)
    elif newVal - oldVal == 0:
        leftLowerValue, leftUpperValue, unused = CalculateAngles(0, -1*newVal, 0)
        setServo(LeftLower, leftLowerValue)
        setServo(LeftUpper, leftUpperValue)
        setServo(RightLower, 180 - leftLowerValue)
        setServo(RightUpper, 180 - leftUpperValue)
        middleLowerValue, middleUpperValue, unused = CalculateAngles(0, -1*newVal - 10, 0)
        setServo(MiddleLower, 180 - middleLowerValue)
        setServo(MiddleUpper, 180 - middleUpperValue)
        # sleep(timeQuantum/precision)
    else:
        for a in range(oldVal*precision, newVal*precision, -1):
            b = a/precision
            leftLowerValue, leftUpperValue, unused = CalculateAngles(0, -1*b, 0)
            setServo(LeftLower, leftLowerValue)
            setServo(LeftUpper, leftUpperValue)
            setServo(RightLower, 180 - leftLowerValue)
            setServo(RightUpper, 180 - leftUpperValue)
            middleLowerValue, middleUpperValue, unused = CalculateAngles(0, -1*b - 30, 0)
            setServo(MiddleLower, 180 - middleLowerValue)
            setServo(MiddleUpper, 180 - middleUpperValue)
            # sleep(timeQuantum/precision)