
height, width = input().split()
height = int(height)
width = int(width)
array = []

for i in range(height):
	array += input().split()


top, left, bottom, right = input().split()
top = int(top)
left = int(left)
right = int(right)
bottom = int(bottom)

result = ['0' for i in range(width*height)]

for j in range(top, bottom+1):
	start = j * width + left
	end = j * width + right

	result[start:end+1] = array[start:end+1]

i = 0
for j in range(height):
	print(*result[i:i+width])
	i = i + width


