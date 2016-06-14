pyramid = [[75],\
           [95,64],\
           [17,47,82], \
           [18,35,87,10],\
           [20,4,82,47,65],\
           [19,1, 23, 75,3, 34],\
           [88,2, 77, 73,7, 63, 67],\
           [99, 65,4, 28,6, 16, 70, 92],\
           [41, 41, 26, 56, 83, 40, 80, 70, 33],\
           [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],\
           [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],\
           [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],\
           [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],\
           [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],\
           [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

testPyramid = [[3],[7,4],[2,4,6],[8,5,9,3]]

maxSum = 0
tempMaxSum = 0
pyramidToUse = testPyramid

treeNodeRow = len(pyramidToUse)-1
treeNodeCol = 0

def generatePathIndices(numRows):
    numPaths = 2**(numRows-1)
    pathIndices = []
    print(pathIndices)
    currentPath = []
    #create path of all zeros
    currentPath = [0]*(numRows)
    pathIndices.append(list(currentPath))
    pathCounter = 1
    majorIdx = len(currentPath)-1
    minorIdx = majorIdx
    while pathCounter < numPaths:
        print("------")
        currentPath[minorIdx] += 1
        print(majorIdx, minorIdx)
        print(currentPath)
        if (currentPath[minorIdx] - currentPath[minorIdx-1]) == 2:
            #print("Roll Over")
            majorIdx -= 1
            currentPath[majorIdx] += 1
            if (minorIdx-majorIdx) == 1:
                print("Major Reset")
                for idx in range(majorIdx,len(currentPath)):
                    currentPath[idx] = currentPath[majorIdx]
                    minorIdx = len(currentPath)-1
            else:
                print("Minor Reset")
                minorIdx -= 1
                currentPath[minorIdx] += 1
                for idx in range(minorIdx,len(currentPath)):
                    currentPath[idx] = currentPath[idx-1]
                
        print(currentPath)                    
        pathIndices.append(list(currentPath))
        pathCounter += 1
        
    return pathIndices

def findMaxSum(paths,pyramid):
    maxTotal = 0
    maxPathIdx = 0
    for pathIdx in range(0,len(paths)):
        #print(paths[pathIdx])
        total = 0
        for pyramidIdx in range(0,len(pyramid)):
            #print(paths[pathIdx][pyramidIdx])
            total += (pyramid[pyramidIdx][paths[pathIdx][pyramidIdx]])
        #print(total)
        if total >= maxTotal:
            maxTotal = total
            maxPathIdx = pathIdx
            
    return [maxTotal,maxPathIdx]


pyramidIndices = generatePathIndices(len(pyramidToUse))
#pyramidIndices = [[0,0,1,2],[0,0,0,0]]
#print(pyramidIndices)

#[maxSum,maxPathIdx] = findMaxSum(pyramidIndices, pyramidToUse)

print(maxSum,pyramidIndices[maxPathIdx])
