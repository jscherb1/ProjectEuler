#1-9
oneThroughNine = 36
#10-19
tenThroughNineteen = 70
#20-29
twentyThru29 = (len('twenty')*10)+ oneThroughNine
#30-39
thirtyThru39= (len('thirty')*10)+ oneThroughNine
#40-49
fortyThru49 = (len('forty')*10)+ oneThroughNine
#50-59
fiftyThru59 = (len('fifty')*10)+ oneThroughNine
#60-69
sixtyThru69 = (len('sixty')*10)+ oneThroughNine
#70-79
seventyThru79 = (len('seventy')*10)+ oneThroughNine
#80-89
eightyThru89 = (len('eighty')*10)+ oneThroughNine
#90-99
ninetyThru99 = (len('ninety')*10)+ oneThroughNine

#under 100 total for reuse
under100Total = oneThroughNine+tenThroughNineteen+twentyThru29+thirtyThru39+fortyThru49+fiftyThru59+sixtyThru69+seventyThru79+eightyThru89+ninetyThru99
#100-199
oneHundredThru199 = (len('onehundredand')*99)+under100Total+len('onehundred')
#200-299
twoHundredThru299 = (len('twohundredand')*99)+under100Total+len('twohundred')
#300-399
threeHundredThru399 = (len('threehundredand')*99)+under100Total+len('threehundred')
#400-499
fourHundredThru499 = (len('fourhundredand')*99)+under100Total+len('fourhundred')
#500-599
fiveHundredThru599 = (len('fivehundredand')*99)+under100Total+len('fivehundred')
#600-699
sixHundredThru699 = (len('sixhundredand')*99)+under100Total+len('sixhundred')
#700-799
sevenHundredThru799 = (len('sevenhundredand')*99)+under100Total+len('sevenhundred')
#800-899
eightHundredThru899 = (len('eighthundredand')*99)+under100Total+len('eighthundred')
#900-999
nineHundredThru999 = (len('ninehundredand')*99)+under100Total+len('ninehundred')

oneHundredThrough999 = oneHundredThru199+twoHundredThru299+threeHundredThru399+fourHundredThru499+ \
                        fiveHundredThru599+sixHundredThru699+sevenHundredThru799+eightHundredThru899+nineHundredThru999

#1000
oneThousand = len('onethousand')

total = under100Total + oneHundredThrough999 + oneThousand

print(total)
