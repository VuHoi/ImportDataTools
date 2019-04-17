
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

    return template[0]


template_line = get_template_line()
variable_data = copy.deepcopy(template_line)
variation_data = copy.deepcopy(template_line)
fileCSVs = glob.glob("list_csv_in/*.csv")
fieldnames = template_line.keys()
datas=[]

for file in fileCSVs:
    datas=[]
    with open('list_csv_in/'+file[12:]) as f:
        reader = csv.DictReader(f)

        for row in reader:
            datas.append(row)

    with open('list_csv_out\\'+file[12:], 'w', newline='\n') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in datas :
            for temp in template :
                if temp['Keyword']!='' : 
                    keys=temp['Keyword'].split('/')
                    if (keys[0].lower().strip() in row['Name'].lower().strip() ) and temp['Keyword']!='' : 
                        timestamp = calendar.timegm(time.gmtime())
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
                            variable_data['Name']=row['Name']
                            variable_data['Keyword']=temp['Keyword']
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
                            variable_data['Name']=''
                            variable_data['Keyword']=''
                        variable_data['Sale price']=row['Sale price']
                        variable_data['Regular price']=row['Regular price']
                        variable_data['Categories']=row['Categories']
                        variable_data['Attribute 1 name']=row['Attribute 1 name']
                        variable_data['Attribute 1 global']=row['Attribute 1 global']
                        variable_data['Attribute 2 name']=row['Attribute 2 name']
                        variable_data['Attribute 2 value(s)']=row['Attribute 2 value(s)']
                        variable_data['Attribute 2 visible']=row['Attribute 2 visible']
                        variable_data['Attribute 2 global']=row['Attribute 2 global']
                        variable_data['Attribute 1 value(s)']=row['Attribute 1 value(s)']
                        variable_data['In stock?']=1
                        variable_data['Tax status']='taxable'
                        writer.writerow(variable_data)
                        break

        



