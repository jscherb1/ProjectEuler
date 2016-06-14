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

number = 8
primeCounter = 0
resultsList = []
while primeCounter < 11:
    if is_prime(number):
        #prime number
        ##print(number, 'is a prime')
        truncatable = 'true'
        numberOfDigits = len(str(number))
        ##print(numberOfDigits)
        #testNumber = number
        for loopIndex in range(1,numberOfDigits):
            #get truncated right number
            truncRight = round((number/(10**loopIndex)-int(number/(10**loopIndex)))*(10**loopIndex))
            #get truncated left number
            truncLeft = int(number/(10**loopIndex))
            #print('TR:',truncRight,is_prime(truncRight), 'TL:',truncLeft,is_prime(truncLeft))
            if not (is_prime(truncRight) and is_prime(truncLeft)):
                truncatable = 'false'
        if truncatable == 'true':
            #number is truncatable - add it to the list
            resultsList.append(number)
            primeCounter = primeCounter + 1
            ##print(number)
    number = number + 1
    
print(sum(resultsList))
