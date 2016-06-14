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

def get_circular_numbers(num):
  returnList = []
  returnList.append(num)
  numDigits = len(str(num))
  digitList = list(str(num))
  #print(digitList)
  for digitIndex in range(1,numDigits):
    rotNum = digitList[digitIndex:numDigits]+digitList[0:digitIndex]
    #print(rotNum)
    returnList.append(combine_integers(rotNum))
  return returnList

maxVal = 1000000
resultsList = []
digitsList = []
circularList = []
primeList = []
allPrimes = 'true'
for number in range(1,maxVal):
    if is_prime(number):
        #print('prime number: ',number)
        #primeList.append(number)
        circularList= get_circular_numbers(number)
        #print (circularList)
          
        allPrimes = 'true'
        for index in range(0,len(circularList)):
            numToTest = circularList[index]
            if not is_prime(numToTest):
                allPrimes = 'false'
        if allPrimes == 'true':
            resultsList.append(number)
            
print(len(resultsList))

