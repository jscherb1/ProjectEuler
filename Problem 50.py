import functions_jas

primeList = []
maxPrime = 1000000
for item in range(1,maxPrime):
    if functions_jas.is_prime(item):
        primeList.append(item)

print("Generated Prime List.. moving to finding number")
distanceLoopDone = False
startDistance = 2
distance = startDistance
maxDistance = 1
maxPrimeList = []
##while done == False:

#loop through the list of primes
for prime in primeList:
    #print("Prime Numeber: ",prime)
    start = 0
    end = distance + start
    incrementDistanceLoopDone = False
    while incrementDistanceLoopDone == False:
        #print("distance: ", distance)
        distanceLoopDone = False
        distanceIncrementCount = 0
        while distanceLoopDone == False:
            #print(primeList[start:end])
            #loop through the prime list at a fixed distance
            if prime == sum(primeList[start:end]) and distance > maxDistance:
                resultPrime = prime
                maxDistance = distance
                maxPrimeList = primeList[start:end]

            if sum(primeList[start:end]) >= prime:
                #print("distance loop done")
                distanceLoopDone= True
            else:
                start += 1
                end = distance + start
                distanceIncrementCount += 1

        if distanceIncrementCount == 0:
            #segment is too large
            #quit incrementing the distance
            #print("Get new prime")
            incrementDistanceLoopDone = True
            distance = maxDistance
        else:
            distance += 1
            start = 0
            end = start+ distance
print("Max Prime: ",resultPrime)
print("Number of primes: ", maxDistance)
print("Prime List: ", maxPrimeList)
