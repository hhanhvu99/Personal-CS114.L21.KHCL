m, n, a = input().split()

tongGach = 0

m = int(m)
n = int(n)
a = int(a)

gachOne = m//a
gachTwo = n//a

if m % a != 0 and m > a:
	gachOne += 1
if n % a != 0 and n > a:
	gachTwo += 1

if gachOne == 0:
	gachOne = 1

if gachTwo == 0:
	gachTwo = 1

tongGach += gachOne * gachTwo

print(tongGach)