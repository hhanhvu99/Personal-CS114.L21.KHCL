from sys import stdin

row, column = input().split()
row = int(row)
column = int(column)
length = row * column

listOfInput = []
maxLenList = []

for i in range(row):
	temp = stdin.readline().split()

	for index, element in enumerate(temp):
		if element[0] == '0':
			temp[index] = str(int(element))
		elif element[0] == '-' and element[1] == '0':
			temp[index] = str(int(element))

	listOfInput += temp


for currentCol in range(column):
	maxLen = -1

	for j in range(currentCol, length, column):
		if len(listOfInput[j]) > maxLen:
			maxLen = len(listOfInput[j])

	maxLenList.append(maxLen)

formatString = ''
tempLength = len(maxLenList)
for index, maxLen in enumerate(maxLenList):
	if index < tempLength - 1:
		formatString += '{:>' + str(maxLen) + 's} '
	else:
		formatString += '{:>' + str(maxLen) + 's}\n'

currentIndex = 0
for i in range(row):
	newList = listOfInput[currentIndex:currentIndex+column]
	print(formatString.format(*newList), end='')

	currentIndex += column

