from collections import Counter

found = False
number = 138366 #125874
numberMult = 6
while found == False:
    numberList = []
    numberList.append(number)
    for idx in range(2,numberMult+1):
        numberList.append(number*idx)

    #print(numberList)
    #numberList = [number, number2x] #, number3x, number4x, number5x, number6x]
    #numberListStr = [str(number), str(number2x), str(number3x), str(number4x), str(number5x), str(number6x)]
    #print(list(str(numberList[1])))
    found = False
    for index1 in range(0,len(numberList)):
        for index2 in range(0,len(numberList)):
            if index1 != index2:
                #print(len(str(numberList[index1])), len(str(numberList[index2])))
                if len(str(numberList[index1])) == len(str(numberList[index2])):
                    found = True
                    #Same number of digits
                    #print(list(str(numberList[index1])),list(str(numberList[index2])))
                    differences = Counter(list(str(numberList[index1]))) - Counter(list(str(numberList[index2])))
                    diffList = list(differences.elements())
                    #differences = list(set(str(numberList[index1]))-set(str(numberList[index2])))
                    if len(diffList) != 0:
                        #different numbers,
                        found = False

    if found == True:
        print(differences.elements())
        print(numberList)
        print(number)
    else:
        number = number + 1
