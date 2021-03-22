from sys import stdin, stdout

class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None

class SLinkedList:
	def __init__(self):
		self.Head = None
		self.Tail = None
		self.Count = 0
		self.dictionary = {}

	def print(self):
		printval = self.Head
		while printval is not None:
			stdout.write(printval.value + ' ')
			printval = printval.next

	def appendleft(self, newdata):
		new_node = Node(newdata)

		if newdata not in self.dictionary:
			self.dictionary[newdata] = 1
		else:
			count = self.dictionary[newdata] + 1
			self.dictionary[newdata] = count

		temp = self.Head
		self.Head = new_node
		new_node.next = temp

		self.Count += 1
		if self.Count == 1:
			self.Tail = self.Head

	def append(self, newdata):
		new_node = Node(newdata)

		if newdata not in self.dictionary:
			self.dictionary[newdata] = 1
		else:
			count = self.dictionary[newdata] + 1
			self.dictionary[newdata] = count

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

		if newdata not in self.dictionary:
			self.dictionary[newdata] = 1
		else:
			count = self.dictionary[newdata] + 1
			self.dictionary[newdata] = count

		self.Count += 1

		if middle_node == self.Tail:
			self.Tail = new_node

	def search(self, x):
		if x not in self.dictionary:
			return -1

		current = self.Head
		while current is not None:
			if current.value == x:
				return current
			current = current.next

		return -1

	def remove(self, Removekey):
		if Removekey not in self.dictionary:
			return -1

		previous = None
		current = self.Head

		while current is not None:
			# A match is found!
			if current.value == Removekey:
				# We're in the middle or end of the list
				if previous is not None:
					previous.next = current.next
					# We're at the very end of the list
					if current.next is None:
						self.Tail = previous
					self.Count -= 1
				# We're at the very start of the list
				else:
					self.Head = self.Head.next
					self.Count -= 1
					if self.Count == 0:
						self.Tail = None

				count = self.dictionary[Removekey] - 1
				if count == 0:
					del self.dictionary[Removekey]
				else:
					self.dictionary[Removekey] = count

				return True

			previous = current
			current = current.next

		return -1

	def remove_all_value(self, RemoveKey):
		if RemoveKey not in self.dictionary:
			return -1

		previous = None
		current = self.Head

		while current is not None and RemoveKey in self.dictionary:
			# A match is found!
			if current.value == RemoveKey:
				# We're in the middle or end of the list
				if previous is not None:
					previous.next = current.next
					# We're at the very end of the list
					if current.next is None:
						self.Tail = previous
					self.Count -= 1
				# We're at the very start of the list
				else:
					self.Head = self.Head.next
					self.Count -= 1
					if self.Count == 0:
						self.Tail = None

				current = current.next

				count = self.dictionary[RemoveKey] - 1
				if count == 0:
					del self.dictionary[RemoveKey]
				else:
					self.dictionary[RemoveKey] = count

			else:
				previous = current
				current = current.next


	def popleft(self):
		if self.Count > 0:
			key = self.Head.value
			self.Head = self.Head.next
			self.Count -= 1
			if self.Count == 0:
				self.Tail = None

			count = self.dictionary[key] - 1
			if count == 0:
				del self.dictionary[key]
			else:
				self.dictionary[key] = count

	def isEmpty(self):
		if self.Count == 0:
			return True
		return False

linkedList = SLinkedList()

while True:
	element = stdin.readline().split()
	option = element[0]

	# Thêm đầu
	if option == '0':
		linkedList.appendleft(element[1])
	# Thêm đuôi
	elif option == '1':
		linkedList.append(element[1])
	# Tìm a trong list, thêm b vào sau
	elif option == '2':
		a = element[1]
		b = element[2]

		firstNode = linkedList.search(a)

		if firstNode != -1:
			linkedList.insert(firstNode, b)
		else:
			linkedList.appendleft(b)
	# Tìm số n đầu tiên trong danh sách và xóa nó
	elif option == '3':
		if not linkedList.isEmpty():
			linkedList.remove(element[1])

	# Xóa mọi số n khỏi danh sách
	elif option == '4':
		linkedList.remove_all_value(element[1])

	# Xóa số đầu tiên trong danh sách
	elif option == '5':
		if not linkedList.isEmpty():
			linkedList.popleft()
	else:
		break


if linkedList.isEmpty():
	stdout.write('blank')
else:
	linkedList.print()
