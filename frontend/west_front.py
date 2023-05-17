import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

# fetching the plot endpoint from the backend
response = requests.get('http://localhost:5000/plot')
data = response.json()

# converting the base64 encoded object into an image
descstatplot_data = base64.b64decode(data['plot_data'])
descstatplot = Image.open(BytesIO(descstatplot_data))

st.image(descstatplot)