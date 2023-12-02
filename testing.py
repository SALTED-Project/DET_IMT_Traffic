import pandas as pd
import numpy as np

# Specify the path to the CSV file
csv_file_path = '/home/dice/Mohsan_Simulatiom_directory_C2JN_project/SALTED_IOT_DATA/Traffic  data to convert to NGSI LD Model/2019/04-2019.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path, delimiter=';', na_values=['"NaN"'], quoting=3)

# Display the DataFrame
print("Original DataFrame:")
#print(df)


print ("\n\ndf.columns", df.columns)

# Count NaN values in each series
nan_counts = df.isna().sum()

# Display the number of NaN values in each series
print("\nNumber of NaN values in each series:")
print(nan_counts)

df.replace("NaN", np.nan, inplace=True)
df = df.infer_objects()
# Interpolate NaN values
df.interpolate(inplace=True)

# Print the series with np.nan values
print("\nSeries with np.nan values:")
n = df.isna().sum()
print(n )



df = pd.read_excel("/home/dice/Mohsan_Simulatiom_directory_C2JN_project/SALTED_IOT_DATA/Traffic  data to convert to NGSI LD Model/SENSOR_DATA/pmed_ubicacion_06-2023.xlsx")

# Iterate over columns and calculate the total length of each series
series_lengths = {}
for column in df.columns:
    series_lengths[column] = len(df[column])

# Print the total length of each series
for series, length in series_lengths.items():
    print(f"Series '{series}' has a total length of {length}.")

# If you want to get the sum of lengths across all series, you can do the following:
total_length = sum(series_lengths.values())
print(f"\nTotal length of all series: {total_length}")
