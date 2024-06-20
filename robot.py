from time import sleep
from numpy import interp
import math

import wheels
import legs
import mpu6050

K = 0.98
K1 = 1 - K

timeSlice = 0.02

def distance(a, b):
    return math.sqrt((a*a) + (b*b))

def y_rotation(x, y, z):
    radians = math.atan2(x, distance(y, z))
    return -math.degrees(radians)

def x_rotation(x, y, z):
    radians = math.atan2(y, distance(x, z))
    return math.degrees(radians)
    
def main():
    legs.changeHeight(110, 110)
    wheels.enable_motors()
    
    # accel_data = mpu6050.read_accel()
    # gyro_data = mpu6050.read_gyro()
        
    # aTempX = accel_data[0]
    # aTempY = accel_data[1]
    # aTempZ = accel_data[2]
    # gTempX = gyro_data[0]

    # last_x = x_rotation(aTempX, aTempY, aTempZ)

    # gyro_offset_x = gTempX
    try:
        while True:
            # accel_data = mpu6050.read_accel()
            # gyro_data = mpu6050.read_gyro()

            # accelX = accel_data[0]
            # accelY = accel_data[1]
            # accelZ = accel_data[2]

            # gyroX = gyro_data[0]
            # gyroX -= gyro_offset_x

            # gyro_x_delta = (gyroX * timeSlice)

            # rotation_x = x_rotation(accelX, accelY, accelZ)
            
            # #Complementary Filter
            # last_x = K * (last_x + gyro_x_delta) + (K1 * rotation_x)
            # print(f"X: {last_x}")
            # sleep(timeSlice)
            print(f"X: {mpu6050.getAngle()}")
            sleep(0.5)
            # interpXAccel = interp(last_x, [-5, 5], [-100, 100])
            # if interpXAccel < 0:
            #     wheels.move_stepper(timeSlice, abs(interpXAccel), "forward")
            # else:
            #     wheels.move_stepper(timeSlice, abs(interpXAccel), "backward")
            
    except KeyboardInterrupt:
        wheels.disable_motors()

if __name__ == "__main__":
    main()
