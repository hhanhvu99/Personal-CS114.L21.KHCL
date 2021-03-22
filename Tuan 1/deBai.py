n = int(input())
k = int(input())
p = int(input())
q = int(input())

def oneDtoTwoD(number, length):
	return number//length, number%length

currentLocation = (p - 1) * 2 + q
idealLocationFirst = currentLocation - k
idealLocationSecond = currentLocation + k


if idealLocationFirst >= 1:
	index = oneDtoTwoD(idealLocationFirst-1, 2)
	u = index[0] + 1
	v = index[1] + 1
	print(str(u) + ' ' + str(v))

elif idealLocationSecond <= n:
	index = oneDtoTwoD(idealLocationSecond - 1, 2)
	u = index[0] + 1
	v = index[1] + 1
	print(str(u) + ' ' + str(v))

else:
	print('-1')