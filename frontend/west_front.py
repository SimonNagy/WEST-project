import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

# setting up page title and formatting config
st.set_page_config(page_title="WEST: Weather Station with RaspberryPI", page_icon=':sunny:')
st.title("WEST: Weather Station with RaspberryPI")

# adding the sidebar menu
menu_options = ["Home", "Descriptive Statistics"]
selected_option = st.sidebar.selectbox('Menu', menu_options)

if selected_option == "Home":
    # displaying a welcome screen on home
    st.write("Welcome to the WEST project: Weather Station with RaspberryPI and Bosch BME.280 sensor!")
elif selected_option == "Descriptive Statistics":
    # fetching the plot endpoint from the backend
    response = requests.get('http://localhost:5000/plot')
    data = response.json()

    # converting the base64 encoded object into an image
    descstatplot_data = base64.b64decode(data['plot_data'])
    descstatplot = Image.open(BytesIO(descstatplot_data))

    st.subheader('Average and Median values')
    st.image(descstatplot)