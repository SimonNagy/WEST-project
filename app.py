
from dashboard import display_test as dt
from analysis import analysis as an



# integration of the dashboard module to the app module
sample_dataframe = dt.df
print(sample_dataframe)

# integration of the analysis module to the app module
descstat = an.descriptive_statistics
print(descstat.dataset_describe)