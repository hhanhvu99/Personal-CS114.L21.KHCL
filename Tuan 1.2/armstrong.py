n = int(input())
temp = n
tong = 0
i = 0

length = len(str(n))

while i < length:
	number = temp % 10
	temp = temp // 10

	tong += number**length

	i += 1

if tong == n:
	print('True')
else:
	print('False')
