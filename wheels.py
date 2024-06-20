import time
from TMC_2209.TMC_2209_StepperDriver import *
from TMC_2209._TMC_2209_GPIO_board import Board
    
# stepper left pinout:
# en = 11
# step = 13
# dir = 15

# stepper right pinout:
# en = 33
# step = 35
# dir = 37


from gpiozero import DigitalOutputDevice
from time import sleep

# Define the pins
EN_PIN = 33  # Enable pin
STEP_PIN = 35  # Step pin
DIR_PIN = 37  # Direction pin

# Create DigitalOutputDevice instances for each pin
en = DigitalOutputDevice(EN_PIN)
step = DigitalOutputDevice(STEP_PIN)
dir = DigitalOutputDevice(DIR_PIN)

# Function to move the stepper motor
def move_stepper(steps, direction):
    # Set direction
    dir.value = direction

    # Enable the motor
    en.off()

    # Move the specified number of steps
    for _ in range(steps):
        step.on()
        sleep(0.001)  # Adjust this delay as needed
        step.off()
        sleep(0.001)  # Adjust this delay as needed

    # Disable the motor
    en.on()

# Move the stepper motor
move_stepper(200, 1)  # Move 200 steps in one direction
sleep(10)  # Wait for a second
move_stepper(200, 0)  # Move 200 steps in the other direction