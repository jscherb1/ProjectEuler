#create pyramid

keys = ['A', 'B', 'C','D','E','F','G','H','I','J',\
        'K','L','M','N','O','P','Q','R','S','T','U',\
        'V','W','X','Y','Z','AA','AB','AC','AD','AE',\
        'AF','AG','AH','AI','AJ','AK','AL','AM','AN',\
        'AO','AP','AQ','AR','AS','AT','AU','AV','AW',\
        'AX','AY','AZ','BA','BB','BC','BD','BE','BF',\
        'BG','BH','BI','BJ','BK','BL','BM','BN','BO',\
        'BP','BQ','BR','BS','BT','BU','BV','BW','BX',\
        'BY','BZ','CA','CB','CC','CD','CE','CF','CG',\
        'CH','CI','CJ','CK','CL','CM','CN','CO','CP',\
        'CQ','CR','CS','CT','CU','CV','CW','CX','CY',\
        'CZ','DA','DB','DC','DD','DE','DF','DG','DH',\
        'DI','DJ','DK','DL','DM','DN','DO','DP','DQ',\
        'DR','DS','DT','DU','DV','DW','DX','DY','DZ',\
        'EA','EB','EC','ED','EF','EG','EH','EI','EJ']

##values = [3, 7, 4,2,4,6,8,5,9,3]
values = [75,95,64,17,47,82,18,35,87,10,20,4,82,47,65,\
          19,1,23,75,3,34,88,2,77,73,7,63,67,\
          99,65,4,28,6,16,70,92,\
          41,41,26,56,83,40,80,70,33,\
          41,48,72,33,47,32,37,16,94,29,\
          53,71,44,65,25,43,91,52,97,51,14,\
          70,11,33,28,77,73,17,78,39,68,17,57,\
          91,71,52,38,17,14,91,43,58,50,27,29,48,\
          63,66,4,68,89,53,67,30,73,16,69,87,40,31,\
          4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
    
numRows = 2

leftEdgeList = []
leftEdgeList.append(0)
rightEdgeList = []
rightEdgeList.append(0)

for num in range(1,numRows):
    leftEdgeList.append(leftEdgeList[num-1]+num)
    rightEdgeList.append(rightEdgeList[num-1]+num+1)

#print(leftEdgeList)
#print(rightEdgeList)

def dfs_paths(graph, start, goal, path=None):
    #print(path)
    if path is None:
        path = [start]
    if start == goal:
        yield path
    if keys.index(path[len(path)-2])>keys.index(path[len(path)-1]):
        exit
    else:
        for next in graph[start] - set(path):
            yield from dfs_paths(graph, next, goal, path + [next])
                                       
def is_left_edge(cur):
    if cur in leftEdgeList:
        return True
    else:
        return False   
def is_right_edge(cur):
    if cur in rightEdgeList:
        return True
    else:
        return False


currentRow = 0
elementCount = 0
bottomRow = []

#add the top of pyramid
connectionList = keys[1:3]
pyramid = {keys[elementCount] : set(connectionList)}
currentRow += 1
elementCount += 1

previousLeftEdge = 0
previousRightEdge = 0

#print(pyramid)

while currentRow <= numRows-1:
    #continue building the pyrmid until
    #your row count is greater than the number
    #of rows specified by user
    connectingSet = []
    parents = []
    children = []
    incrementRow = False
    
    if is_left_edge(elementCount):
        #left edge
        #print("Left edge")
        
        #parents
        idx = elementCount-currentRow
        if idx > len(keys) or idx < 0:
            idx = 0
        parents.append(keys[idx])

        #add children
        children.append(keys[elementCount+(currentRow+1)+1])
        children.append(keys[elementCount+(currentRow+1)])
        
        previousLeftEdge = elementCount
        
    elif is_right_edge(elementCount):
        #right edge
        #print("Right edge")
        previousRightEdge = elementCount
        #parents
        idx = elementCount-currentRow-1
        if idx > len(keys) or idx < 0:
            idx = 0
        parents.append(keys[idx])

        #add children
        children.append(keys[elementCount+(currentRow+1)+1])
        children.append(keys[elementCount+(currentRow+1)])
        
        incrementRow = True
    else:
        #print("not an edge")
        #is in the center of pyramid
        #get parents
        parents.append(keys[elementCount-currentRow])
        parents.append(keys[elementCount-(currentRow+1)])

        #add children
        children.append(keys[elementCount+(currentRow+1)+1])
        children.append(keys[elementCount+(currentRow+1)])

    if currentRow == numRows-1:
        #last row, no children
        connectingSet.append(parents)
        bottomRow.append(keys[elementCount])
    else:
        connectingSet.append(parents+children)

    #print({keys[elementCount] : set(connectingSet[0])})
    
    pyramid.update({keys[elementCount] : set(connectingSet[0])})
    
    elementCount += 1

    if incrementRow == True:
        currentRow += 1

#print(pyramid)

finalList = []
for item in bottomRow:
    print(item)
    tempPaths = list(dfs_paths(pyramid,'A',item))
    for idx in range(0,len(tempPaths)):
        finalList.append(tempPaths[idx])
    
#paths = list(dfs_paths(graph, 'A', 'H'))
##print(len(paths))
##print(paths)
###filter out all paths that go up in tree
##finalList = []
##for idx in range(0,len(paths)):
##    if len(paths[idx]) <= numRows:
##        finalList.append(paths[idx])

##print(finalList)
print("Number of Paths for a diamond: ",len(finalList)*2)

####pathSum = []
####for item in finalList:
####    tempSum = 0
####    for value in item:
####        tempSum += values[keys.index(value)]
####    pathSum.append(tempSum)
####
####print(max(pathSum), finalList[pathSum.index(max(pathSum))])

