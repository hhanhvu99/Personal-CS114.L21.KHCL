from decimal import *

n = float(input())
getcontext().prec = 6

result = Decimal((n * 0.453592) / 2.54**2)

print(result.normalize())

