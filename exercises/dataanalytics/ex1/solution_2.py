from datetime import datetime
from getpass import getuser
from operator import itemgetter
import csv

# user = getuser()
# csv_location = f'/home/varpha/dan/private/{user}' + \
#                 f'/exrc_01/data/prob2_{user}.csv'

with open("prob2_ah4323.csv") as handle:
    mydata = list(csv.DictReader(handle))


mydata = mydata[0:20] # To test with sample data


# Convert the TimeStamp to MM/dd/yyyy HH:mm:ss format
update_mydata = list(map(
    lambda data: {
        **data,
        "TimeStamp": datetime.strptime(data["TimeStamp"], "%Y-%m-%d %H:%M:%S.%f").strftime("%m/%d/%Y %H:%M:%S")
    },
    mydata
))

## print(update_mydata) # To validate results with sample data

# Sort the data with RotorSpeed_rpm
sort_mydata = sorted(update_mydata,key=itemgetter("RotorSpeed_rpm"))
print(sort_mydata)

# Add new column WindSpeed_Group
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


add_mydata = list(map(assign_group, update_mydata))


## print(add_mydata) # To validate results with sample data

with open("prob2_ah4323_updated.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=add_mydata[0].keys())
    writer.writeheader()
    writer.writerows(add_mydata)                                