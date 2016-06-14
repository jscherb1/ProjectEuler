from math import sqrt
import functions_jas

#Generate a list of odd composite numbers
#odd numbers that are not prime
compositeOdds = []
primeList = []

maxPrime = 100
for item in range(1,maxPrime):
    if functions_jas.is_prime(item):
        primeList.append(item)
    elif item%2 != 0:
        #odd
        compositeOdds.append(item)

done = False
number = 1

while done == False:
    for number in compositeOdds:
        solutionFound = False
        maxPrimeIndex = next(x[0] for x in enumerate(primeList) if x[1] > number)
        for prime in primeList[0:maxPrimeIndex]:
            for square in range(1,int(sqrt(number)/2)+2):
                print("Composite Number = ", number," Prime = ", prime, "; Square = ", square)

                if number == (prime + 2*square**2):
                    print("Solution Found!")
                    solutionFound = True
                    break
    
    if solutionFound == False:
        done = True

print(number)
