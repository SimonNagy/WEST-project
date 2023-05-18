import numpy as np
import pandas as pd

class data_head():
    def objects(self, testdata):
        head = testdata.head(0)
        return head

"""
TODO: make :data: to be a pandas dataframe, from which we can read attributes in the class constructor
"""


class descriptive_statistics():

    # making the class constructor to contain the three attributes
    def __init__(self, data):
        self.temperature = data["temperature"]
        self.pressure = data["pressure"]
        self.humidity = data["humidity"]

    # :data: is an object, which is fetched from GCP in the :app.py: module
    def dataset_describe(self, data):
        desc = data.describe()
        return desc
    
    @staticmethod
    def average_and_median(self):
        
        avg_temperature = np.average(self.temperature)
        avg_pressure = np.average(self.pressure)
        avg_humidity = np.average(self.humidity)
        med_temperature = np.median(self.temperature)
        med_pressure = np.median(self.pressure)
        med_humidity = np.median(self.humidity)

        # returning results named :avg_and_med:
        avg_and_med = {
            "avg_temperature": avg_temperature,
            "avg_pressure": avg_pressure,
            "avg_humidity": avg_humidity,
            "med_temperature": med_temperature,
            "med_pressure": med_pressure,
            "med_humidity": med_humidity
        }
        
        return avg_and_med
    
    @staticmethod
    def min_and_max(self):

        min_temperature = np.min(self.temperature)
        max_temperature = np.max(self.temperature)
        min_pressure = np.min(self.pressure)
        max_pressure = np.max(self.pressure)
        min_humidity = np.min(self.humidity)
        max_humidity = np.max(self.humidity)

        min_and_max = {
            "min_temperature": min_temperature,
            "max_temperature": max_temperature,
            "min_pressure": min_pressure,
            "max_pressure": max_pressure,
            "min_humidity": min_humidity,
            "max_humidity": max_humidity
        }

        return min_and_max


    @staticmethod
    def std_dev(self):

        std_temperature = np.std(self.temperature)
        std_pressure = np.std(self.pressure)
        std_humidity = np.std(self.humidity)

        std_dev = {
            "std_dev_temperature": std_temperature,
            "std_dev_pressure": std_pressure,
            "std_dev_humidity": std_humidity
        }

        return std_dev

"""ds = descriptive_statistics()   
temperature_data = [25, 28, 27, 24, 26]
pressure_data = [1013, 1015, 1012, 1014, 1011]
humidity_data = [50, 55, 52, 49, 53]

# Call the descriptive_statistics method
result = ds.descriptive_statistics(temperature_data, pressure_data, humidity_data)

# Print the result
print(result)"""