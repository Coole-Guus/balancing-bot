from mpu6050 import mpu6050

mpu = mpu6050(0x68)

def read_sensor_data():
    accelerometer_data = mpu.get_accel_data()
    # gyroscope_data = mpu6050.get_gyro_data()
    # temperature = mpu6050.get_temp()
    return accelerometer_data['x']