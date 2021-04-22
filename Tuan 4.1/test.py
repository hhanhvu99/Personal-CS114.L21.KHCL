import textwrap
import re

text = input()
listText = text.split()
listOfSpace = re.findall(r'[\s]+', text)
a = int(input())


if text[0] == ' ':
	a = 4/0