import numpy as np
import pandas as pd

class data_objects():
    def objects(testdata):
        head = testdata.head(0)
        return head

class descriptive_statistics():

    def data():
        data = pd.read_csv("./test_data/data.csv")
        return data

    def attributes(data):
        id = data["id"]
        timestamp = data["timestamp"]
        temperature = data["temperature"]
        pressure = data["pressure"]
        humidity = data["humidity"]
        return id, timestamp, temperature, pressure, humidity
    
    def dataset_describe(testdata):
        desc = testdata.describe()
        return desc
    
    # implementing descriptive statistics with numpy
    def descriptive_statistics(temperature, pressure, humidity):
        DS = {avg_temperature, avg_pressure, avg_humidity, med_temperature, med_pressure, med_humidity}
        avg_temperature = np.average(temperature)
        avg_pressure = np.average(pressure)
        avg_humidity = np.average(humidity)
        med_temperature = np.median(temperature)
        med_pressure = np.median(pressure)
        med_humidity = np.median(humidity)
        return DS
    
    print(DS)

