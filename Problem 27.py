import functions_jas

maxConsecPrimes = 0
maxAorBVal = 1000
startVal = -1000
a = startVal
b = startVal
n = 0
while a <= maxAorBVal:
    n = 0
    consecPrimeCount = 0
    while b <= maxAorBVal:
        num = n*n + a*n + b
        if(functions_jas.is_prime(num)):
            consecPrimeCount += 1
            n += 1
        else:
            if consecPrimeCount > maxConsecPrimes:
                maxConsecPrimes = consecPrimeCount
                maxA = a
                maxB = b

            n = 0
            b+=1
            consecPrimeCount = 0
    a += 1
    b = startVal

print("max consecutive primes = ", maxConsecPrimes)
print("Max A: ", maxA)
print("Max B: ", maxB)
print("A and B product = ", maxA*maxB)
