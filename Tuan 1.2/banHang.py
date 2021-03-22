n = int(input())
listOfInput = []

for i in range(n):
	number = int(input())
	listNum = input().split()
	for index, a in enumerate(listNum):
		listNum[index] = int(a)
	listOfInput.append([number, listNum])

for input in listOfInput:
	number = input[0]
	listNum = input[1]

	total = sum(listNum)

	if total % number != 0:
		print(total//number + 1)
	else:
		print(total//number)

