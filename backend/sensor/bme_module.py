import smbus2
import bme280
import time
import math

class sensor_module:
    SEA_LEVEL_PRESSURE_HPA = 1013.25 # declaring the sea level std pressure
    PORT = 1
    ADDRESS = 0x76

    def __init__(self):
        return
    
    def read_sensor(self)
        return