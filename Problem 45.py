pList = []
tList = []
hList = []

for n in range (1,100000):
    pList.append((n*(3*n-1))/2)
    tList.append((n*(n+1))/2)
    hList.append((n*(2*n-1)))

n = 285
notFound = True
while notFound == True:
    n = n + 1
    if hList[n] in tList[n:len(tList)]:
        if hList[n] in pList[n:len(tList)]:
            notFound = False

print(hList[n])
