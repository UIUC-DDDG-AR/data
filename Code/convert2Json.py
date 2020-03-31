import csv, json 

path_Hardware_clean = "/Users/scottwang/Desktop/AR/FeatureMappingData/ARTool_Hardware.csv"
path_Software_clean = "/Users/scottwang/Desktop/AR/FeatureMappingData/ARTool_Software.csv"
path_capability = "/Users/scottwang/Desktop/AR/FeatureMappingData/ARTool_ARCapability.csv"
path_HC = "/Users/scottwang/Desktop/AR/FeatureMappingData/HardwareInfo.csv"
path_SC = "/Users/scottwang/Desktop/AR/FeatureMappingData/SoftwareInfo.csv"

data_hardware = {}
with open(path_Hardware_clean) as csv_hardWare:
    hd = csv.DictReader(csv_hardWare)
    for csvRow in hd:
        hardware = csvRow["Hardware"]
        data_hardware[hardware] = csvRow
with open("/Users/scottwang/Desktop/AR/FeatureMappingData/Hardware_Capability.json", 'w') as f1:
    f1.write(json.dumps(data_hardware,indent=4))

data_software = {}
with open(path_Software_clean) as csv_softWare:
    st = csv.DictReader(csv_softWare)
    for csvRow in st:
        software = csvRow["Software"]
        data_software[software] = csvRow
with open("/Users/scottwang/Desktop/AR/FeatureMappingData/Software_Capability.json", 'w') as f1:
    f1.write(json.dumps(data_software,indent=4))

data_capability = {}
with open(path_capability) as csv_capability:
    cap = csv.DictReader(csv_capability)
    for csvRow in cap:
        capability = csvRow["Capability"]
        data_capability[capability] = csvRow
with open("/Users/scottwang/Desktop/AR/FeatureMappingData/CapabilityIntro.json", 'w') as f1:
    f1.write(json.dumps(data_capability,indent=4))

data_H_capability = {}
with open(path_HC) as csv_H_capability:
    h_cap = csv.DictReader(csv_H_capability)
    for csvRow in h_cap:
        H_capability = csvRow["Hardware"]
        data_H_capability[H_capability] = csvRow
with open("/Users/scottwang/Desktop/AR/FeatureMappingData/HardwareIntro.json", 'w') as f1:
    f1.write(json.dumps(data_H_capability,indent=4))

data_S_capability = {}
with open(path_SC) as csv_S_capability:
    s_cap = csv.DictReader(csv_S_capability)
    for csvRow in s_cap:
        S_capability = csvRow["Software"]
        data_S_capability[S_capability] = csvRow
with open("/Users/scottwang/Desktop/AR/FeatureMappingData/Sardware_Intro.json", 'w') as f1:
    f1.write(json.dumps(data_S_capability,indent=4))


