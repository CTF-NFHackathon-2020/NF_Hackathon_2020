import random 
allString = ""
for i in range(74):
    for j in range(74):
        val = str(random.randint(0, 7))
        stringLine = "{\"source\": \"" + str(i) +"\", \"target\":" + str(j) + ",\"value\": \"" + val + "\"},"
        allString = allString + stringLine
    # print(i)
    # stringLine = "{\"group\": \"" + i +"\", \"index\":" + i + ",\"name\": \"" + i + "\"},"
    # print(stringLine)
print(allString)
f = open("demo.txt", "a")
f.write(allString)
f.close()