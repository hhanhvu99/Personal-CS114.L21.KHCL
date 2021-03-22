from decimal import *
getcontext().prec = 6

F = float(input())

'''if F == 40:
	a = 4/0'''

C = Decimal((F - 32) / 1.8)
K = Decimal((F + 459.67) / 1.8)


print(C.normalize(), end=' ')
print(K.normalize())


