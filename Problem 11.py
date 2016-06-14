with open('problem 11.txt') as f:
    masterArray = []
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            masterArray.append(line)

print (masterArray[0][0])

maxCol = 19
maxRow = 19


tempMax = 0

for row in range(0,maxRow+1):
    for col in range(0,maxCol+1):
        up = 0
        right = 0
        down = 0
        left = 0
        diagUpLeft = 0
        diagUpRight = 0
        diagDownRight = 0
        diagDownLeft = 0

        resultsArray = [0,0,0,0,0,0,0,0]
        #print (row,col)
        if row == 6 and col == 8:
            blah = 1
    
        
        if row >= 3:
            #calculate up
            resultsArray[0] = masterArray[row][col]*masterArray[row-1][col]*masterArray[row-2][col]*masterArray[row-3][col]
        if maxCol - col >= 3:
            #calculate right
            resultsArray[1] = masterArray[row][col]*masterArray[row][col+1]*masterArray[row][col+2]*masterArray[row][col+3]
        if maxRow - row >= 3:
            #calculate down
            resultsArray[2] = masterArray[row][col]*masterArray[row+1][col]*masterArray[row+2][col]*masterArray[row+3][col]
        if col >= 3:
            #calculate left
            resultsArray[3] = masterArray[row][col]*masterArray[row][col-1]*masterArray[row][col-2]*masterArray[row][col-3]
        if col >=3 and row >= 3:
            #calculate diagUpLeft
            resultsArray[4] = masterArray[row][col]*masterArray[row-1][col-1]*masterArray[row-2][col-2]*masterArray[row-3][col-3]
        if col >=3 and maxRow - row >= 3:
            #calculate diagDownLeft
            resultsArray[5] = masterArray[row][col]*masterArray[row+1][col-1]*masterArray[row+2][col-2]*masterArray[row+3][col-3]
        if maxCol - col >= 3 and row >= 3:
            #caclulate diagUpRight
            resultsArray[6] = masterArray[row][col]*masterArray[row-1][col+1]*masterArray[row-2][col+2]*masterArray[row-3][col+3]
        if maxCol - col >= 3 and maxRow - row >= 3:
            #calculate diagDownRight
            resultsArray[7] = masterArray[row][col]*masterArray[row+1][col+1]*masterArray[row+2][col+2]*masterArray[row+3][col+3]

        if max(resultsArray) > tempMax:
            tempMax = max(resultsArray)
            tempMaxRow = row
            tempMaxCol = col
        #print (resultsArray)
        
print (tempMax, tempMaxRow, tempMaxCol)
