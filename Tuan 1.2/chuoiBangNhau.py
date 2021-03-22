n = int(input())
listOfInput = []

for i in range(n):
	chuoiMot = input()
	chuoiHai = input()
	listOfInput.append((chuoiMot, chuoiHai))

for element in listOfInput:
	chuoiMot = element[0]
	chuoiHai = element[1]

	intersect = set(chuoiMot).intersection(chuoiHai)

	if len(intersect) != 0:
		print('YES')
	else:
		print('NO')