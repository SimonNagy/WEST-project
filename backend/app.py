import pandas as pd
from analysis import analysis as an
from preprocessing import preprocessor as prep

"""
Integration of the modules
-- the analysis module is imported
-- the preprocessor is imported, then data is transmitted to the analysis module
"""

testdata = pd.read_csv("test_data/data.csv", delimiter=';')

attr = prep.Attributes()
id, timestamp, temperature, pressure, humidity = attr.attributes(testdata)

ds = an.descriptive_statistics()
descriptive_statistics = ds.calculation(temperature, pressure, humidity)