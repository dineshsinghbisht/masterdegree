import numpy as np

data = np.array([
    [10, 20, 30],
    [40, np.nan, 60],  # Row with NaN
    [70, 80, 90],
    [100, 110, np.nan] # Another row with NaN
])

# Create a boolean mask where True indicates a NaN value
nan_mask = np.isnan(data)

# Find rows with at least one NaN
rows_with_nan = nan_mask.any(axis=1)

# Invert the mask to select rows without NaN
filtered_mask = ~rows_with_nan

# Filter the array to keep only the desired rows
clean_data = data[filtered_mask]

print(f"Original array: {data}")
print(f"nan_mask is {nan_mask}")
print(f"rows_with_nan is {rows_with_nan}")
print(f"filtered_mask is {filtered_mask}")
print("\nArray with NaN rows removed:")
print(clean_data)


# import numpy as np

# data = np.array([
#     ['A', 'Pass', 95],
#     ['B', 'Fail', 78],  # Row to be removed
#     ['C', 'Pass', 85],
#     ['D', 'Fail', 60]   # Another row to be removed
# ])

# # Select the second column (index 1) for filtering
# status_column = data[:, 1]
# print(status_column)

# # Create a boolean mask to identify 'Fail' entries
# fail_mask = (status_column == 'Fail')
# print(f"fail_mask is {fail_mask}")

# # Invert the mask to select rows that are not 'Fail'
# filtered_mask = ~fail_mask

# # Filter the array to keep only the desired rows
# clean_data = data[filtered_mask]

# print("Original array:")
# print(data)
# print("\nArray with 'Fail' rows removed:")
# print(clean_data)