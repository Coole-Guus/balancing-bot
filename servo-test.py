# Set up libraries and overall settings
import RPi.GPIO as GPIO  # Imports the standard Raspberry Pi GPIO library
from time import sleep   # Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) # Sets the pin numbering system to use the physical layout

# Set up pin 12 for PWM
GPIO.setup(12, GPIO.OUT)  # Sets up pin 12 to an output (instead of an input)
a = GPIO.PWM(12, 50)     # Sets up pin 12 as a PWM pin

# GPIO.setup(32, GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
# b = GPIO.PWM(32, 50)     # Sets up pin 11 as a PWM pin

# GPIO.setup(33, GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
# c = GPIO.PWM(33, 50)     # Sets up pin 11 as a PWM pin

# GPIO.setup(35, GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
# d = GPIO.PWM(35, 50)     # Sets up pin 11 as a PWM pin

a.start(0)               # Starts running PWM on the pin and sets it to 0
# b.start(0)               # Starts running PWM on the pin and sets it to 0
# c.start(0)               # Starts running PWM on the pin and sets it to 0
# d.start(0)               # Starts running PWM on the pin and sets it to 0

try:
    while True:  # This will keep the servo sweep running until the process is interrupted
        # Move the servo back and forth
        a.ChangeDutyCycle(50)
        # b.ChangeDutyCycle(50)
        # c.ChangeDutyCycle(50)
        # d.ChangeDutyCycle(50)

        # p.ChangeDutyCycle(3)     # Changes the pulse width to 3 (so moves the servo)
        # sleep(1)                 # Wait 1 second
        # p.ChangeDutyCycle(12)    # Changes the pulse width to 12 (so moves the servo)
        # sleep(1)
except KeyboardInterrupt:  # This will catch the interrupt and move to the cleanup code
    pass

finally:
    # Clean up everything
    a.stop()                 # At the end of the program, stop the PWM
    # b.stop()
    # c.stop()
    # d.stop()
    GPIO.cleanup()           # Resets the GPIO pins back to defaults