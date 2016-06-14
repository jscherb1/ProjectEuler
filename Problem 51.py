import itertools

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def combine_integers(numList):
    s = ''.join(map(str, numList))
    return int(s)


eightPrimeNumFound = False
goalNumOfPrimes = 7
testNum = 55000
#while loop to increment number until eight prime value family is found
while eightPrimeNumFound == False:
    if is_prime(testNum):
        numDigits = len(str(testNum))
        testNumStr = list(str(testNum))
        #print(testNumStr)
        #loop through all combinations of digits to replace
        for index1 in range(0,numDigits):
            resultsList = []
            for index2 in range(0,numDigits):
                primesFound = 0
                testNumStr = list(str(testNum))
                newTestNumStr = testNumStr
                resultsList = []
                #print(newTestNumStr)
                if index1 != index2:
                    #replace this combination of digits with a digit
                    for digit in range(0,10):
                        newTestNumStr[index1] = str(digit)
                        newTestNumStr[index2] = str(digit)
                        #print(newTestNumStr)
                        newTestNumber = combine_integers(newTestNumStr)
                        if is_prime(newTestNumber):
                            primesFound = primesFound + 1
                            resultsList.append(newTestNumber)
                            #print('prime found: ',primesFound,newTestNumber)
                #print(primesFound)
            #if len(resultsList)>0:
                #print(resultsList)       
                if primesFound == goalNumOfPrimes:
                    eightPrimeNumFound = True
                    print(resultsList)
                    break

    testNum = testNum + 1
