
import csv
import copy
import sys
import glob
import calendar
import time


# current date and time
# timestamp = calendar.timegm(time.gmtime())
template = []


def get_template_line():
     # Read data that needs processing from CSV files

    with open('product_template.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            template.append(row)

    temp1 = copy.deepcopy(template[0])
    del temp1['Keyword']
    return temp1


template_line = get_template_line()
variable_data = copy.deepcopy(template_line)
variation_data = copy.deepcopy(template_line)
fileCSVs = glob.glob("list_csv_in/*.csv")
fieldnames = template_line.keys()
datas = []

for file in fileCSVs:
    datas = []
    with open('list_csv_in/'+file[12:]) as f:
        reader = csv.DictReader(f)
        for row in reader:
            datas.append(row)

    with open('list_csv_out\\'+file[12:], 'w', newline='\n') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        isVariation = 0
        name = ''
        for row in datas:
            timestamp = calendar.timegm(time.gmtime())
            if row['Type'] == 'variable':
                for temp in template:
                    variable_data=copy.deepcopy(temp)
                    if variable_data['Type'] == 'variable':
                        if name == row['Name']:
                            break
                        isVariation = 0
                        keys = temp['Keyword'].split('/')
                        if (keys[0].lower() in row['Name'].lower() or (len(keys) > 0 and keys[len(keys)-1].lower() in row['Name'].lower())) and len(variable_data['Description'])>0:
                            isVariation = 1
                            variable_data['Description'] =  row['Name']+ ' ' +variable_data['Description'][8:]
                            variable_data['Short description'] = row['Name']
                            variable_data['Images'] = row['Images']
                            variable_data['Name'] = row['Name']
                            variable_data['SKU'] = timestamp
                            name = row['Name']
                            variable_data['Name'] = row['Name']
                            a= copy.deepcopy(variable_data)
                            del a['Keyword']
                            writer.writerow(a)
                    elif isVariation == 1:
                        variable_data['Name'] = name
                        variable_data['Parent'] = timestamp
                        a= copy.deepcopy(variable_data)
                        del a['Keyword']
                        writer.writerow(a)
    

