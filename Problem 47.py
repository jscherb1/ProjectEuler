from collections import defaultdict
from math import sqrt

def divisorGenerator(n):
    returnList = []
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            returnList.append(i)
    return(returnList) 

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

def factor(n):
    i = 2
    limit = sqrt(n)    
    while i <= limit:
      if n % i == 0:
        yield i
        n = n / i
        limit = sqrt(n)   
      else:
        i += 1
    if n > 1:
        yield n
        
def distinctPrimeGen(num):
    d=defaultdict(int)
    for f in factor(num):
        d[f]+=1

    terms=[]
    base = sorted(d.keys())
    for e in base:
        if e>1:
            terms.append(e**d[e])
    return terms

done = False
number = 2
consecutiveCount = 0
maxConsecutive = 4
numberList = []

while done == False:
####    factorList = divisorGenerator(number)
####    #print(factorList)
####    primefactors = []
####    for item in factorList:
####        if is_prime(item):
####            primefactors.append(item)
####    #print(primefactors)
    primefactors = []
    primefactors = distinctPrimeGen(number)
    
    if len(primefactors) == maxConsecutive:
        product = 1
        for item in primefactors:
            product *= item
        #print(product)

        if product == number:
            consecutiveCount += 1
            numberList.append(number)
        else:
            consecutiveCount = 0
            numberList = []
    else:
        consecutiveCount = 0
        numberList = []
    if consecutiveCount == maxConsecutive:
        done = True
        print(numberList)
    number += 1

##while done == False:
##    divisorList = divisorGenerator(number)
##    for item in divisorList:
##        if is_prime(item):
