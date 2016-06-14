totalSum = 0
abundantNumList = []
def divisorGenerator(n):
    returnList = []
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            returnList.append(i)
    return(returnList) 

def findSums(testNum, searchList):
    returnVal = 0
    done = 0
    index = 0
    maxIndex = searchList.index(
    while done == 0:
        if searchList[index1]+searchList[index2] == testNum:
            done = 1
            returnVal = 1
            

for index in range(12,50): #28123):
    divisorList = divisorGenerator(index)
    if sum(divisorList) > index:
        #abundantNumber
        abundantNumList.append(index)

print("starting search")

for index in range (2,50): #28123,2):
    foundSum = findIfNum(index, abudnantNumList)
    if foundSum == 1:
        #found an even number that can't be written
        #as a sum of two abundant numbers
        print(index)
        totalSum += index

print(totalSum)


