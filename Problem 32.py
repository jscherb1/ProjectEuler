def combine_integers(numList):
    s = ''.join(map(str, numList))
    return int(s)

def is_pandigital(number, pandigitalLength):
    returnVal = True
    numberList = list(str(number))
    #print(numberList)
    for num in range(1,pandigitalLength+1):
        #print(num)
        if str(num) not in numberList:
            returnVal = False
            break
    return returnVal

resultSum = 0
done = False
num1 = 1
num2 = 1
productList = []
for num1 in range (1, 10000):
    #print(num1)
    for num2 in range (1, 10000):
            product = num1*num2
            if len(str(num1))+len(str(num2))+len(str(product)) == 9:
                #9 digits
                numberList = [num1, num2, product]
                if is_pandigital(combine_integers(numberList),9):
                    if product not in productList:
                        resultSum = resultSum + product
                        productList.append(product)
            
print(resultSum)
