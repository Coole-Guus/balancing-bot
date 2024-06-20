from time import sleep
from numpy import interp
import math

import wheels
import legs
import mpu6050

def main():
    legs.changeHeight(110, 110)
    wheels.enable_motors()

    try:
        while True:
            print(f"X: {mpu6050.getAngle()}")
            sleep(0.5)

    except KeyboardInterrupt:
        wheels.disable_motors()

if __name__ == "__main__":
    main()
