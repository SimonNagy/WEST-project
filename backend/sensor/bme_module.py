import smbus2
import bme280
import time
import math

class sensor_module:
    SEA_LEVEL_PRESSURE_HPA = 1013.25 # declaring the sea level std pressure
    PORT = 1
    ADDRESS = 0x76

    def __init__(self):
        self.bus = smbus2.SMBus(sensor_module.PORT)
        self.calibration_params = bme280.load_calibration_params(self.bus, sensor_module.ADDRESS)
    
    def read_sensor(self):
        
        return