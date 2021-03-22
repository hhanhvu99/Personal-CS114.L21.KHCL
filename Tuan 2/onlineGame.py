dictionary = set()

while True:
	data = input().split()
	order = data[0]

	if order == '1':
		dictionary.add(data[1])
	elif order == '2':
		if data[1] in dictionary:
			print('1')
		else:
			print('0')
	else:
		exit(0)