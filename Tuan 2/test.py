from sys import stdin, stdout

n1, m1 = stdin.readline().split()
n2, m2 = stdin.readline().split()

n1, m1 = int(n1), int(m1)
n2, m2 = int(n2), int(m2)

if n1 * m1 != n2 * m2:
	for j in range(n1):
		data = stdin.readline().split()
		print(*data)
else:
	holder = []

	for j in range(n1):
		data = stdin.readline().split()
		holder += data
		length = len(holder)

		if length % m2 == 0:
			index = 0
			endIndex = length - m2

			while index <= endIndex:
				nextIndex = index + m2
				print(*holder[index:nextIndex], end=' ')
				stdout.write('\n')
				index = nextIndex

			holder = []

	'''index = 0
	endIndex = len(holder) - m2

	while index <= endIndex:
		nextIndex = index + m2
		print(*holder[index:nextIndex], end=' ')
		stdout.write('\n')
		index = nextIndex'''


