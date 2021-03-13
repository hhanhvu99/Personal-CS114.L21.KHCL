import math

a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
	dienTich = 0.0
	if a**2 + b**2 == c**2:
		dienTich = 1/2 * a*b
		if dienTich.is_integer():
			print('Tam giac vuong, dien tich = ' + str(int(dienTich)))
		else:
			print('Tam giac vuong, dien tich = ' + str(round(dienTich, 2)))

	elif a == b and b == c:
		dienTich = a**2 * math.sqrt(3)/4
		if dienTich.is_integer():
			print('Tam giac deu, dien tich = ' + str(int(dienTich)))
		else:
			print('Tam giac deu, dien tich = ' + str(round(dienTich, 2)))

	elif a == b or b == c:
		p = (a + b + c)/2
		dienTich = math.sqrt(p*(p-a)*(p-b)*(p-c))
		if dienTich.is_integer():
			print('Tam giac can, dien tich = ' + str(int(dienTich)))
		else:
			print('Tam giac can, dien tich = ' + str(round(dienTich, 2)))

	else:
		p = (a + b + c) / 2
		dienTich = math.sqrt(p * (p - a) * (p - b) * (p - c))
		if dienTich.is_integer():
			print('Tam giac thuong, dien tich = ' + str(int(dienTich)))
		else:
			print('Tam giac thuong, dien tich = ' + str(round(dienTich, 2)))

else:
	print('Khong phai tam giac')