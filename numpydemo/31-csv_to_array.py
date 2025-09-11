import datetime
import numpy as np
import csv

# Read entire CSV as strings to create a 2d array
data = np.genfromtxt("details.csv", delimiter=",", dtype=str)
print(data)
print(type(data))
np.savetxt("output_data.csv", data, delimiter=",", fmt="%s") ## For debugging to see the output