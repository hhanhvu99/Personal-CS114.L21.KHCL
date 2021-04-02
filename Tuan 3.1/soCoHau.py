n, m = input().split()
lengthN = len(n)
lengthM = len(m)
n = int(n)
m = int(m)

different = int(pow(10, lengthN))

count = ((m-n) // different) + 1

print(count)
