import numpy as np
import pandas as pd

class data_head():
    def objects(self, testdata):
        head = testdata.head(0)
        return head

class descriptive_statistics():

    # :data: is an object, which is fetched from GCP in the :app.py: module
    def dataset_describe(self, data):
        desc = data.describe()
        return desc
    
    # implementing descriptive statistics with numpy
    @staticmethod
    def average_and_median(self, data):
        
        # making objects to cover attributes to analyze
        temperature = data["temperature"]
        pressure = data["pressure"]
        humidity = data["humidity"]

        avg_temperature = np.average(temperature)
        avg_pressure = np.average(pressure)
        avg_humidity = np.average(humidity)
        med_temperature = np.median(temperature)
        med_pressure = np.median(pressure)
        med_humidity = np.median(humidity)

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
    def min_and_max(temperature, pressure, humidity):
        
        return


    @staticmethod
    def std_dev(temperature, pressure, humidity):
        std_temperature = np.std(temperature)
        std_pressure = np.std(pressure)
        std_humidity = np.std(humidity)
        return (std_temperature, std_pressure, std_humidity)

"""ds = descriptive_statistics()   
temperature_data = [25, 28, 27, 24, 26]
pressure_data = [1013, 1015, 1012, 1014, 1011]
humidity_data = [50, 55, 52, 49, 53]

# Call the descriptive_statistics method
result = ds.descriptive_statistics(temperature_data, pressure_data, humidity_data)

# Print the result
print(result)"""