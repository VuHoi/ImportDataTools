
import csv
import json
import copy
from datetime import datetime

# current date and time
# now = datetime.now()

# timestamp = datetime.timestamp(now)
# print("timestamp =", timestamp)


def get_template_line():
     # Read data that needs processing from CSV files
    template = []
    with open('product_template.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            template.append(row)

    return template[0]




template_line = get_template_line()
variable_data = copy.deepcopy(template_line)
variable_data = copy.deepcopy(template_line)
# variant_data = copy.deepcopy(template_line)
# fieldnames = template_line.keys()
# categories = []

# with open('desc.csv') as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         categories.append(row)

# with open('import.csv', 'w', newline='\n') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()

#     page = 1
#     products = get_product_page(page)

#     i = 0
  
