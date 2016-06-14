import csv
with open('p042_words.txt') as f:
    reader = csv.reader(f, delimiter=",")
    d = list(reader)

wordList = list(d[0])

maxWordLength = len(max(wordList, key=len))
maxWordVal = maxWordLength*26

triangleTermList = []
n = 1
triangleTerm = 0
while triangleTerm <= maxWordVal:
    triangleTerm = int(.5*n*(n+1))
    triangleTermList.append(triangleTerm)

    n=n+1
    
#print(triangleTermList)
count = 0
resultScoreList = []
resultWordList = []
for index in range(0,len(wordList)):
    word = list(wordList[index])
    #print(word)
    wordScore = 0
    for letterIndex in range(0,len(word)):
        wordScore = wordScore + (ord(word[letterIndex])-64)

    if wordScore in triangleTermList:
        count = count + 1
        resultScoreList.append(wordScore)
        resultWordList.append(wordList[index])

print(count)
print(resultScoreList)
print(resultWordList)
