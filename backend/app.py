import pandas as pd
from analysis import analysis as an
from preprocessing import preprocessor as prep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from sensor import bme_module

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

"""
Implementing the GCP Firestore communication channel, and the data upload mechanism. Steps 
of development:
1. initializing the GCP connection, credentials, and the client
2. declaration of the upload_sensor_readings function
"""

cred = credentials.Certificate('TODO: path to service account')
firebase_admin.initialize_app(cred)
db = firestore.client()

def upload_sensor_readings():
    # creating an instance of the sensor module