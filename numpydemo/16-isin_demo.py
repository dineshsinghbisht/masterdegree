import numpy as np

# A list of survey responses, some of which are invalid
survey_responses = np.array(['4', '5', 'N/A', '3', '1', 'missing', '2', '-', np.nan, 'Nan'])

# Define the set of invalid entries you want to filter out
invalid_entries = np.array(['N/A', 'missing', '-', np.nan])

# Use isin() with invert=True to find the valid responses
valid_mask = np.isin(survey_responses, invalid_entries, invert=True)
print(valid_mask)

# Use the boolean mask to filter the original array
valid_responses = survey_responses[valid_mask]

print("Original responses:", survey_responses)
print("Invalid entries to filter:", invalid_entries)
print("Valid responses (filtered):", valid_responses)