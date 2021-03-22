currentIndex = 0
middleIndex = 12

for i in range(5):
	data = input().split()
	found = False

	for index, value in enumerate(data):
		if value == '1':
			currentIndex += index
			found = True

	if found:
		break

	currentIndex += 5

different = abs(currentIndex - middleIndex)

rowMove = different // 5
columnMove = different % 5

if columnMove == 4:
	columnMove -= 2

print(rowMove + columnMove)
