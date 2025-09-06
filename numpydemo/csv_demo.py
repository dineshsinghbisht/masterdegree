import numpy as np

# File path
file_path = "sample_weather.csv"

# Read header separately
with open(file_path, 'r') as f:
    header = f.readline().strip().split(",")

# Read numeric/string data
data = np.genfromtxt(file_path, delimiter=",", skip_header=1, dtype=None, encoding="utf-8")

print("Header:", header)
print("Data:")
print(data)
