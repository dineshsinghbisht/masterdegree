import numpy as np

file_path = "sample_weather.csv"

# Read entire CSV as strings
data = np.genfromtxt(file_path, delimiter=",", dtype=str)

print("Full Data (including header):")
print("-----")
print(data.ndim)
print(data.shape)
print("-----")
print(type(data))

# Access header
header = data[0]
print("Header:", header)

# Access data rows (without header)
rows = data[1:]
print("First row:", rows[0])
