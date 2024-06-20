import time
from TMC_2209.TMC_2209_StepperDriver import *
from TMC_2209._TMC_2209_GPIO_board import Board
    
# stepper left pinout:
# en = 11
# step = 13
# dir = 15

# stepper right pinout:
# en = 12
# step = 16
# dir = 18

from gpiozero import DigitalOutputDevice
from time import sleep

# Define the pins
EN_PIN = 12  # Enable pin
STEP_PIN = 16  # Step pin
DIR_PIN = 18  # Direction pin

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
sleep(1)  # Wait for a second
move_stepper(200, 0)  # Move 200 steps in the other direction