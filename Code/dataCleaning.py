import csv, json 

path_Hardware = "/Users/scottwang/Desktop/AR/data/csv/hardware_capability.csv"
path_Software = "/Users/scottwang/Desktop/AR/data/csv/software_capability.csv"

hardWare = []
hardWare_copy = []
softWare = []
softWare_copy = []
# read csv and get data
with open(path_Hardware, 'rt') as f1, open(path_Software, 'rt') as f2:
    hd = csv.reader(f1)
    st = csv.reader(f2)
    for i in hd:
        hardWare.append(i)
    for j in st:
        softWare.append(j)

# clean data to only yes/no
    for item1 in hardWare:
        if item1[0] == 'Hardware':
            hardWare_copy.append(item1)
            continue
        for i in range(1, len(item1)):
            if item1[i][:3] == 'yes':
                item1[i] = True
                # print (type(item1[i]))
            else :
                item1[i] = False
        hardWare_copy.append(item1)

    for item2 in softWare:
        if item2[0] == 'Software':
            softWare_copy.append(item2)
            continue
        for i2 in range(1, len(item2)):
            if item2[i2][:3] == 'yes':
                item2[i2] = True
            else :
                item2[i2] = False
        softWare_copy.append(item2)

# wirte clean data to csv
path_Hardware_clean = "/Users/scottwang/Desktop/AR/data/csv/cleaned_hardware_capability.csv"
path_Software_clean = "/Users/scottwang/Desktop/AR/data/csv/cleaned_software_capability.csv"
with open(path_Hardware_clean,'w') as f3:
    f3 = csv.writer(f3)
    for row in hardWare_copy:
        f3.writerow(row)
with open(path_Software_clean,'w') as f4:
    f4 = csv.writer(f4)
    for row in softWare_copy:
        f4.writerow(row)
