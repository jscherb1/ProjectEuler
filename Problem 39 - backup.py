import math

def isint(num):
    if num == int(num):
        return True
    else:
        return False

maxPval = 1001

maxSolutions = 0
solutionCount = 0
resultPVal = 0
solutionSet = []
for p in range (120,121):#(560,maxPval):
    print(p)
    solutionCount = 0
    tempSolutionSet = []
    continueA = True
    a = 1
    
    while continueA == True:
        b=1
        continueB = True
        
        while continueB == True:
            c=p-(b+a)
            print(a,b,c)
            if c > 0:
                if (a*a+b*b) == c*c:
                    #right triangle
                    solutionCount = solutionCount + 1
                    sideList = [a,b,c]
                    tempSolutionSet.append(sideList)
                    
                if ((b+1)+a+(p-((b+1)+a)))>p:
                    #test if next iteration of a,b,c > p
                    continueB = False
                else:
                    while (not isint(math.sqrt(a*a+b*b))) and continueB == True:
                        b = b + 1
                        if ((b)+a+(p-((b)+a)))>p:
                            continueB = False
            else:
                continueB = False
                
        if ((a+1)+1+(p-((a+1)+b)))>p:
            #test if next iteration of a,b,c > p
            continueA = False
        else:
            a = a+1

    if solutionCount > maxSolutions:
        resultPVal = p
        maxSolutions = solutionCount
        solutionSet = tempSolutionSet
print(resultPVal, maxSolutions/2, solutionSet)
