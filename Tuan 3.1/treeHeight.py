from sys import stdin, stdout
from collections import deque

binaryTree = None

class NodeTree:
	__slots__ = ['left', 'right', 'data']
	def __init__(self, val):
		self.left = None
		self.right = None
		self.data = val

class Node:
	__slots__ = ['value', 'next']
	def __init__(self, value=None):
		self.value = value
		self.next = None

class SLinkedList:
	def __init__(self):
		self.Head = None
		self.Tail = None
		self.Count = 0

	def print(self):
		printval = self.Head
		while printval is not None:
			stdout.write(printval.value + ' ')
			printval = printval.next

	def appendleft(self, newdata):
		new_node = Node(newdata)

		temp = self.Head
		self.Head = new_node
		new_node.next = temp

		self.Count += 1
		if self.Count == 1:
			self.Tail = self.Head

	def append(self, newdata):
		new_node = Node(newdata)

		if self.Count == 0:
			self.Head = new_node
		else:
			self.Tail.next = new_node
		self.Tail = new_node
		self.Count += 1

	def insert(self, middle_node, newdata):
		if middle_node is None:
			return

		new_node = Node(newdata)
		new_node.next = middle_node.next
		middle_node.next = new_node

		self.Count += 1

		if middle_node == self.Tail:
			self.Tail = new_node

	def search(self, x):
		current = self.Head
		while current is not None:
			if current.value == x:
				return current
			current = current.next

		return -1

	def popleft(self):
		if self.Count > 0:
			key = self.Head.value
			self.Head = self.Head.next
			self.Count -= 1
			if self.Count == 0:
				self.Tail = None

			return key

	def isEmpty(self):
		if self.Count == 0:
			return True
		return False


''' Danh sách liên kết '''
linkedList = SLinkedList()
while True:
	element = stdin.readline().split()

	if not element:
		continue

	option = element[0]

	# Thêm đầu
	if option == '0':
		linkedList.appendleft(int(element[1]))
	# Thêm đuôi
	elif option == '1':
		linkedList.append(int(element[1]))
	# Tìm a trong list, thêm b vào sau
	elif option == '2':
		a = int(element[1])
		b = int(element[2])

		firstNode = linkedList.search(a)

		if firstNode != -1:
			linkedList.insert(firstNode, b)
		else:
			linkedList.appendleft(b)
	# Kết thúc
	else:
		break


''' Cây nhị phân '''
def binary_insert(root, key):
	global binaryTree

	newnode = NodeTree(key)

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


def findHeight(root):
	queue = deque()
	queue.append(root)
	height = 0

	while True:
		nodeCount = len(queue)
		if nodeCount == 0:
			return height

		height += 1

		while nodeCount > 0:
			node = queue.popleft()

			if node.left is not None:
				queue.append(node.left)
			if node.right is not None:
				queue.append(node.right)

			nodeCount -= 1


while True:
	inputLine = linkedList.popleft()

	if inputLine is not None:
		data = inputLine
		binary_insert(binaryTree, data)
	else:
		break

print(findHeight(binaryTree))


