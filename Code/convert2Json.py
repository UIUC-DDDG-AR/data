import csv, json 

path_capability = "csv/capability.csv"
path_Hardware_capability = "csv/hardware_capability.csv"
path_Software_capability = "csv/software_capability.csv"
path_Hardware_information = "csv/hardware_information.csv"
path_Software_information = "csv/software_information.csv"

data_capability = []
with open(path_capability) as csv_capability:
    cap = csv.DictReader(csv_capability)
    for csvRow in cap:
        data_capability.append(csvRow)
with open("Capability/capability_information.json", 'w') as f1:
    f1.write(json.dumps(data_capability,indent=4))

data_H_capability = []
with open(path_Hardware_capability) as csv_hardWare:
    hd = csv.DictReader(csv_hardWare)
    for csvRow in hd:
        data_H_capability.append(csvRow)
for item in data_H_capability:
    # print (type(item.values()))
    for key in item:
        if item[key][:3] == 'yes':
            item[key] = (1,item[key][5:])
        if item[key][:2] == 'no':
            item[key] = (0,item[key][4:])
        if item[key][:8] == 'possible':
            item[key] = (2,item[key][10:])
    
with open("Hardware/hardware_capability.json", 'w') as f1:
    f1.write(json.dumps(data_H_capability,indent=4))

data_S_capability = []
with open(path_Software_capability) as csv_softWare:
    st = csv.DictReader(csv_softWare)
    for csvRow in st:
        data_S_capability.append(csvRow)

for item in data_S_capability:
    for key in item:
        if item[key][:3] == 'yes':
            item[key] = (1,item[key][5:])
        if item[key][:2] == 'no':
            item[key] = (0,item[key][4:])
        if item[key][:8] == 'possible':
            item[key] = (2,item[key][10:])

with open("Software/software_capability.json", 'w') as f1:
    f1.write(json.dumps(data_S_capability,indent=4))

data_H_information = []
with open(path_Hardware_information) as csv_H_capability:
    h_cap = csv.DictReader(csv_H_capability)
    for csvRow in h_cap:
        data_H_information.append(csvRow)
for item in data_H_information:
    if (item['field_of_view'] != ''):
        item['field_of_view'] = int(item['field_of_view']) 
    item['use_cases'] = item['use_cases'].split(', ')
    item['related_softwares'] = item['related_softwares'].split(', ')
    item['related_hardwares'] = item['related_hardwares'].split(', ')
    item['customer_segment'] = item['customer_segment'].split(', ')
    item['possible_interactions'] = item['possible_interactions'].split(', ')

with open("Hardware/hardware_documentation.json", 'w') as f1:
    f1.write(json.dumps(data_H_information,indent=4))

data_S_information = []
with open(path_Software_information) as csv_S_capability:
    s_cap = csv.DictReader(csv_S_capability)
    for csvRow in s_cap:
        data_S_information.append(csvRow)
for item in data_S_information:
    item['related_softwares'] = item['related_softwares'].split(', ')
    item['related_hardwares'] = item['related_hardwares'].split(', ')   
    item['key_features'] = item['key_features'].split(', ')
        
with open("Software/software_documentation.json", 'w') as f1:
    f1.write(json.dumps(data_S_information,indent=4))


