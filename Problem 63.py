resultsList = []
baseList = []
powerList = []
for base in range(2,10):
    for power in range (2,10000000):
        number = base**power
        numDigits = len(str(number))
        if numDigits == power:
            lastDigit = round(((number/10)-int((number/10)))*10)
            if lastDigit == base:
                resultsList.append(number)
                baseList.append(base)
                powerList.append(power)

print(resultsList)
print(baseList)
print(powerList)
print(len(resultsList))
