def combine_integers(numList):
    s = ''.join(map(str, numList))
    return int(s)

numList = []
number = 1
numList.append(str(number))
while len(numList)<1000000:
    number = number+1
    numList = numList + list(str(number))

resultProd = int(numList[0])*int(numList[9])*int(numList[99])*int(numList[999])*int(numList[9999])*int(numList[99999])*int(numList[999999])

#print(numList)
print(resultProd)
