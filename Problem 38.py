
def is_pandigital(number):
    returnVal = True
    numberList = list(str(number))
    #print(numberList)
    for num in range(1,10):
        #print(num)
        if str(num) not in numberList:
            returnVal = False
            break
    return returnVal

def combine_integers(numList):
    s = ''.join(map(str, numList))
    return int(s)

maxNumber = 0
number = 8
resultArray = []
tempResults = []

while number < 1000000000/2:
    #loop through every number until the
    #number multiplied by 2 is a 10 digit number

    #multiply by integers until a 9 digit number is created
    numDigits = len(str(number))
    multiplier = 2
    tempResults = []
    tempResults.append(number)
    while numDigits < 9:
        tempResults.append(number*multiplier)
        numDigits = numDigits + len(str(tempResults[multiplier-1]))

        multiplier = multiplier + 1

    concatenatedNum = combine_integers(tempResults)
    if len(str(concatenatedNum)) == 9 and is_pandigital(concatenatedNum):
        #nine digit pandigital number
        if concatenatedNum >= maxNumber:
            maxNumber = concatenatedNum
            resultArray = tempResults

    #move to the next number
    number = number+1

print(maxNumber)
print(resultArray)
