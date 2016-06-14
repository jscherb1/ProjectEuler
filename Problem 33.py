origNum = []
origDenom = []
ResultsDenom = []
ResultsNum = []

for numerator in range(10,100):
    for denominator in range (10,100):
        if numerator != denominator and numerator < denominator:
            numDigits = list(str(numerator))
            denomDigits = list(str(denominator))
            #print(numDigits, " / ", denomDigits)
            origFraction = numerator/denominator
            #print(origFraction)
            tempResultsNum = []
            tempResultsDenom = []

            fracResults = []
            numResults = 0
            for numIdx in range(0,len(numDigits)):
                for denomIdx in range(0,len(denomDigits)):
                    if numDigits[numIdx] == denomDigits[denomIdx] and numDigits[numIdx] != '0':
                        #the numerator digit is in the denominator
                        #remove the digits to create a new fraction
                        tempResultsDenom.append(denomDigits[abs(1-denomIdx)])
                        tempResultsNum.append(numDigits[abs(1-numIdx)])
                        numResults = numResults + 1
                        if denomDigits[abs(1-denomIdx)] != '0':
                            tempResultsFrac = (ord(numDigits[abs(1-numIdx)])-48)/(ord(denomDigits[abs(1-denomIdx)])-48)
                            #print(numDigits[abs(1-numIdx)], " = ",(ord(numDigits[abs(1-numIdx)]))-48)
                        else:
                            tempResultsFrac = 0.0

                        fracResults.append(tempResultsFrac)
                        #print(tempResultsFrac)
                        #print(tempResultsNum, ";", tempResultsDenom)

                        if tempResultsFrac == origFraction:
                            ResultsDenom.append(denomDigits[abs(1-denomIdx)])
                            ResultsNum.append(numDigits[abs(1-numIdx)])
                            origNum.append(numerator)
                            origDenom.append(denominator)
                        
print("Original Numerator", origNum)
print("Results Numerators: ", ResultsNum)
print("Original Denominator", origDenom)
print("Results Denominators: ", ResultsDenom)
