row, col, actionLen = input().split()
row = int(row)
col = int(col)
actionLen = int(actionLen)
emptyStringList = []

initialHead = [0, 0]
snakeSpaceMatrix = []
snakeBody = []
turnDict = {}
arrowDirection = ""
checkTail = True


class Snake(object):
	def __init__(self, body, turnDict, arrowDirection, row, col):
		self.row = row
		self.col = col

		self.body = body
		self.head = body[0]
		self.length = len(body)
		self.oldPos = self.head[:]

		self.turnDict = turnDict
		self.directionX = self.turnDict[tuple(self.head)][1]
		self.directionY = self.turnDict[tuple(self.head)][0]
		self.arrowText = arrowDirection

	def move(self, action):
		allowMove = False

		if action == 'F':
			allowMove = True

		elif action == 'L':
			if self.arrowText == "left":
				self.directionX = 0
				self.directionY = 1
				self.arrowText = "down"
			elif self.arrowText == "down":
				self.directionX = 1
				self.directionY = 0
				self.arrowText = "right"
			elif self.arrowText == "right":
				self.directionX = 0
				self.directionY = -1
				self.arrowText = "up"
			elif self.arrowText == "up":
				self.directionX = -1
				self.directionY = 0
				self.arrowText = "left"

		elif action == 'R':
			if self.arrowText == "left":
				self.directionX = 0
				self.directionY = -1
				self.arrowText = "up"
			elif self.arrowText == "up":
				self.directionX = 1
				self.directionY = 0
				self.arrowText = "right"
			elif self.arrowText == "right":
				self.directionX = 0
				self.directionY = 1
				self.arrowText = "down"
			elif self.arrowText == "down":
				self.directionX = -1
				self.directionY = 0
				self.arrowText = "left"
		self.turnDict[tuple(self.head)] = [self.directionY, self.directionX]

		if allowMove:
			for index, cube in enumerate(self.body):
				if index == 0:
					pos = cube[:]
					tailPos = self.body[-1]

					turn = self.turnDict[tuple(pos)]
					pos[0], pos[1] = pos[0] + turn[0], pos[1] + turn[1]

					if (tuple(pos) in self.turnDict and tuple(pos) != tuple(tailPos)) or pos[0] < 0 or pos[0] >= self.row or pos[1] < 0 or pos[1] >= self.col:
						return False

					cube[0], cube[1] = pos[0], pos[1]

					if self.length == 1:
						del self.turnDict[tuple(self.oldPos)]
						self.oldPos = self.head[:]

				elif index == self.length - 1:
					turn = self.turnDict[tuple(cube)]
					oldPos = cube[:]
					cube[0], cube[1] = cube[0] + turn[0], cube[1] + turn[1]

					del self.turnDict[tuple(oldPos)]

				else:
					turn = self.turnDict[tuple(cube)]
					cube[0], cube[1] = cube[0] + turn[0], cube[1] + turn[1]

		return True


def findOccurrences(string, rowNumber):
	global initialHead
	global turnDict
	global arrowDirection
	global emptyStringList
	global checkMatrix
	listReturn = []

	for i, letter in enumerate(string):
		if letter == '<':
			initialHead = [rowNumber, i]
			turnDict[tuple(initialHead)] = [0, -1]
			arrowDirection = "left"
		elif letter == '^':
			initialHead = [rowNumber, i]
			turnDict[tuple(initialHead)] = [-1, 0]
			arrowDirection = "up"
		elif letter == '>':
			initialHead = [rowNumber, i]
			turnDict[tuple(initialHead)] = [0, 1]
			arrowDirection = "right"
		elif letter == 'v':
			initialHead = [rowNumber, i]
			turnDict[tuple(initialHead)] = [1, 0]
			arrowDirection = "down"
		elif letter == '*':
			listReturn.append(i)

	return listReturn


for rowInput in range(row):
	snakeSpaceMatrix.append(findOccurrences(input(), rowInput))

for column in range(col):
	emptyStringList.append(".")

''' Lấy thân rắn '''
snakeBody.append(initialHead)
while True:
	currentPos = snakeBody[-1]

	upPos = [currentPos[0] - 1, currentPos[1]]
	downPos = [currentPos[0] + 1, currentPos[1]]
	leftPos = [currentPos[0], currentPos[1] - 1]
	rightPos = [currentPos[0], currentPos[1] + 1]

	''' LEFT '''
	if 0 <= leftPos[1]:
		if leftPos[1] in snakeSpaceMatrix[leftPos[0]]:
			if checkTail:
				if arrowDirection != "left":
					snakeBody.append(leftPos)
					snakeSpaceMatrix[leftPos[0]].remove(leftPos[1])
					turnDict[tuple(leftPos)] = [0, 1]
					checkTail = False
					continue
			else:
				snakeBody.append(leftPos)
				snakeSpaceMatrix[leftPos[0]].remove(leftPos[1])
				turnDict[tuple(leftPos)] = [0, 1]
				continue
	''' UP '''
	if 0 <= upPos[0]:
		if upPos[1] in snakeSpaceMatrix[upPos[0]]:
			if checkTail:
				if arrowDirection != "up":
					snakeBody.append(upPos)
					snakeSpaceMatrix[upPos[0]].remove(upPos[1])
					turnDict[tuple(upPos)] = [1, 0]
					checkTail = False
					continue
			else:
				snakeBody.append(upPos)
				snakeSpaceMatrix[upPos[0]].remove(upPos[1])
				turnDict[tuple(upPos)] = [1, 0]
				continue
	''' RIGHT '''
	if rightPos[1] < col:
		if rightPos[1] in snakeSpaceMatrix[rightPos[0]]:
			if checkTail:
				if arrowDirection != "right":
					snakeBody.append(rightPos)
					snakeSpaceMatrix[rightPos[0]].remove(rightPos[1])
					turnDict[tuple(rightPos)] = [0, -1]
					checkTail = False
					continue
			else:
				snakeBody.append(rightPos)
				snakeSpaceMatrix[rightPos[0]].remove(rightPos[1])
				turnDict[tuple(rightPos)] = [0, -1]
				continue
	''' DOWN '''
	if downPos[0] < row:
		if downPos[1] in snakeSpaceMatrix[downPos[0]]:
			if checkTail:
				if arrowDirection != "down":
					snakeBody.append(downPos)
					snakeSpaceMatrix[downPos[0]].remove(downPos[1])
					turnDict[tuple(downPos)] = [-1, 0]
					checkTail = False
					continue
			else:
				snakeBody.append(downPos)
				snakeSpaceMatrix[downPos[0]].remove(downPos[1])
				turnDict[tuple(downPos)] = [-1, 0]
				continue

	break


def printCurrentSnake(snake, row, alive):
	spaceMatrix = [emptyStringList[:] for i in range(row)]

	for index, cube in enumerate(snake.body):
		if alive:
			if index == 0:
				if snake.arrowText == "left":
					spaceMatrix[cube[0]][cube[1]] = "<"
				elif snake.arrowText == "up":
					spaceMatrix[cube[0]][cube[1]] = "^"
				elif snake.arrowText == "right":
					spaceMatrix[cube[0]][cube[1]] = ">"
				else:
					spaceMatrix[cube[0]][cube[1]] = "v"
			else:
				spaceMatrix[cube[0]][cube[1]] = "*"
		else:
			spaceMatrix[cube[0]][cube[1]] = "X"

	for listString in spaceMatrix:
		temp = ''.join(listString)
		print(temp)


snakeInTheBox = Snake(snakeBody, turnDict, arrowDirection, row, col)
stringOfAction = input()


def printMove(stringOfAction, snakeInTheBox):
	for action in stringOfAction:
		alive = snakeInTheBox.move(action)

		print(action)

		if not alive:
			printCurrentSnake(snakeInTheBox, row, alive)
			exit(0)
		printCurrentSnake(snakeInTheBox, row, alive)


def printFinalResult(stringOfAction, snakeInTheBox):
	for action in stringOfAction:
		alive = snakeInTheBox.move(action)
		if not alive:
			printCurrentSnake(snakeInTheBox, row, alive)
			exit(0)

	printCurrentSnake(snakeInTheBox, row, alive)


printFinalResult(stringOfAction, snakeInTheBox)