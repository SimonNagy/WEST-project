import io
import base64
import matplotlib.pyplot as plt
from flask import Flask, jsonify
from flask_cors import CORS
from plot import descstatplot
from app import fetch_sensor_reading

app = Flask(__name__)
CORS(app)

@app.route('/plot')
def plot():
    # generating the plot object from plot.descstatplot
    plot_obj = descstatplot()

    buffer = io.BytesIO()
    plot_obj.savefig(buffer, format='png')
    buffer.seek(0)

    # converting the buffer contents
    plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close(plot_data)

    return jsonify({'plot_data': plot_data})

if __name__ == '__main__':
    app.run()

@app.route('fetch')
def fetch_data_endpoint():
    fetch_sensor_reading()