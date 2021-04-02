from sys import stdin, stdout
import bisect

def findClosestElements(arr, k, x):
	i = bisect.bisect_left(arr, x)
	left, right = i-1, i
	length = len(arr)
	while k:
		if right >= length or (left >= 0 and abs(arr[left]-x) <= abs(arr[right]-x)):
			left -= 1
		else:
			right += 1
		k -= 1
	return arr[left+1], arr[right-1]


n = int(input())
listOfInput = stdin.readline().split()

for index, value in enumerate(listOfInput):
	listOfInput[index] = int(value)


inputString = stdin.readline()
while inputString:
	k, x = inputString.split()
	k = int(k)
	x = int(x)

	low, high = findClosestElements(listOfInput, k, x)
	stdout.write(str(low) + ' ' + str(high) + '\n')

	inputString = stdin.readline().strip()