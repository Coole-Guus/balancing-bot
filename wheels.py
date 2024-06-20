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


# Define the pins
R_EN_PIN = 12  # Enable pin
R_STEP_PIN = 16  # Step pin
R_DIR_PIN = 18  # Direction pin


# Define the pins
L_EN_PIN = 11  # Enable pin
L_STEP_PIN = 13  # Step pin
L_DIR_PIN = 15  # Direction pin

GPIO.setmode(GPIO.BOARD)

# Create DigitalOutputDevice instances for each pin
GPIO.setup(R_EN_PIN, GPIO.OUT)
GPIO.setup(R_STEP_PIN, GPIO.OUT)
GPIO.setup(R_DIR_PIN, GPIO.OUT)
GPIO.setup(L_EN_PIN, GPIO.OUT)
GPIO.setup(L_STEP_PIN, GPIO.OUT)
GPIO.setup(L_DIR_PIN, GPIO.OUT)



# Function to move the stepper motor
def move_stepper(steps, direction):
    # print("Moving the stepper motor")
    
    # SET DIRECTION
    ENABLE_R and GPIO.output(R_DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
    ENABLE_L and GPIO.output(L_DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
    # ENABLE THE MOTOR
    ENABLE_R and GPIO.output(R_EN_PIN, GPIO.LOW)
    ENABLE_L and GPIO.output(L_EN_PIN, GPIO.LOW)
    
    # Move the specified number of steps
    for _ in range(steps):
        ENABLE_R and GPIO.output(R_STEP_PIN, GPIO.HIGH)
        ENABLE_L and GPIO.output(L_STEP_PIN, GPIO.HIGH)
        sleep(0.00005)  # Adjust this delay as needed
        ENABLE_R and GPIO.output(R_STEP_PIN, GPIO.LOW)
        ENABLE_L and GPIO.output(L_STEP_PIN, GPIO.LOW)
        sleep(0.00005)  # Adjust this delay as needed

    # # Disable the motor
    # sleep(7)
    # print("Disabling the motor")
    ENABLE_R and GPIO.output(R_EN_PIN, GPIO.HIGH)
    ENABLE_L and GPIO.output(L_EN_PIN, GPIO.HIGH)
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