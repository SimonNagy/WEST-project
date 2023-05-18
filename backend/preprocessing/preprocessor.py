import pandas as pd
import numpy as np

testdata = pd.read_csv("test_data/data.csv", delimiter=";")

class Attributes():
    def attributes(self, testdata):
        id = testdata["id"]
        timestamp = testdata["timestamp"]
        temperature = testdata["temperature"]
        pressure = testdata["pressure"]
        humidity = testdata["humidity"]
        return id, timestamp, temperature, pressure, humidity

"""
TODO: This module has not yet been implemented to work with the sensor data. We need to make sure, the GCP data is formatted into a pandas dataframe, which can be further processed in the :analysis.py: module.
"""