# Set up libraries and overall settings
from gpiozero import Servo
from time import sleep   # Imports sleep (aka wait or pause) into the program
from signal import pause

# Set up pins for Servos
# servo_a = Servo(18)  # BCM equivalent of physical pin 12
servo_b = Servo(12)  # BCM equivalent of physical pin 32
# servo_c = Servo(13)  # BCM equivalent of physical pin 33
# servo_d = Servo(19)  # BCM equivalent of physical pin 35

try:
    while True:  # This will keep the servo sweep running until the process is interrupted
        # Move the servos back and forth
        # servo_a.value = 0.2
        servo_b.value = 0.12
        # servo_c.value = 0.2
        # servo_d.value = 0.2
        sleep(1)
        # servo_a.value = 0.0
        servo_b.value = 0.0
        # servo_c.value = 0.4
        # servo_d.value = 0.4
        sleep(1)
        
except KeyboardInterrupt:  # This will catch the interrupt and move to the cleanup code
    pass

finally:
    # Disable all servos
    # for servo in [servo_a, servo_b, servo_c, servo_d]:
    #     servo.detach()
    # servo_a.detach()
    servo_b.detach()

pause()  # Wait for an interrupt signal (like Ctrl+C)