from sys import stdin, stdout
from collections import deque

binaryTree = None

class Node:
	__slots__ = ['left', 'right', 'data']
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


def printLeaf(root):
	queue = deque()
	queue.append(root)
	leaf = 0

	while queue:
		node = queue.popleft()
		count = 0

		if node:
			if node.left is None:
				count += 1
			else:
				queue.append(node.left)

			if node.right is None:
				count += 1
			else:
				queue.append(node.right)

			if count == 2:
				leaf += 1

	return leaf


while True:
	inputLine = stdin.readline().strip()

	if not inputLine:
		continue

	if inputLine == '0':
		break

	data = int(inputLine)
	binary_insert(binaryTree, data)

print(printLeaf(binaryTree))