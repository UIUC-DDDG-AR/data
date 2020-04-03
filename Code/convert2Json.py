import csv, json 

path_capability = "/Users/scottwang/Desktop/AR/data/csv/ARTool_ARCapability.csv"
path_Hardware_capability = "/Users/scottwang/Desktop/AR/data/csv/ARTool_Hardware.csv"
path_Software_capability = "/Users/scottwang/Desktop/AR/data/csv/ARTool_Software.csv"
path_Hardware_information = "/Users/scottwang/Desktop/AR/data/csv/Hardware_Info.csv"
path_Software_information = "/Users/scottwang/Desktop/AR/data/csv/Software_Info.csv"

data_capability = {}
with open(path_capability) as csv_capability:
    cap = csv.DictReader(csv_capability)
    for csvRow in cap:
        capability = csvRow["Capability"]
        data_capability[capability] = csvRow
with open("/Users/scottwang/Desktop/AR/data/Capability/capability_information.json", 'w') as f1:
    f1.write(json.dumps(data_capability,indent=4))

data_H_capability = {}
with open(path_Hardware_capability) as csv_hardWare:
    hd = csv.DictReader(csv_hardWare)
    for csvRow in hd:
        hardware = csvRow["Hardware"]
        data_H_capability[hardware] = csvRow
with open("/Users/scottwang/Desktop/AR/data/Hardware/hardware_capability.json", 'w') as f1:
    f1.write(json.dumps(data_H_capability,indent=4))

data_S_capability = {}
with open(path_Software_capability) as csv_softWare:
    st = csv.DictReader(csv_softWare)
    for csvRow in st:
        software = csvRow["Software"]
        data_S_capability[software] = csvRow
with open("/Users/scottwang/Desktop/AR/data/Software/software_capability.json", 'w') as f1:
    f1.write(json.dumps(data_S_capability,indent=4))

data_H_information = {}
with open(path_Hardware_information) as csv_H_capability:
    h_cap = csv.DictReader(csv_H_capability)
    for csvRow in h_cap:
        H_capability = csvRow["Hardware"]
        data_H_information[H_capability] = csvRow
with open("/Users/scottwang/Desktop/AR/data/Hardware/hardware_information.json", 'w') as f1:
    f1.write(json.dumps(data_H_information,indent=4))

data_S_information = {}
with open(path_Software_information) as csv_S_capability:
    s_cap = csv.DictReader(csv_S_capability)
    for csvRow in s_cap:
        S_capability = csvRow["name"]
        data_S_information[S_capability] = csvRow
with open("/Users/scottwang/Desktop/AR/data/Software/software_information.json", 'w') as f1:
    f1.write(json.dumps(data_S_information,indent=4))


