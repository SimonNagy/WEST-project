import pandas as pd 
from dashboard import display_test as dt
from analysis import analysis as an



# integration of the dashboard module to the app module
"""sample_dataframe = dt.df
print(sample_dataframe)"""

# integration of the analysis module to the app module
testdata = pd.read_csv("./test_data/data.csv")

print(an.descriptive_statistics.dataset_describe(testdata))
print(an.data_objects.objects(testdata))
print(an.descriptive_statistics.descriptive_statistics(testdata))