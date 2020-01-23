# general blink routine for neopixel
# should work on all boards with an "NEOPIXEL" pin defined in firmware
#
# M.Holliday

import time
import board
from pycubed import cubesat

delay = 1
while True:
    #if (not cubesat.hardware['IMU']):
    #    print("No IMU!")
    #    break
    #temp = cubesat.temperature
    temp = cubesat.temperature
    print(temp)
    time.sleep(delay)