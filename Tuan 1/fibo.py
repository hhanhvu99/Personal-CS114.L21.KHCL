x = int(input())
n1, n2 = 0, 1
count = 0

if 1 <= x <= 30:
	while count <= x:
		if count == x:
			print(n1)
			break
		else:
			soThuN = n1 + n2

			n1 = n2
			n2 = soThuN
			count += 1

else:
	print("So " + str(x) + " khong nam trong khoang [1,30].")