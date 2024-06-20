import adafruit_mpu6050
import board

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

def read_x_accel():
    # accelerometer_data = mpu.acceleration
    # gyroscope_data = mpu6050.get_gyro_data()
    # temperature = mpu6050.get_temp()
    # return accelerometer_data['x']
    print(mpu.acceleration[0])
    return mpu.acceleration[0]