s = input().strip()
try:
	n = int(input())
except:
	n = 83


while len(s) != 0:
	if len(s) <= n:
		print(s)
		exit(0)
	if s.find(' ') == -1:
		print(s)
		exit(0)
	else:
		if s[n] != ' ':
			tmp = s[:n]
			pos_space = tmp.rfind(' ')
			if pos_space != -1:
				print(tmp[:pos_space + 1])
				s = tmp[pos_space + 1:] + s[n:]
			else:
				tmp = s
				pos_space = tmp.find(' ')
				if pos_space != -1:
					print(tmp[:pos_space + 1])
					s = tmp[pos_space + 1:]

					if s[0] == ' ':
						s = s[1:]

				else:
					s = tmp
		else:
			print(s[:n])
			s = s[n:]