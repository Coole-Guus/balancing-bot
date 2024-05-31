# Set up libraries and overall settings
from gpiozero import Servo
from time import sleep   # Imports sleep (aka wait or pause) into the program
from signal import pause

# Set up pin 12 for Servo
servo = Servo(12)

try:
    while True:  # This will keep the servo sweep running until the process is interrupted
        # Move the servo back and forth
        servo.min()    # Move the servo to its minimum position
        sleep(1)       # Wait 1 second
        servo.max()    # Move the servo to its maximum position
        sleep(1)
except KeyboardInterrupt:  # This will catch the interrupt and move to the cleanup code
    pass

pause()  # Wait for an interrupt signal (like Ctrl+C)