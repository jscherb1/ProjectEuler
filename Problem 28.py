x=1
y=0
counter = 1
diagonalSum = 1

directionFlag = 'Down'

maxVal = 500

while x<=maxVal and y<=maxVal:
    counter = counter+1
    if abs(x)==abs(y) and x>0 and y>0:
        #is diagonal (top right corner)
        #move right
        #print('diagonal top right;',' x = ',x,'; y = ',y,'Num = ',counter)
        x=x+1
        diagonalSum = diagonalSum + counter
        directionFlag = 'Down'
        
    elif abs(x)==abs(y) and x<0 and y >0:
        #is diagonal (top left corner)
        #move right
        #print('diagonal top left;',' x = ',x,'; y = ',y,'Num = ',counter)
        x=x+1
        diagonalSum = diagonalSum + counter
        directionFlag = 'Right'
        
    elif abs(x)==abs(y) and x>0 and y<0:
        #is diagonal (bottom right corner)
        #move left
        #print('diagonal bottom right;',' x = ',x,'; y = ',y,'Num = ',counter)
        x=x-1
        diagonalSum = diagonalSum + counter
        directionFlag = 'Left'
        
    elif abs(x)==abs(y) and x<0 and y<0:
        #is diagonal (bottom left corner)
        #move up
        #print('diagonal bottom left;',' x = ',x,'; y = ',y,'Num = ',counter)
        y=y+1
        diagonalSum = diagonalSum + counter
        directionFlag = 'Up'
    else:
        #not diagonal, need to figure out where to move
        #print('not diaganol', 'move = ',directionFlag,' x = ',x,'; y = ',y,'Num = ',counter)
        if directionFlag == 'Down':
            y=y-1
        elif directionFlag == 'Left':
            x=x-1
        elif directionFlag == 'Right':
            x=x+1
        else:
            #direction = 'Up'
            y=y+1
    #print('x = ',x,'y = ',y)
    #print('counter = ',counter)
    
print(diagonalSum)
