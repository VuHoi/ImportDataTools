
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
        isVariation = 0
        for row in datas :
            name=''
            timestamp = calendar.timegm(time.gmtime())
            if row['Type']=='variable' :
                for temp in template :
                    if temp['Type']=='variable' : 
                        isVariation=0
                        keys=temp['Keyword'].split('/')
                        if  keys[0].lower().strip() in row['Name'].lower().strip() or (len(keys)>0 and keys[len(keys)-1].lower().strip() in row['Name'].lower().strip() ) : 
                            isVariation=1
                            temp['Description']=row['Name']+ temp['Description'][8:]
                            temp['Short description']=row['Name']
                            temp['Images']=row['Images']
                            temp['Name']=row['Name']
                            temp['SKU']=timestamp
                            name=row['Name']
                            temp['Name']=row['Name'] 
                            writer.writerow(temp)
                    elif isVariation == 1:
                        temp['Name']=name 
                        temp['Parent']=timestamp 
                        writer.writerow(temp)

                    
            
                            
                

        



