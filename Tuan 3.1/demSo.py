from sys import stdin, stdout

q = int(stdin.readline())

for i in range(q):
	n, k = stdin.readline().split()
	n = int(n)
	k = int(k)

	dictionary = {}

	tempInput = stdin.readline().split()

	for j in range(n):
		temp = int(tempInput[j])

		if temp not in dictionary:
			dictionary[temp] = 1
		else:
			dictionary[temp] = dictionary[temp] + 1

	if k in dictionary:
		stdout.write(str(dictionary[k]) + '\n')
	else:
		stdout.write('0\n')