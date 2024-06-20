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

tmc = TMC_2209(11, 13, 15, serialport="/dev/ttyAMA0")
tmc.set_movement_abs_rel(MovementAbsRel.RELATIVE)

tmc.set_direction_reg(False)
tmc.set_current(300)
tmc.set_interpolation(True)
tmc.set_spreadcycle(False)
tmc.set_microstepping_resolution(2)
tmc.set_internal_rsense(False)

tmc.test_dir_step_en()

tmc.set_motor_enabled(False)

