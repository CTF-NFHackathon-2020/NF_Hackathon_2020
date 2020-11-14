import csv
import requests
import json 

# Pathways mapping 
pathwaysSet = set()
pathwaysDict = {}
count = 0
geneDict = {}
with open('pathways.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        if int(row[2]) > 99: 
            pathwaysDict[row[0]] = row[13]
            geneString = row[13]
            onlyGenes = geneString.split(";")
            count += len(onlyGenes)
            for m in onlyGenes:
                if m in geneDict.keys():
                    temp = geneDict[m]
                    geneDict[m] = temp + 1
                else:
                    geneDict[m] = 1
                pathwaysSet.add(m)
        
print(count)
print(len(pathwaysSet))
result = sorted(geneDict.items() , key=lambda t : t[1])

for k,v in result[:200]:
  print(k,v)

# for k,v in geneDict.items():
#     print(k, v)
# print(pathwaysSet)
# for k,v in pathwaysDict.items():
#     print()
#     print(k, v)


with open('pathways.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        # print(row[0], row[13])
        pathwaysDict[row[0]] = row[13]

DRUG Fetch Req Code 
URL = "https://dgidb.org/api/v2/interactions.json?"  
geneDrugDict = {}
for geneName in list(pathwaysSet):
    PARAMS = {'genes':geneName} 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    # x = json.loads(str(data)) 
    with open('data.json', 'w') as f:
        json.dump(data, f ,indent=4)
    with open('data.json', 'r') as f:
        json_data = json.load(f)
    interactions = json_data['matchedTerms'][0]['interactions'] 

    drugList = []    
    for m in interactions:
        drugList.append((str(m['drugName']), int(m['score'])))
    geneDrugDict[geneName] = drugList
    print(drugList)


# Pathways -> Genes -> Drugs [Priority]

# {geneName: [List of drugs and their scores]}

# [geneName: count]


