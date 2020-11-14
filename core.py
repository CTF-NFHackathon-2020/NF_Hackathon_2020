import csv
import requests
import json 

drugDict = {}
drugSet = set()
geneDict = {}
with open('base.tsv', mode='r') as infile:
    reader = csv.reader(infile, delimiter="\t")
    for row in reader:
        if row[0] in geneDict.keys():
            temp1 = geneDict[row[0]]
            geneDict[row[0]] = temp1 + 1
        else:
            geneDict[row[0]] = 1
        drugSet.add(row[0])
        
        if row[4] in drugDict.keys():
            temp = drugDict[row[4]]
            drugDict[row[4]] = temp + 1
        else:
            drugDict[row[4]] = 1

resultDrug = sorted(drugDict.items() , key=lambda t : t[1])
i = 0
for k,v in resultDrug:
    m = str(i)
    # stringLine = "{\"group\": \"" + str(v) +"\", \"index\":" + m + ",\"name\": \"" + k + "\"},"
    # print(stringLine)
    # i = i + 1
    print(k,float(v))


resultGene = sorted(geneDict.items() , key=lambda t : t[1])
i = 0
for k,v in resultGene:
  m = str(i)
#   stringLine = "{\"group\": \"" + str(v) +"\", \"index\":" + m + ",\"name\": \"" + k + "\"},"
#   print(stringLine)
#   i = i + 1
#  print(k,v)

# import csv

with open('base_data.csv', mode='w') as e_file:
    e_writer = csv.writer(e_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for k,v in resultDrug[-50:-1]:
        for k1,v1 in resultGene[-50:-1]:
            e_writer.writerow([k1, k, float(v1*v)])
    
    
    
# allString = ""
# i = 0
# for k,v in resultDrug[:74]:
#     j = 0
#     for k1,v1 in resultGene[:74]:
#         stringLine = "{\"source\": \"" + str(i) +"\", \"target\":" + str(j) + ",\"value\": \"" + str(v1*v) + "\"},"
#         allString = allString + stringLine
#         j = j + 1
#     i = i + 1

# print(allString)
# f = open("final_demo.txt", "a")
# f.write(allString)
# f.close()

# URL = "https://dgidb.org/api/v2/interactions.json?"  
# geneDrugDict = {}
# for geneName in result:
#     print(geneName[0])
#     PARAMS = {'genes':geneName[0]} 
#     r = requests.get(url = URL, params = PARAMS) 
#     data = r.json()
#     # x = json.loads(str(data)) 
#     with open('data.json', 'w') as f:
#         json.dump(data, f ,indent=4)
#     with open('data.json', 'r') as f:
#         json_data = json.load(f)
#     interactions = json_data['matchedTerms'][0]['interactions'] 

#     drugList = []    
#     for m in interactions:
#         drugList.append((str(m['drugName']), int(m['score'])))
#     geneDrugDict[geneName] = drugList
#     print(drugList)
# print(drugSet)
# print(len(drugSet))
