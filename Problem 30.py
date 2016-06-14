totalSum = 0

for num in range(2, 1000000):
    stringNum = str(num)
    tempSum = 0
    for digit in stringNum:
        iDigit = int(digit)
        tempSum += iDigit*iDigit*iDigit*iDigit*iDigit

    if tempSum == num:
        print(num)
        totalSum += tempSum
        
print(totalSum)
