mauMat = input().split()
loiGiaiGoc = input().split()

listOfMat = []

for i in range(4):
	listString = [mauMat[i]] * 9
	listOfMat.append(listString)

def originalRubik(listOfMat, loiGiaiGoc):
	top, bottom, left, right = 0, 1, 2, 3

	for loiGiai in reversed(loiGiaiGoc):
		if loiGiai[0].isupper():
			numberToRotate = 1
		else:
			numberToRotate = 2

		if loiGiai[0].lower() == "u":
			anchor = top
			anchorLeft = left
			anchorRight = right
		elif loiGiai[0].lower() == "b":
			anchor = bottom
			anchorLeft = right
			anchorRight = left
		elif loiGiai[0].lower() == "l":
			anchor = left
			anchorLeft = top
			anchorRight = bottom
		else:
			anchor = right
			anchorLeft = bottom
			anchorRight = top

		if loiGiai[-1] == "'":
			if numberToRotate == 1:
				temp = listOfMat[anchor][0]
				listOfMat[anchor][0] = listOfMat[anchorLeft][4]
				listOfMat[anchorLeft][4] = listOfMat[anchorRight][8]
				listOfMat[anchorRight][8] = temp
			else:
				'''Xoay đỉnh'''
				temp = listOfMat[anchor][0]
				listOfMat[anchor][0] = listOfMat[anchorLeft][4]
				listOfMat[anchorLeft][4] = listOfMat[anchorRight][8]
				listOfMat[anchorRight][8] = temp

				'''Xoay cạnh giữa'''
				first, second, third = listOfMat[anchor][1], listOfMat[anchor][2], listOfMat[anchor][3]
				listOfMat[anchor][1], listOfMat[anchor][2], listOfMat[anchor][3] = listOfMat[anchorLeft][6], listOfMat[anchorLeft][5], listOfMat[anchorLeft][1]
				listOfMat[anchorLeft][6], listOfMat[anchorLeft][5], listOfMat[anchorLeft][1] = listOfMat[anchorRight][3], listOfMat[anchorRight][7], listOfMat[anchorRight][6]
				listOfMat[anchorRight][3], listOfMat[anchorRight][7], listOfMat[anchorRight][6] = first, second, third

		else:
			if numberToRotate == 1:
				temp = listOfMat[anchor][0]
				listOfMat[anchor][0] = listOfMat[anchorRight][8]
				listOfMat[anchorRight][8] = listOfMat[anchorLeft][4]
				listOfMat[anchorLeft][4] = temp
			else:
				'''Xoay đỉnh'''
				temp = listOfMat[anchor][0]
				listOfMat[anchor][0] = listOfMat[anchorRight][8]
				listOfMat[anchorRight][8] = listOfMat[anchorLeft][4]
				listOfMat[anchorLeft][4] = temp

				'''Xoay cạnh giữa'''
				first, second, third = listOfMat[anchor][1], listOfMat[anchor][2], listOfMat[anchor][3]
				listOfMat[anchor][1], listOfMat[anchor][2], listOfMat[anchor][3] = listOfMat[anchorRight][3], listOfMat[anchorRight][7], listOfMat[anchorRight][6]
				listOfMat[anchorRight][3], listOfMat[anchorRight][7], listOfMat[anchorRight][6] = listOfMat[anchorLeft][6], listOfMat[anchorLeft][5], listOfMat[anchorLeft][1]
				listOfMat[anchorLeft][6], listOfMat[anchorLeft][5], listOfMat[anchorLeft][1] = first, second, third

	for row in listOfMat:
		print(*row)


originalRubik(listOfMat, loiGiaiGoc)