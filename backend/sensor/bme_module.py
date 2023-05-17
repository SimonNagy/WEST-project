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

        # performing a sample reading
        sample_reading = bme280.sample(self.bus, sensor_module.ADDRESS)
        temperature_val = sample_reading.temperature
        humidity_val = sample_reading.humidity
        pressure_val = sample_reading.pressure

        # calculating the altitude
        altitude_val = 44330 * (1.0 - math.pow(pressure_val / sensor_module.SEA_LEVEL_PRESSURE_HPA, 0.1903))

        return (temperature_val, pressure_val, humidity_val, altitude_val)
    
    """
    The function read_sensor retrieves a tuple for the caller containing the declared
    attributes. 
    TODO: forward this reading to the app.py module to be stored in the cloud database
    TODO: fetch this data from the database to the app.py module, from there take it to 
    the analysis.py module (should need to use the preprocessor.py module as well)
    """