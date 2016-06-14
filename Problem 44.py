pentagonalList = []
for n in range(1,10001):
    pentagonalList.append((n*(3*n-1))/2)

j = 1
k = 1
solutionFound = False
for j in range(1,5000):
    for k in range(j,-1,-1):
        #print(j,k)
        if (pentagonalList[j]+pentagonalList[k]) in pentagonalList:
            if abs(pentagonalList[j]-pentagonalList[k]) in pentagonalList:
                solutionFound = True
                D = abs(pentagonalList[j]-pentagonalList[k])
    if solutionFound == True:
        break
    
print(D)
print(pentagonalList[j], j)
print(pentagonalList[k], k)
            
