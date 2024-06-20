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

ENABLE_L = True
ENABLE_R = True

# # Define the pins
R_EN_PIN = 18  # Enable pin
R_STEP_PIN = 23  # Step pin
R_DIR_PIN = 24  # Direction pin


# # Define the pins
L_EN_PIN = 17  # Enable pin
L_STEP_PIN = 27  # Step pin
L_DIR_PIN = 22  # Direction pin

# # Define the pins
# R_EN_PIN = 12  # Enable pin
# R_STEP_PIN = 16  # Step pin
# R_DIR_PIN = 18  # Direction pin


# # Define the pins
# L_EN_PIN = 11  # Enable pin
# L_STEP_PIN = 13  # Step pin
# L_DIR_PIN = 15  # Direction pin

GPIO.setmode(GPIO.BCM)

# Create DigitalOutputDevice instances for each pin
GPIO.setup(R_EN_PIN, GPIO.OUT)
GPIO.setup(R_STEP_PIN, GPIO.OUT)
GPIO.setup(R_DIR_PIN, GPIO.OUT)
GPIO.setup(L_EN_PIN, GPIO.OUT)
GPIO.setup(L_STEP_PIN, GPIO.OUT)
GPIO.setup(L_DIR_PIN, GPIO.OUT)

iterationTime = 0.1

# Function to move the stepper motor
def move_stepper(speed, direction):
    assert 0 <= speed <= 100, "Velocity must be between 0 and 100"
    
    if speed == 0:
        sleep(iterationTime)
        return
    
    speed = speed / 10
    
    totalSteps = speed / iterationTime
    sleepTime = (iterationTime / totalSteps) / 2
    
    print(f"Speed: {speed}, Total Steps: {totalSteps}, Sleep Time: {sleepTime}")
    
    # SET DIRECTION
    ENABLE_R and GPIO.output(R_DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
    ENABLE_L and GPIO.output(L_DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
    
    # Move the specified number of steps
    for _ in range(int(totalSteps)):
        ENABLE_R and GPIO.output(R_STEP_PIN, GPIO.HIGH)
        ENABLE_L and GPIO.output(L_STEP_PIN, GPIO.HIGH)
        sleep(sleepTime)  # Adjust this delay as needed
        ENABLE_R and GPIO.output(R_STEP_PIN, GPIO.LOW)
        ENABLE_L and GPIO.output(L_STEP_PIN, GPIO.LOW)
        sleep(sleepTime)  # Adjust this delay as needed
    
def enable_motors():
    ENABLE_R and GPIO.output(R_EN_PIN, GPIO.LOW)
    ENABLE_L and GPIO.output(L_EN_PIN, GPIO.LOW)

def disable_motors():
    ENABLE_R and GPIO.output(R_EN_PIN, GPIO.HIGH)
    ENABLE_L and GPIO.output(L_EN_PIN, GPIO.HIGH)