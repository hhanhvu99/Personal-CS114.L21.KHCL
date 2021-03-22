stringList = input().lower()

nguyenAm = {'a', 'o', 'y', 'e', 'u', 'i'}
listResult = []

for i in stringList:
	if i in nguyenAm:
		continue
	else:
		listResult.append('.' + i)

print(''.join(listResult))