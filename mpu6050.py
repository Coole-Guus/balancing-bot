import adafruit_mpu6050
import board
import math

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

def read_accel():
    return mpu.acceleration

def read_gyro():
    return mpu.gyro

def getAngle():
    acceleration = mpu.acceleration
    accel_x, accel_y, accel_z = acceleration
    tilt_angle_x = math.atan2(accel_y, math.sqrt(accel_x**2 + accel_z**2))
    tilt_angle_x = math.degrees(tilt_angle_x)
    return tilt_angle_x