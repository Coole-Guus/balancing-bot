from time import sleep

import legs
import mpu6050

while True:
    # changeHeight(120, 70)
    legs.changeHeight(70, 120)
    # Read the sensor data
    
    accelerometer_x_data = mpu6050.read_sensor_data()
    # -10 max forward lean, 0 is straight, 10 is max backward lean
    # might have to calibrate pure up since body is slanted forward.
    # like minimize 
    print("Accelerometer data:", accelerometer_x_data)
    sleep(1)

    
