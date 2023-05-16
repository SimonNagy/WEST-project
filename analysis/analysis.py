import numpy as np
import pandas as pd

class data_objects():
    def objects(testdata):
        head = testdata.head(0)
        return head

class descriptive_statistics():

    def __init__(self, id, timestamp, temperature, pressure, humidity):
        self.id = id
        self.timestamp = timestamp
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
    
    # describe the test dataframe using the pandas built in libary
    def dataset_describe(testdata):
        desc = testdata.describe()
        return desc
    
    # implementing descriptive statistics with numpy
    def descriptive_statistics(temperature, pressure, humidity):
        avg_temperature = np.average(temperature)
        avg_pressure = np.average(pressure)
        avg_humidity = np.average(humidity)
        med_temperature = np.median(temperature)
        med_pressure = np.median(pressure)
        med_humidity = np.median(humidity)
        return avg_temperature, avg_pressure, avg_humidity, med_temperature, med_pressure, med_humidity

