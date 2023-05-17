import pandas as pd
from analysis import analysis as an
from preprocessing import preprocessor as prep
import schedule
import time
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
Implementing the GCP Firestore communication channel, and the data upload / download mechanism. 
Steps of development:
1. initializing the GCP connection, credentials, and the client
2. declaration of the fetch_sensor_readings function, from firestore
3. scheduling the function to run every n minutes
4. declaration of the upload_sensor_readings function, based on an instance of the sensor module
"""

cred = credentials.Certificate('TODO: path to service account')
firebase_admin.initialize_app(cred)
db = firestore.client()

# creating an instance of the sensor module 
sensor = bme_module.sensor_module()

def fetch_sensor_reading():

    #fetch all documents from sensor_data collection on firestore
    collection_ref = db.collection('sensor_data')
    docs = collection_ref.get()

    # empty list for the sensor data
    sensor_data = []

    for doc in docs:
        data = doc.to_dict()
        sensor_data.append(data)

def upload_sensor_readings():

    # reading sensor data using the sensor module
    temperature, pressure, humidity, altitude = sensor.read_sensor()

    timestamp = datetime.now()

    # creating a data dictionary with the sensor readings
    data = {
        'temperature': temperature,
        'pressure': pressure,
        'humidity': humidity,
        'altitude': altitude,
        'timestamp': timestamp
    }

    # uploading the data to firestore
    doc_ref = db.collection('sensor_data').document() # <= sensor_data collection needs to be named in firestore
    doc_ref.set(data)

schedule.every(1).minutes.do(upload_sensor_readings)

# run the scheduled job constantly
while True:
    schedule.run_pending()
    time.sleep(1)

