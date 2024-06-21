import time
import math
import numpy

import wheels
import legs
import mpu6050

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def main():
    legs.changeHeight(110, 110)
    wheels.enable_motors()
    
    timeSlice = 0.01
    previousTime = time.time()
    gyroAngle = 0
    previousAngle = 0
    targetAngle = -3
    errorSum = 0
    
    Kp = 1
    Ki = 0
    Kd = 0
    gyroAngletotal = 0
    
    try:
        while True:
            # for a in range(0, 1000, 1):
            #     wheels.move_stepper(a/10)
            #     print(f"Motor Power: {a/10}")
            now = time.time()
            iterationTime = previousTime - now
            print(f"Iteration Time: {iterationTime}")
            previousTime = now
            
            gy = mpu6050.read_gyro_y()
            grate = numpy.interp(gy, [-32768, 32768], [-250, 250])
            
            gyroAngle = grate*iterationTime
            gyroAngletotal += gyroAngle
            
            currentAngle = 0.95 * (previousAngle + gyroAngle) + 0.05 * mpu6050.getAngle()
            # print(f"Current Angle: {currentAngle}")
            
            error = currentAngle - targetAngle
            errorSum = errorSum + error
            errorSum = constrain(errorSum, -300, 300)
            
            motorPower = Kp*(error) + Ki*(errorSum)*iterationTime - Kd*(currentAngle-previousTime)/iterationTime
            previousAngle = currentAngle
            
            # print(f"Current Angle: {currentAngle}")
            motorPower = constrain(motorPower, -100, 100)
            print(f"Motor Power: {motorPower}")
            
            wheels.move_stepper(motorPower)
            if currentAngle > 25 or currentAngle < -25:
                raise Exception("Robot has fallen over")
    except KeyboardInterrupt:
        wheels.disable_motors()

if __name__ == "__main__":
    main()