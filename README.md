# WEST: Weather station project using RaspberryPI and Bosch BME.280 sensor

In this project we are using a Raspberry PI 4 and BOSHCs' BME.280 sensor to build a weather station.

For the data processing and analysis we are using a plain python with numpy and pandas to write our own functions, then passing them to a module which utilizes matplotlib.pyplot for visualization.

The application, which displays the plots and the processed data is using a Flask backend API, and Streamlit as a fronend framework.