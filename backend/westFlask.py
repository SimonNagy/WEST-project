from flask import Flask

app = Flask(__name__)

@app.route('/plot')
def plot():
    return 

if __name__ == '__main__':
    app.run()