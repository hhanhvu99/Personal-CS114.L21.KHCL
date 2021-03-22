
xxx, yy = input().split()

xxx = int(xxx)
yy = int(yy)

D = 2
Dx = xxx*4 - yy
Dy = yy - 2*xxx

ga = round(Dx/D)
cho = round(Dy/D)

print(str(ga) + ' ' + str(cho))

