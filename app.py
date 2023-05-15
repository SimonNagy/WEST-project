from data_import import import_test as it
from dashboard import display_test as dt
from analysis import analysis as an

# integration of the import module to the app module
data_test = it.data
print(data_test)

# integration of the dashboard module to the app module
sample_dataframe = dt.df
print(sample_dataframe)

# integration of the analysis module to the app module
descstat = an.descriptive_statistics
print(descstat.dataset_describe)