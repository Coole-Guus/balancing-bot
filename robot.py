import time
import math
import numpy

import wheels
import legs
import mpu6050

timeSlice = 0.05
previousTime = time.time()
gyroAngle = 0
previousAngle = 0

def main():
    legs.changeHeight(110, 110)
    wheels.enable_motors()

    try:
        while True:
            now = time.time()
            iterationTime = previousTime - now
            previousTime = now
            
            gx = mpu6050.read_gyro_x()
            grate = numpy.interp(gx, [-32768, 32768], [-250, 250])
            gyroAngle = gyroAngle + grate*iterationTime/1000

            currentAngle = 0.9934 * (previousAngle + gyroAngle) + 0.0066 * mpu6050.getAngle()
            previousAngle = currentAngle
            print(f"X: {currentAngle}")
            time.sleep(timeSlice)

    except KeyboardInterrupt:
        wheels.disable_motors()

if __name__ == "__main__":
    main()
