from sys import stdin, stdout
import bisect

n = int(input())
listOfInput = stdin.readline().split()

for index, value in enumerate(listOfInput):
	listOfInput[index] = int(value)


def printKclosest(arr, x, k):
	n = len(arr)

	if x >= arr[n-1]:
		return arr[n-k], arr[n-1]
	if x <= arr[0]:
		return arr[0], arr[k-1]

	smallest = float('inf')
	highest = float('-inf')

	l = bisect.bisect_left(arr, x, 0, len(arr))

	r = l + 1
	count = 0

	# So sánh khoảng cách
	while l >= 0 and r < n and count < k:
		if x - arr[l] <= arr[r] - x:
			if arr[l] > highest:
				highest = arr[l]
			if arr[l] < smallest:
				smallest = arr[l]
			l -= 1
		else:
			if arr[r] > highest:
				highest = arr[r]
			if arr[r] < smallest:
				smallest = arr[r]
			r += 1
		count += 1

	# In bên trái
	while count < k and l >= 0:
		smallest = arr[l]
		l -= 1
		count += 1

	# In bên phải
	while count < k and r < n:
		highest = arr[r]
		r += 1
		count += 1

	return smallest, highest


inputString = stdin.readline()
while inputString:
	k, x = inputString.split()
	k = int(k)
	x = int(x)

	low, high = printKclosest(listOfInput, x, k)
	stdout.write(str(low) + ' ' + str(high) + '\n')

	inputString = stdin.readline().strip()