import itertools
import functions_jas
numbers = []

index = 1000000

numList = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
for item in numList:
    numbers.append(functions_jas.combine_integers(item))

print("sorting list")
#sortedNumbers = numbers.sort()
print(numbers[index-1])
