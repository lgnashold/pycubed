# Some miscallenous radio functions
# Docs: https://circuitpython.readthedocs.io/projects/rfm9x/en/latest/

# Written by Langston Nashold

import time
import digitalio

from pycubed import cubesat

if cubesat.hardware['Radio1']:
    # Update settings to improve "effective range"
    # Change number of hertz you're modulating between
    rfm9x.signal_bandwidth = 62500
    # This changes FEC. Between 5-8. Higher number is more tolerant.
    rfm9x.coding_rate = 8
    # Higher value allows distinguishes signal from noise
    # From 6 - 12
    rfm9x.spreading_factor = 8
    # Enables cyclic redudancy check, checking for errors
    rfm9x.enable_crc = True
    # Send something
    cubesat.radio1.send('hello!')
    print("sent hello")

    # Receive Something

