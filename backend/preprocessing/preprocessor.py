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

"""# Create an instance of the Attributes class
attr = Attributes()
# Call the attributes method with testdata and store the returned values
id, timestamp, temperature, pressure, humidity = attr.attributes(testdata)
# Print the values
print(id, timestamp, temperature, pressure, humidity)"""