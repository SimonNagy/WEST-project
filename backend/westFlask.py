from flask import Flask, jsonify
from plot import descstatplot

app = Flask(__name__)

@app.route('/plot')
def plot():
    # generating the plot object from plot.descstatplot
    plot_obj = descstatplot()

    buffer = io.BytesIO()
    plot_obj.savefig(buffer, format='png')
    buffer.seek(0)

    # converting the buffer contents
    plot_data = base64.b64encoder(buffer.getvalue().decode('utf-8'))

    return jsonify({'plot_data': plot_data})

if __name__ == '__main__':
    app.run()