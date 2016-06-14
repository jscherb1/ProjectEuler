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
        'DI','DJ','DK','DL','DM','DN','DO','DP']


##graph = {'A': set(['B','C']),\
##         'B': set(['A','D','E']),\
##         'C': set(['A','E','F']),\
##         'D': set(['B','G','H']),\
##         'E': set(['B','C','H','I']),\
##         'F': set(['C','I','J']),\
##         'G': set(['D']),\
##         'H': set(['D','E']),\
##         'I': set(['E','F']),\
##         'J': set(['F'])}

graph = {'A': set(['B','C']),\
         'B': set(['A','D','E']),\
         'C': set(['A','E','F']),\
         'D': set(['B','G','H']),\
         'E': set(['B','C','H','I']),\
         'F': set(['C','I','J']),\
         'G': set(['D','K','L']),\
         'H': set(['D','E','L','M']),\
         'I': set(['E','F','M','N']),\
         'J': set(['F','N','O']),\
         'K': set(['G','P','Q']),\
         'L': set(['G','H','Q','R']),

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])
        
paths = []
bottomRow = ['G','H','I','J']
numRows = 4
for item in bottomRow:
    tempPaths = list(dfs_paths(graph,'A',item))
    for idx in range(0,len(tempPaths)):
        paths.append(tempPaths[idx])
    
#paths = list(dfs_paths(graph, 'A', 'H'))
#print(paths)
#filter out all paths that go up in tree
finalList = []
for idx in range(0,len(paths)):
    if len(paths[idx]) <= numRows:
        finalList.append(paths[idx])

print(finalList)

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
        'DI','DJ','DK','DL','DM','DN','DO','DP']
values = [3, 7, 4,2,4,6,8,5,9,3]
##values = [75,95,64,17,47,82,18,35,87,10,20,4,82,47,65,\
##          19,1,23,75,3,34,88,2,77,73,7,63,67,\
##          99,65,4,28,6,16,70,92,\
##          41,41,26,56,83,40,80,70,33,\
##          41,48,72,33,47,32,37,16,94,29,\
##          53,71,44,65,25,43,91,52,97,51,14,\
##          70,11,33,28,77,73,17,78,39,68,17,57,\
##          91,71,52,38,17,14,91,43,58,50,27,29,48,\
##          63,66,4,68,89,53,67,30,73,16,69,87,40,31,\
##          4,62,998,27,23,9,70,98,73,93,38,53,60,4,23]

pathSum = []
for item in finalList:
    tempSum = 0
    for value in item:
        tempSum += values[keys.index(value)]
    pathSum.append(tempSum)

print(pathSum)
print(max(pathSum), finalList[pathSum.index(max(pathSum))])
