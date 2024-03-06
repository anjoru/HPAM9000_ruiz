import pandas as pd

# Define the path to your file
data_path = '/Users/andrewruiz/PycharmProjects/HPAM9000_ruiz/Python/West_Nile_Virus__WNV__Mosquito_Test_Results.xlsx'

# Read the data
data = pd.read_excel(data_path)

# Print the first few rows of the DataFrame
print(data.head())

# Get a summary of the data including the non-null count and data type of each column
print(data.info())

# Get descriptive statistics for numerical columns
print(data.describe())

# Count unique values in the 'Species' column
print(data['Species'].value_counts())

