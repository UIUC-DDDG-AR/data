import csv, json 

path_usecase = "csv/example_page_content.csv"

usecase = []
# array = []
with open(path_usecase) as csv_usecase:
    uc = csv.DictReader(csv_usecase)
    for csvRow in uc:
        usecase.append(csvRow)
# for item in usecase:
#     # print (type(item))
#     for key in item:
#         if item[key][:3] == 'yes':
#             item[key] = (1,item[key][5:])
#         if item[key][:2] == 'no':
#             item[key] = (0,item[key][4:])
#         if item[key][:8] == 'possible':
#             item[key] = (2,item[key][10:])

with open("example_page_content.json", 'w') as f1:
    f1.write(json.dumps(usecase,indent=4))