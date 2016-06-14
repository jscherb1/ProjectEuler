import csv
with open('p022_names.txt') as f:
    reader = csv.reader(f, delimiter=",")
    d = list(reader)
#print (d)
    
nameList = list(d[0])
nameListSrt = sorted(nameList)

resultSum = 0

for index in range(0,len(nameListSrt)):
    name = nameListSrt[index]
    #print(name)
    nameLength = len(list(str(name)))
    nameSum = 0
    for letterIdx in range(0,nameLength):
        nameSum = nameSum + (ord(name[letterIdx])-64)
        #print(name[letterIdx], '=', (ord(name[letterIdx])-64))
    #print(nameSum, index+1)
    resultSum = resultSum + (nameSum*(index+1))
    
print (resultSum)
