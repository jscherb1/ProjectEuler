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

def is_pandigital(number,numDigits):
    digitsList = []
    numberList = list(str(number))
    for count in range (1,numDigits+1):
        digitsList.append(str(count))
        
    #check if number contains list all digits
    result = list(set(digitsList)-set(numberList))
    #print(result)
    
    if len(result) == 0:
        return True
    else:
        return False

maxNumber = 999999999
number = 7652413
maxPandigital = 2143
while number <= maxNumber:
    if is_prime(number):
        if is_pandigital(number, len(str(number))):
            if number >= maxPandigital:
                maxPandigital = number
                print(maxPandigital)
    number = number+1
