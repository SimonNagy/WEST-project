import numpy as np
import pandas as pd

class data_head():
    def objects(self, testdata):
        head = testdata.head(0)
        return head

class descriptive_statistics():

    def data(self):
        data = pd.read_csv("./test_data/data.csv")
        return data

    def attributes(self, data):
        id = data["id"]
        timestamp = data["timestamp"]
        temperature = data["temperature"]
        pressure = data["pressure"]
        humidity = data["humidity"]
        return id, timestamp, temperature, pressure, humidity
    
    def dataset_describe(self, testdata):
        desc = testdata.describe()
        return desc
    
    # implementing descriptive statistics with numpy
    @staticmethod
    def calculation(temperature, pressure, humidity):
        avg_temperature = np.average(temperature)
        avg_pressure = np.average(pressure)
        avg_humidity = np.average(humidity)
        med_temperature = np.median(temperature)
        med_pressure = np.median(pressure)
        med_humidity = np.median(humidity)
        ds = {"avg_temperature": avg_temperature, 
              "avg_pressure": avg_pressure,
               "avg_humidity": avg_humidity, 
               "med_temperature": med_temperature,
                "med_pressure": med_pressure, 
                "med_humidity": med_humidity
            }
        return ds

"""ds = descriptive_statistics()   
temperature_data = [25, 28, 27, 24, 26]
pressure_data = [1013, 1015, 1012, 1014, 1011]
humidity_data = [50, 55, 52, 49, 53]

# Call the descriptive_statistics method
result = ds.descriptive_statistics(temperature_data, pressure_data, humidity_data)

# Print the result
print(result)"""