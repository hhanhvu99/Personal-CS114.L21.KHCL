from sys import stdin, stdout
from collections import deque

binaryTree = None

class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.data = val


def binary_insert(root, key):
	global binaryTree

	newnode = Node(key)

	x = root
	y = None

	while x:
		y = x
		if key < x.data:
			x = x.left
		elif key > x.data:
			x = x.right
		else:
			return

	if not y:
		y = newnode
	elif key < y.data:
		y.left = newnode
	elif key > y.data:
		y.right = newnode
	else:
		return

	if not root:
		binaryTree = y


def printBFS(root):
	queue = deque()
	queue.append(root)

	while queue:
		node = queue.popleft()

		if node:
			stdout.write(str(node.data) + ' ')
			queue.append(node.left)
			queue.append(node.right)


while True:
	inputLine = stdin.readline().strip()

	if not inputLine:
		continue

	if inputLine == '0':
		break

	data = int(inputLine)
	binary_insert(binaryTree, data)

printBFS(binaryTree)