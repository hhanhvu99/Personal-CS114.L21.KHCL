chuoiMot = input()
chuoiHai = input()

if len(chuoiMot) == len(chuoiHai):
	length = len(chuoiHai) - 1
	for index, valueOne in enumerate(chuoiMot):
		if valueOne != chuoiHai[length - index]:
			print('NO')
			exit(0)
	print('YES')
else:
	print('NO')