from time import sleep
from numpy import interp

import wheels
import legs
import mpu6050

def setup():
    legs.changeHeight(110, 110)
    wheels.enable_motors()

def loop():
    mpu6050.read_x_accel()
    sleep(1)
    # accelerometer_x_data = mpu6050.read_sensor_data()
    # for a in range(0, 100, 1):
    #     wheels.move_stepper(a, 1)

def main():
    setup()
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        wheels.disable_motors()

if __name__ == "__main__":
    main()
