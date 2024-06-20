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
    # Read gyroscope data
    gyro = mpu.gyro
    
    # Integrate gyroscope data to get angular displacement
    accumulated_angle_x += gyro['x']
    accumulated_angle_y += gyro['y']
    accumulated_angle_z += gyro['z']
    
    # Correct for drift using accelerometer data
    acc = mpu.acceleration
    corrected_acc_x = correct_for_gravity(acc['x'])
    corrected_acc_y = correct_for_gravity(acc['y'])
    corrected_acc_z = correct_for_gravity(acc['z'])
    
    # Calculate gravity vector
    gravity_vector = [corrected_acc_x, corrected_acc_y, corrected_acc_z]
    
    # Subtract gravity vector from integrated gyroscope data
    corrected_angle_x = accumulated_angle_x - gravity_vector[0]
    corrected_angle_y = accumulated_angle_y - gravity_vector[1]
    corrected_angle_z = accumulated_angle_z - gravity_vector[2]
    
    # Print corrected angles in degrees
    print(f"Corrected Angles: X={corrected_angle_x}, Y={corrected_angle_y}, Z={corrected_angle_z} degrees")
    