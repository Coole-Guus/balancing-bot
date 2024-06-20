import adafruit_mpu6050
import board
import math

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

def read_accel():
    return mpu.acceleration

def read_gyro():
    return mpu.gyro

last_gyro_x = 0
last_gyro_y = 0
last_gyro_z = 0
accumulated_angle_x = 0
accumulated_angle_y = 0
accumulated_angle_z = 0

def correct_for_gravity(acc):
    """Corrects accelerometer data for gravity."""
    g = 9.81  # Acceleration due to gravity
    return acc / g

def getAngle():
    acc = mpu.acceleration
    return math.degrees(math.atan2(acc[0], acc[2]))