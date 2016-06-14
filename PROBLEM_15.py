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
##values = [75,95,64,17,47,82,18,35,87,10,20,4,82,47,65,\
##          19,1,23,75,3,34,88,2,77,73,7,63,67,\
##          99,65,4,28,6,16,70,92,\
##          41,41,26,56,83,40,80,70,33,\
##          41,48,72,33,47,32,37,16,94,29,\
##          53,71,44,65,25,43,91,52,97,51,14,\
##          70,11,33,28,77,73,17,78,39,68,17,57,\
##          91,71,52,38,17,14,91,43,58,50,27,29,48,\
##          63,66,4,68,89,53,67,30,73,16,69,87,40,31,\
##          4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
    

#number of rows is equivalent for the center width of the diamond
numRows = 21

diamondHeight = numRows*2-1

lastItemList = []
lastItemList.append(0)
for num in range(3,numRows+1,2):
    lastItemList.append(lastItemList[len(lastItemList)-1]+num)

topLeftEdgeList = []
topLeftEdgeList.append(0)
topRightEdgeList = []
topRightEdgeList.append(0)
rowCount = 0
for num in range(1,round(numRows/2)+1):
    topLeftEdgeList.append(topLeftEdgeList[num-1]+num)
    topRightEdgeList.append(topRightEdgeList[num-1]+num+1)
    rowCount += 1

bottomLeftEdgeList = []
bottomLeftEdgeList.append(topLeftEdgeList[len(topLeftEdgeList)-1] + \
                          round(numRows/2)+1)
bottomRightEdgeList = []
bottomRightEdgeList.append(topRightEdgeList[len(topRightEdgeList)-1] + \
                          round(numRows/2))

for num in range(round(numRows/2)+1, diamondHeight-1):
    bottomLeftEdgeList.append(bottomLeftEdgeList[(len(bottomLeftEdgeList)-1)]+rowCount)
    bottomRightEdgeList.append(bottomRightEdgeList[(len(bottomRightEdgeList)-1)]+rowCount-1)
    rowCount -= 1

bottomLeftEdgeList = list(set(bottomLeftEdgeList))
bottomRightEdgeList = list(set(bottomRightEdgeList))
print("TL: ",topLeftEdgeList)
print("TR: ",topRightEdgeList)
print("BL: ",bottomLeftEdgeList)
print("BR: ",bottomRightEdgeList)

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
                                       
def is_left_edge_top(cur):
    if cur in topLeftEdgeList:
        return True
    else:
        return False   
def is_right_edge_top(cur):
    if cur in topRightEdgeList:
        return True
    else:
        return False
def is_left_edge_bottom(cur):
    if cur in bottomLeftEdgeList:
        return True
    else:
        return False   
def is_right_edge_bottom(cur):
    if cur in bottomRightEdgeList:
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
bottomIncrement = 0
topHalf = True
bLastItem = False
while bLastItem != True:
    #continue building the pyrmid until
    #your row count is greater than the number
    #of rows specified by user
    connectingSet = []
    parents = []
    children = []
    incrementRow = False

    if topHalf == True:
        if is_left_edge_top(elementCount):
            #left edge
            #print("Left edge")
            
            #parents
            idx = elementCount-currentRow
            if idx > len(keys) or idx < 0:
                idx = 0
            parents.append(keys[idx])

            #add children
            if currentRow == round(numRows/2):
                #last row, children are different
                children.append(keys[elementCount+(currentRow+1)])
            else:
                children.append(keys[elementCount+(currentRow+1)+1])
                children.append(keys[elementCount+(currentRow+1)])
            
            previousLeftEdge = elementCount
            
        elif is_right_edge_top(elementCount):
            #right edge
            print("Right edge")
            previousRightEdge = elementCount
            #parents
            idx = elementCount-currentRow-1
            if idx > len(keys) or idx < 0:
                idx = 0
            parents.append(keys[idx])

            #add children
            if currentRow == round(numRows/2):
                print("Top Half Right Edge")
                #last row, children are different
                children.append(keys[elementCount+(currentRow)])
                topHalf = False
                bottomIncrement = currentRow+1
            else:
                children.append(keys[elementCount+(currentRow+1)+1])
                children.append(keys[elementCount+(currentRow+1)])
            
            incrementRow = True
        else:
            #print("not an edge")
            #is in the center of pyramid
            #get parents
            parents.append(keys[elementCount-currentRow])
            parents.append(keys[elementCount-(currentRow+1)])

            if currentRow == round(numRows/2):
                #last row, children are different
                children.append(keys[elementCount+(currentRow)])
                children.append(keys[elementCount+(currentRow+1)])
            else:
                #add children
                children.append(keys[elementCount+(currentRow+1)+1])
                children.append(keys[elementCount+(currentRow+1)])
            
        connectingSet.append(parents+children)
    else:
        #bottom half of diamond
        if is_left_edge_bottom(elementCount) and is_right_edge_bottom(elementCount):
            #left edge
            print("Bottom Point", elementCount)
            
            #parents
            parents.append(keys[elementCount-(bottomIncrement)-1])
            parents.append(keys[elementCount-(bottomIncrement)])

            #last item
            incrementRow = True
            lastItem = keys[elementCount]
            bLastItem = True
        elif is_left_edge_bottom(elementCount):
            #left edge
            print("Bottom Left edge", elementCount)
            
            #parents
            parents.append(keys[elementCount-(bottomIncrement)-1])
            parents.append(keys[elementCount-(bottomIncrement)])

            #children
            children.append(keys[elementCount+(bottomIncrement)])

        elif is_right_edge_bottom(elementCount):
            #right edge
            print("Bottom Right edge", elementCount)
            #parents
            parents.append(keys[elementCount-bottomIncrement-1])
            parents.append(keys[elementCount-bottomIncrement])
            
            children.append(keys[elementCount+(bottomIncrement)-1])

            incrementRow = True
        else:
            print("Bottom: not an edge")
            #is in the center of pyramid
            #get parents
            parents.append(keys[elementCount-bottomIncrement])
            parents.append(keys[elementCount-(bottomIncrement-1)])
            
            children.append(keys[elementCount+(bottomIncrement)])
            children.append(keys[elementCount+(bottomIncrement-1)])

            
        connectingSet.append(parents+children)
        
    print({keys[elementCount] : set(connectingSet[0])})
    
    pyramid.update({keys[elementCount] : set(connectingSet[0])})
    
    elementCount += 1

    if incrementRow == True:
        currentRow += 1
        bottomIncrement -= 1

#print(pyramid)

######pyramid = {'A' : set(['B','C'])}
######pyramid.update({'B' : set(['A','D','E'])})
######pyramid.update({'C' : set(['A','E','F'])})
######pyramid.update({'D' : set(['B','G'])})
######pyramid.update({'E' : set(['B','C','H','G'])})
######pyramid.update({'F' : set(['C','H'])})
######pyramid.update({'G' : set(['D','E','I'])})
######pyramid.update({'H' : set(['E','F','I'])})
######pyramid.update({'I' : set(['H','G'])})
######
##lastItem = keys[lastItemList[len(lastItemList)-1]]

finalList = []
finalList = list(dfs_paths(pyramid,'A',lastItem))
    
print(len(finalList))

