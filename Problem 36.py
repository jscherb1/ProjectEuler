def is_palandrome_base2_base10(num):
    decNum = num
    binNum = bin(num)
    #print(binNum,len(str(decNum))%2)
    returnVal = True

    #Check base 10
    #print('Checking base 10')
    listDecNum = list(str(decNum))
    #print(listDecNum)
    for index in range(0,int(len(listDecNum)/2)):
        #print((len(listDecNum)-index)-1)
        if listDecNum[index] != listDecNum[(len(listDecNum)-index)-1]:
            returnVal = False

    #print('Checking binary')
    #check binary
    #strip off '0b' part
    listBinNum = list(binNum[2:len(binNum)])
    for index in range(0,int(len(listBinNum)/2)):
        if listBinNum[index] != listBinNum[(len(listBinNum)-index)-1]:
            returnVal = False

    return returnVal
number = 1
maxValue = 1000000
resultSum = 0

while number < maxValue:
    
    if is_palandrome_base2_base10(number):
            resultSum = resultSum + number

    number = number + 1
    
print(resultSum)
