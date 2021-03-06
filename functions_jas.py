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

def is_pandigital(number):
    returnVal = True
    numberList = list(str(number))
    #print(numberList)
    for num in range(0,10):
        #print(num)
        if str(num) not in numberList:
            returnVal = False
            break
    return returnVal