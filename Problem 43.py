import itertools

def combine_integers(numList):
    s = ''.join(map(str, numList))
    return int(s)

def is_pandigital(number):
    returnVal = True
    numberList = list(str(number))
    #print(numberList)
    for num in range(0,10):
        #print(num)
        if str(num) not in numberList:
            returnVal = False
            break
    return returnVal

#####generate list of all pandigital numbers
####numList = list(itertools.permutations([1,2,3,4,5,6,7,8,9,0])) #itertools.permutations([1,2,3,4,5,6,7,8,9])
####print(numList)
####
####
####panDigitalList = []
####for index in range(0,len(numList)):
####    panDigitalList.append(combine_integers(numList[index]))
####
####print(panDigitalList)
#strNum = str(123456)
#print(combine_integers(strNum[1:3]))
resultSum = 0

numList = list(itertools.permutations([1,2,3,4,5,6,7,8,9,0]))
for item in numList:
    num = combine_integers(item)
#for num in range(1000000000,9999999999): #range(1406357289,1406357289+1):#
    if is_pandigital(num):
        strNum = str(num)
        if combine_integers(strNum[1:4])%2 == 0:
            if combine_integers(strNum[2:5])%3 == 0:
                if combine_integers(strNum[3:6])%5 == 0:
                    if combine_integers(strNum[4:7])%7 == 0:
                        if combine_integers(strNum[5:8])%11 == 0:
                            if combine_integers(strNum[6:9])%13 == 0:
                                if combine_integers(strNum[7:10])%17 == 0:
                                     print(num)
                                     resultSum = resultSum + num
print(resultSum)
            
