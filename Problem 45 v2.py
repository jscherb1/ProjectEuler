pList = []
tList = []
hList = []

for n in range (1,100000):
    pList.append((n*(3*n-1))/2)
    tList.append((n*(n+1))/2)
    hList.append((n*(2*n-1)))

TPList = list(set(tList).intersection(pList))
finalList = list(set(TPList).intersection(hList))

print(finalList)
