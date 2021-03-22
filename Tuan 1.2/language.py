listOfTu = input().split()

'''
Tính từ nam: -lios
Tính từ nữ: -liala
Danh từ nam: -etr
Danh từ nữ: -etra
Động từ nam: -initis
Động từ nữ: -inites

Tính từ: adj
Danh từ: noun
Động từ: verb

Nam: 0
Nữ: 1

Phần tử trong list: (từ, độ dài, từ loại, giới tính)

return (Từ loại, giới tính)
'''

listOfTuLoai = [('lios', 4, 10, 0), ('liala', 5, 10, 1),
				('etr', 3, 20, 0), ('etra', 4, 20, 1),
				('initis', 6, 30, 0), ('inites', 6, 30, 1)]

def xacDinhTuLoai(word, listOfTuLoai):
	for rule in listOfTuLoai:
		temp = word
		length = rule[1]
		temp = temp[-length:]

		if temp == rule[0]:
			return (rule[2], rule[3])

	return None

def exitModified():
	print('NO')
	exit()


if len(listOfTu) == 1:
	result = xacDinhTuLoai(listOfTu[0], listOfTuLoai)

	if result != None:
		print('YES')
	else:
		print('NO')

else:
	listOfResult = []

	for word in listOfTu:
		result = xacDinhTuLoai(word, listOfTuLoai)

		if result == None:
			exitModified()

		listOfResult.append(result)

	foundNoun = False
	currentTuLoai = 10
	currentGioiTinh = 0

	for ketQua in listOfResult:
		if ketQua[0] == 30 and foundNoun == False:
			exitModified()
		if ketQua[0] > currentTuLoai:
			currentTuLoai = ketQua[0]
		if ketQua[0] < currentTuLoai:
			exitModified()
		if ketQua[0] == 20:
			if foundNoun:
				exitModified()
			else:
				currentTuLoai = ketQua[0]
				foundNoun = True

		currentGioiTinh += ketQua[1]

	if currentGioiTinh == 0 or currentGioiTinh == len(listOfResult):
		print('YES')
	else:
		print('NO')



