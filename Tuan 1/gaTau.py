k, t = input().split()
k = int(k)
t = int(t)

if k < t:
	result = t//k
	if result % 2 != 0:
		print(k - t%k)
	else:
		print(t%k)
elif k == t:
	print(k)
else:
	print(t)