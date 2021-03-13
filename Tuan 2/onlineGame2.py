from sys import stdin, stdout

dictionary = set()

while True:
	data = stdin.readline().split()

	if not data:
		continue

	order = data[0]

	if order == '1':
		dictionary.add(int(data[1]))

	elif order == '2':
		if int(data[1]) in dictionary:
			stdout.write('1\n')
		else:
			stdout.write('0\n')

	elif order == '3':
		dictionary.discard(int(data[1]))

	else:
		exit(0)