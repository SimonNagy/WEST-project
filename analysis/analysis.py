import numpy as np
import pandas as pd

testdata = pd.read_csv("../test_data/data.csv")

class data_objects():
    def objects(testdata, id, timestamp, temperature, pressure, humidity):
        id = testdata[0]
        timestamp = testdata[1]
        temperature = testdata[2]
        pressure = testdata[3]
        humidity = testdata[4]


class descriptive_statistics():

    def __init__(self, id, timestamp, temperature, pressure, humidity):
        self.id = id
        self.timestamp = timestamp
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
    
    def descriptive_statistics(temperature, pressure, humidity):
        avg_temperature = np.average(temperature)
        avg_pressure = np.average(pressure)
        avg_humidity = np.average(humidity)