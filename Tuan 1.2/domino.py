M, N = input().split()
M = int(M)
N = int(N)

tongSoChieu = M * N

if tongSoChieu % 2 == 0:
	print(tongSoChieu//2)
else:
	print((tongSoChieu-1)//2)