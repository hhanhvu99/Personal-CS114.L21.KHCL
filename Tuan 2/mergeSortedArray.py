n1, n2 = input().split()
arr1 = input().split()
arr2 = input().split()

n1 = int(n1)
n2 = int(n2)

for index, value in enumerate(arr1):
	arr1[index] = int(value)
for index, value in enumerate(arr2):
	arr2[index] = int(value)

i = 0
j = 0
k = 0

while i < n1 and j < n2:
	if arr1[i] < arr2[j]:
		print(arr1[i], end=' ')
		k = k + 1
		i = i + 1
	else:
		print(arr2[j], end=' ')
		k = k + 1
		j = j + 1

while i < n1:
	print(arr1[i], end=' ')
	k = k + 1
	i = i + 1

while j < n2:
	print(arr2[j], end=' ')
	k = k + 1
	j = j + 1