import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app

def descstatplot():
    data = app.descriptive_statistics

    parameters = ['Temperature', 'Pressure', 'Humidity']
    avg_values = [data['avg_temperature'], data['avg_pressure'], data['avg_humidity']]
    med_values = [data['med_temperature'], data['med_pressure'], data['med_humidity']]

    x = range(len(parameters))
    plt.bar(x, avg_values, width=.4, align='center', color='blue', label='Average')
    plt.bar(x, med_values, width=.4, align='center', color='red', label='Median')

    plt.xticks(x, parameters)
    plt.xlabel('Parameters')
    plt.ylabel('Values')
    plt.title('Average and Median Values')
    plt.legend()

    return plt