import RPi.GPIO as GPIO
from time import sleep

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

GPIO.setmode(GPIO.BCM)

# Create DigitalOutputDevice instances for each pin
GPIO.setup(R_EN_PIN, GPIO.OUT)
GPIO.setup(R_STEP_PIN, GPIO.OUT)
GPIO.setup(R_DIR_PIN, GPIO.OUT)
GPIO.setup(L_EN_PIN, GPIO.OUT)
GPIO.setup(L_STEP_PIN, GPIO.OUT)
GPIO.setup(L_DIR_PIN, GPIO.OUT)

iterationTime = 0.01
 
def move_stepper(speed):
    assert -100 <= speed <= 100, "Velocity must be between 0 and 100"
    direction = "forward" if speed > 0 else "backward"
    speed = abs(speed)
    
    if speed == 0:
        sleep(iterationTime)
        return
    
    # Calculate the number of steps needed to move the specified distance and sleep time for those steps
    speed = speed / 75
    totalSteps = speed / iterationTime
    sleepTime = (iterationTime / totalSteps) / 2
    sleepTime = round(sleepTime, 5)
    
    # SET DIRECTION
    ENABLE_R and GPIO.output(R_DIR_PIN, GPIO.HIGH if direction == "forward" else GPIO.LOW)
    ENABLE_L and GPIO.output(L_DIR_PIN, GPIO.LOW if direction == "forward" else GPIO.HIGH)
    
    # Move the specified number of steps
    for _ in range(int(totalSteps)):
        ENABLE_R and GPIO.output(R_STEP_PIN, GPIO.HIGH)
        ENABLE_L and GPIO.output(L_STEP_PIN, GPIO.HIGH)
        sleep(sleepTime)
        ENABLE_R and GPIO.output(R_STEP_PIN, GPIO.LOW)
        ENABLE_L and GPIO.output(L_STEP_PIN, GPIO.LOW)
        sleep(sleepTime)
    
def enable_motors():
    ENABLE_R and GPIO.output(R_EN_PIN, GPIO.LOW)
    ENABLE_L and GPIO.output(L_EN_PIN, GPIO.LOW)

def disable_motors():
    ENABLE_R and GPIO.output(R_EN_PIN, GPIO.HIGH)
    ENABLE_L and GPIO.output(L_EN_PIN, GPIO.HIGH)