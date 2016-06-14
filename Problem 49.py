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

def list_duplicates(seq):
    seen = []
    idxList = []
    for index in range(0,len(seq)):
        if seq[index] in seen:
            #duplicate item
            #loop through sequence to get index of original item
            for index2 in range(0,len(seen)):
                if seen[index2] == seq[index]:
                    idxList.append(index2)
                    
            idxList.append(index)
        else:
            #first time
            seen.append(seq[index])
    return idxList
                     
maxVal = 9999
resultsList = []
digitsList = []
permutationsList = []
primeList = []
primeCounter = 1
for number in range(1487,maxVal):
    primesList = []
    resultsList = []
    if is_prime(number):
        #print('prime number: ',number)
        #primeList.append(number)
        digitsList = str(number)
        permutationsList = list(set(itertools.permutations(digitsList)))
        #print(permutationsList)
        primecounter = 1
        primesList.append(number)
        for index in range(0,len(permutationsList)):
            numToTest = combine_integers(permutationsList[index])
            if is_prime(numToTest):
                primecounter = primecounter + 1
                primesList.append(numToTest)
                #print(numToTest, 'is prime', primecounter)

        primesList = list(set(primesList))
        #print(primesList)
        if primecounter >= 3:
            resultsList = []
            for index1 in range(0,len(primesList)):
                differenceList = []
                for index2 in range(0,len(primesList)):
                    #print(abs(primesList[index2]-primesList[index1]))
                    differenceList.append(abs(primesList[index2]-primesList[index1]))
            #check for duplicates in list
                duplicateIndices = list_duplicates(differenceList)
                if len(duplicateIndices) > 0:
                    resultsList.append(primesList[index1])
                    for loopIdx in range(0,len(duplicateIndices)):
                        resultsList.append(primesList[duplicateIndices[loopIdx]])
            if len(resultsList)>0:            
                print(resultsList)
