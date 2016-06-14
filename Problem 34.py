import math

totalSum = 0
done = 0

factorialList = [0,1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

number = 10

while number <= 1000000:
    stringNum = str(number)
    numberSum = 0
    for index in range(0,len(stringNum)):
        #print(stringNum[index])
        numberSum += math.factorial(int(stringNum[index]))
        #print(numberSum)

        if numberSum == number:
            print(number)
            totalSum += number
            print(totalSum)
            
    number += 1

print(totalSum)
