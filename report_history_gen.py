# PRIVATE AND CONFIDENTIAL [Intellectual Property Of Brett Palmer mince@foldingcircles.co.uk]
# [No Copying Or Reading Or Use Permitted !]
"""
Copyright (c) 2023, Brett Palmer (Mince@foldingcircles.co.uk)

All rights reserved. No permission is granted for anyone, except the software owner, Brett Palmer, to use, copy, modify,
distribute, sublicense, or otherwise deal with the software in any manner.

Any unauthorized use, copying, or distribution of this software without the explicit written consent of the software
owner is strictly prohibited.

For permission requests, please contact the software owner, Brett Palmer, at Mince@foldingcircles.co.uk.
"""

# FoldingCircles Making The Unknown Known


import csv
import datetime

__version__ = "0.0.001"
print(f'report_history_gen.py {__version__}')

# Get current date and time
now = datetime.datetime.now()

# Format the date and time
date_str = now.strftime("%d_%b_%Y_%H%M%S")
filename = f"reports/report_history_{date_str}.csv"

# Create the CSV file with headers
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    headers = ["creation_date", "el_model", "yp", "indices", "label", "matching", "result_date"]
    writer.writerow(headers)

def extract_result_date(input_string):
    # Extract the result date from the input string
    parts = input_string.split('/')
    if len(parts) > 1:
        return parts[1]
    return ""

# Function to update the CSV file
def update_csv(creation_date, el_model, yp, indices, label, matching, for_from_r_string):
    result_date = extract_result_date(for_from_r_string)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([creation_date, el_model, yp, indices,label, matching, result_date])

# Example Usage
if __name__ == "__main__":
    update_csv("2024-07-14",
               "ModelX", "YP123",
               "1,2,3,4,5,6,7",
               "Label1",
               "Matching1",
               "readings/Sat-13-07-2024/2024-07-12T17-59-53")
