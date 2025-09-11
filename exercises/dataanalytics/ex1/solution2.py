from datetime import datetime
from getpass import getuser
from operator import itemgetter
import csv


with open("prob2_ah4323.csv") as handle:
    mydata = list(csv.DictReader(handle))


#mydata = mydata[0:20] # To test with sample data


# Convert the TimeStamp to MM/dd/yyyy HH:mm:ss format
update_mydata = list(map(
    lambda data: {
        **data,
        "TimeStamp": datetime.strptime(data["TimeStamp"], "%Y-%m-%d %H:%M:%S.%f").strftime("%m/%d/%Y %H:%M:%S")
    },
    mydata
))
print(update_mydata)

# Sort the data with RotorSpeed_rpm
sort_mydata = sorted(update_mydata,key=itemgetter("RotorSpeed_rpm"))
print(sort_mydata)

def assign_group(data):
    try:
        ws = float(data["WindSpeed_mps"])
        if ws < 5:
            group = "A"
        elif ws <= 10:
            group = "B"
        else:
            group = "C"
    except ValueError:
        group = "NA"   # Handle empty or bad values

    return {**data, "WindSpeed_Group": group}


# add_mydata = list(map(assign_group, sort_mydata))
add_mydata = list(map(assign_group, update_mydata))


# # Add new column WindSpeed_Group
# add_mydata = list(map(
#     lambda data: {
#         **data,
#         "WindSpeed_Group": (
#             "A" if float(data["WindSpeed_mps"]) < 5
#             else "B" if float(data["WindSpeed_mps"]) <= 10
#             else "C"
#         )
#     },
#     sort_mydata
# ))

print(add_mydata) ## to verify the output from sample data

with open("prob2_ah4323_updated.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=add_mydata[0].keys())
    writer.writeheader()
    writer.writerows(add_mydata)