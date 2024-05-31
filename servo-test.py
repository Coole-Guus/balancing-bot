# Set up libraries and overall settings
import pigpio
from time import sleep   # Imports sleep (aka wait or pause) into the program

# Set up pins for Servos
servo_a = 18  # BCM equivalent of physical pin 12
servo_b = 12  # BCM equivalent of physical pin 32
servo_c = 13  # BCM equivalent of physical pin 33
servo_d = 19  # BCM equivalent of physical pin 35

# Create a pigpio object
pi = pigpio.pi()

try:
    while True:  # This will keep the servo sweep running until the process is interrupted
        # Move the servos back and forth
        pi.set_servo_pulsewidth(servo_a, 1000)  # Move the servo to its minimum position
        pi.set_servo_pulsewidth(servo_b, 2000)  # Move the servo to its maximum position
        pi.set_servo_pulsewidth(servo_c, 1000)  # Move the servo to its minimum position
        pi.set_servo_pulsewidth(servo_d, 2000)  # Move the servo to its maximum position
        sleep(1)
        pi.set_servo_pulsewidth(servo_a, 1500)  # Move the servo to its middle position
        pi.set_servo_pulsewidth(servo_b, 1500)  # Move the servo to its middle position
        pi.set_servo_pulsewidth(servo_c, 1500)  # Move the servo to its middle position
        pi.set_servo_pulsewidth(servo_d, 1500)  # Move the servo to its middle position
        sleep(1)
        
except KeyboardInterrupt:  # This will catch the interrupt and move to the cleanup code
    pass

finally:
    # Disable all servos
    pi.set_servo_pulsewidth(servo_a, 0)
    pi.set_servo_pulsewidth(servo_b, 0)
    pi.set_servo_pulsewidth(servo_c, 0)
    pi.set_servo_pulsewidth(servo_d, 0)
    pi.stop()