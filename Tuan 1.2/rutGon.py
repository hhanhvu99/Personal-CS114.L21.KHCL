import math

n = int(input())
listOfInput = []

for i in range(n):
	a, b = input().split()
	a = int(a)
	b = int(b)
	listOfInput.append((a, b))

for fraction in listOfInput:
	numOne = fraction[0]
	numTwo = fraction[1]
	common = math.gcd(numOne, numTwo)

	numOne = numOne // common
	numTwo = numTwo // common

	print(numOne, end=' ')
	if numTwo != 1:
		print(numTwo)
	else:
		print()