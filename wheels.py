import RPi.GPIO as GPIO
from time import sleep

# stepper left pinout:
# en = 11
# step = 13
# dir = 15

# stepper right pinout:
# en = 12
# step = 16
# dir = 18


# Define the pins
EN_PIN = 12  # Enable pin
STEP_PIN = 16  # Step pin
DIR_PIN = 18  # Direction pin


# Define the pins
# EN_PIN = 11  # Enable pin
# STEP_PIN = 13  # Step pin
# DIR_PIN = 15  # Direction pin

GPIO.setmode(GPIO.BOARD)

# Create DigitalOutputDevice instances for each pin
GPIO.setup(EN_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Function to move the stepper motor
def move_stepper(steps, direction):
    # print("Moving the stepper motor")
    
    # SET DIRECTION
    GPIO.output(DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
    # ENABLE THE MOTOR
    GPIO.output(EN_PIN, GPIO.LOW)
    
    # Move the specified number of steps
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        sleep(0.001)  # Adjust this delay as needed
        GPIO.output(STEP_PIN, GPIO.LOW)
        sleep(0.001)  # Adjust this delay as needed

    # # Disable the motor
    # sleep(7)
    # print("Disabling the motor")
    GPIO.output(EN_PIN, GPIO.HIGH)
    # sleep(7)


while True:
    move_stepper(2000, 0)  # Move 200 steps in one direction
    # print("enabling the motor")
    # en.off()
    # sleep(7)
    # print("Disabling the motor")
    # en.on()
    # sleep(7)
# Move the stepper motor
# move_stepper(200, 1)  # Move 200 steps in one direction
# sleep(1)  # Wait for a second
# move_stepper(200, 0)  # Move 200 steps in the other direction