
import csv
import json
import copy
from datetime import datetime
import sys
# current date and time
now = datetime.now()
timestamp = datetime.timestamp(now)
template = []
def get_template_line():
     # Read data that needs processing from CSV files
   
    with open('product_template.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            template.append(row)

    return template[0]


template_line = get_template_line()
variable_data = copy.deepcopy(template_line)
variation_data = copy.deepcopy(template_line)

fieldnames = template_line.keys()
datas=[]
with open('list_csv_in/'+sys.argv[1]) as f:
    reader = csv.DictReader(f)

    for row in reader:
        datas.append(row)

with open('list_csv_out/'+sys.argv[1], 'w', newline='\n') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    # writer.writerow(get_template_line())
    for row in datas :
        for temp in template :
            if temp['Keyword'].lower().strip() in row['Name'].lower().strip() and temp['Keyword']!='' : 
                if row['Type']=='variable' : 
                    variable_data['Description']=row['Name']+ temp['Description'][8:]
                    variable_data['Visibility in catalog']='visible'
                    variable_data['Type']='variable'
                    variable_data['Short description']=row['Name']
                    variable_data['Allow customer reviews?']=1
                    variable_data['Tax class']=' '
                    variable_data['Images']=row['Images']
                    variable_data['Categories']=row['Categories']
                    variable_data['SKU']=timestamp
                    variable_data['Parent']=''
                else :
                    variable_data['Allow customer reviews?']=0
                    variable_data['Type']='variation'
                    variable_data['Tax class']='parent'
                    variable_data['Short description']=''
                    variable_data['Description']=''
                    variable_data['Images']=''
                    variable_data['Categories']=''
                    variable_data['SKU']=''
                    variable_data['Parent']=timestamp
                
                variable_data['Regular price']=row['Regular price']
                variable_data['Categories']=row['Categories']
                variable_data['Attribute 1 name']=row['Attribute 1 name']
                variable_data['Attribute 1 global']=row['Attribute 1 global']
                variable_data['Attribute 2 name']=row['Attribute 2 name']
                variable_data['Attribute 2 value(s)']=row['Attribute 2 value(s)']
                variable_data['Attribute 2 visible']=row['Attribute 2 visible']
                variable_data['Attribute 2 global']=row['Attribute 2 global']
                variable_data['Name']=row['Name']
                variable_data['Attribute 1 value(s)']=temp['Attribute 1 value(s)']
                variable_data['Keyword']=temp['Keyword']
                variable_data['In stock?']=1
                variable_data['Tax status']='taxable'
                writer.writerow(variable_data)

        



