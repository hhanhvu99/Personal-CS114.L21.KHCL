import math

n = int(input())

def printUocSo(n):
	i = 1
	tong = 0

	while i <= math.sqrt(n):
		remainder = int(n % i)

		if remainder == 0:
			result = n // i

			if result == i:
				tong += i
			else:
				tong += i + result

		i += 1

	return tong - n

print(printUocSo(n))
