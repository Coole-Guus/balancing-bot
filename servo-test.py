# Set up libraries and overall settings
from gpiozero import Servo
from time import sleep   # Imports sleep (aka wait or pause) into the program
from signal import pause

# Set up pins for Servos
servo_a = Servo(18)  # BCM equivalent of physical pin 12
servo_b = Servo(12)  # BCM equivalent of physical pin 32
servo_c = Servo(13)  # BCM equivalent of physical pin 33
servo_d = Servo(19)  # BCM equivalent of physical pin 35

try:
    while True:  # This will keep the servo sweep running until the process is interrupted
        # Move the servos back and forth
        for servo in [servo_a, servo_b]:
            servo.value = 0.4    # Move the servo to its maximum position
        for servo in [servo_c, servo_d]:
            servo.value = 0.2    # Move the servo to its minimum position
        sleep(1)
        for servo in [servo_a, servo_b]:
            servo.mid()    # Move the servo to its middle position
        for servo in [servo_c, servo_d]:
            servo.value = 0.4    # Move the servo to a different position
        sleep(1)
except KeyboardInterrupt:  # This will catch the interrupt and move to the cleanup code
    pass

finally:
    # Disable all servos
    for servo in [servo_a, servo_b, servo_c, servo_d]:
        servo.detach()

pause()  # Wait for an interrupt signal (like Ctrl+C)