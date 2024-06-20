import adafruit_mpu6050
import board
import math

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

def read_accel():
    return mpu.acceleration

def read_gyro_x():
    return mpu.gyro[0]

def getAngle():
    acc = mpu.acceleration
    return math.degrees(math.atan2(acc[1], acc[2]))