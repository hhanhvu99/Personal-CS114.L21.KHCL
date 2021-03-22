n = int(input())
listOfInput = input().split()

for index, value in enumerate(listOfInput):
	listOfInput[index] = int(value)

k, x = input().split()
k = int(k)
x = int(x)

def binary_search(arr, n, x):
	low = 0
	high = n - 1

	while low <= high:
		if arr[high] <= x:
			return high
		if arr[low] > x:
			return low

		mid = (high + low) // 2

		if arr[mid] < x:
			low = mid + 1

		elif arr[mid] > x:
			high = mid - 1

		else:
			return mid


def printKclosest(arr, x, k, n):
	listOfResult = []

	l = binary_search(arr, n, x)
	r = l + 1
	count = 0


	#So sánh khoảng cách
	while (l >= 0 and r < n and count < k):

		if (x - arr[l] <= arr[r] - x):
			listOfResult.append(arr[l])
			l -= 1
		else:
			listOfResult.append(arr[r])
			r += 1
		count += 1

	#In bên trái
	while (count < k and l >= 0):
		reverse = True
		listOfResult.append(arr[l])
		l -= 1
		count += 1

	#In bên phải
	while (count < k and r < n):
		listOfResult.append(arr[r])
		r += 1
		count += 1

	listOfResult.sort()

	return listOfResult

result = printKclosest(listOfInput, x, k, n)
print(*result, end=' ')