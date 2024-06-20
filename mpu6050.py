import adafruit_mpu6050
import board

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

def read_sensor_data():
    # accelerometer_data = mpu.acceleration
    # gyroscope_data = mpu6050.get_gyro_data()
    # temperature = mpu6050.get_temp()
    # return accelerometer_data['x']
    return mpu.acceleration