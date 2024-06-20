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
    
    timeSlice = 0.005
    previousTime = time.time()
    gyroAngle = 0
    previousAngle = 0
    targetAngle = -0.88
    errorSum = 0
    
    Kp = 1
    Ki = 0
    Kd = 0
    
    try:
        while True:
            now = time.time()
            iterationTime = previousTime - now
            previousTime = now
            
            gx = mpu6050.read_gyro_x()
            grate = numpy.interp(gx, [-32768, 32768], [-250, 250])
            
            gyroAngle = grate*iterationTime/1000
            currentAngle = 0.9934 * (previousAngle + gyroAngle) + 0.0066 * mpu6050.getAngle()
            
            currentAngle = currentAngle - 270
            
            error = currentAngle - targetAngle
            errorSum = errorSum + error
            errorSum = constrain(errorSum, -300, 300)
            
            motorPower = Kp*(error) + Ki*(errorSum)*iterationTime - Kd*(currentAngle-previousTime)/iterationTime
            previousTime = currentAngle
            
            # print(f"Current Angle: {currentAngle}, Motor Power: {motorPower}")
            print(f"acc angle: {mpu6050.getAngle()}")
            time.sleep(timeSlice)

    except KeyboardInterrupt:
        wheels.disable_motors()

if __name__ == "__main__":
    main()