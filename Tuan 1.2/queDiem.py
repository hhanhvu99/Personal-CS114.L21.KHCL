n = int(input())
listOfInput = []

for i in range(n):
	a = int(input())
	listOfInput.append(a)

for number in listOfInput:
	queDiemCanThem = 0
	if number == 2:
		queDiemCanThem = 2
	elif number % 2 == 0:
		queDiemCanThem = 0
	else:
		queDiemCanThem = 1

	print(queDiemCanThem)