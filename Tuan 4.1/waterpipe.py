import collections

N = int(input())
listOfTramBom = []
banDo = []
totalCross = 0

for row in range(N):
	inputString = input()
	temp = []

	for col, character in enumerate(inputString):
		if character.isalpha():
			if character.islower():
				listOfTramBom.append((character, row, col, "None", 0))

		temp.append(character)

	banDo.append(temp)


def GetAvailablePath(type, direction):
	''' Return up, down, left, right '''

	if type == "0":
		return [False, False, False, False]
	elif type == "1":
		return [True, True, False, False]
	elif type == "2":
		return [False, False, True, True]
	elif type == "3":
		return [False, True, False, True]
	elif type == "4":
		return [False, True, True, False]
	elif type == "5":
		return [True, False, True, False]
	elif type == "6":
		return [True, False, False, True]
	elif type[0] == "7":
		if direction == "doc":
			return [True, True, False, False]
		elif direction == "ngang":
			return [False, False, True, True]
		else:
			return [True, True, True, True]
	else:
		return [True, True, True, True]


def GetSuccessor(banDo, currentNode, exploredSet):
	# (Tên trạm, posRow, posCol, ngang hay dọc, số ô có nước)
	# Node = ("A", 7, 8, "None", 9)

	global totalCross

	up = (currentNode[1] - 1, currentNode[2], "None")
	down = (currentNode[1] + 1, currentNode[2], "None")
	left = (currentNode[1], currentNode[2] - 1, "None")
	right = (currentNode[1], currentNode[2] + 1, "None")

	row = len(banDo)
	col = len(banDo[0])

	''' Return up, down, left, right '''
	currentAvailablePath = GetAvailablePath(banDo[currentNode[1]][currentNode[2]], currentNode[3])
	listToReturn = []

	''' UP '''
	if up[0] >= 0 and currentAvailablePath[0]:
		newAvailablePath = GetAvailablePath(banDo[up[0]][up[1]], up[2])
		if newAvailablePath[1]:
			if banDo[up[0]][up[1]][0] == "7":
				newState = (currentNode[0], up[0], up[1])
				if newState not in exploredSet:
					listToReturn.append((currentNode[0], up[0], up[1], "doc", currentNode[4] + 1))

					if banDo[up[0]][up[1]] == "7":
						banDo[up[0]][up[1]] = "7a"
					elif banDo[up[0]][up[1]] == "7a":
						banDo[up[0]][up[1]] = "7b"
						totalCross += 1
			else:
				newState = (currentNode[0], up[0], up[1])
				if newState not in exploredSet:
					listToReturn.append((currentNode[0], up[0], up[1], "None", currentNode[4] + 1))
	''' DOWN '''
	if down[0] < row and currentAvailablePath[1]:
		newAvailablePath = GetAvailablePath(banDo[down[0]][down[1]], down[2])
		if newAvailablePath[0]:
			if banDo[down[0]][down[1]][0] == "7":
				newState = (currentNode[0], down[0], down[1])
				if newState not in exploredSet:
					listToReturn.append((currentNode[0], down[0], down[1], "doc", currentNode[4] + 1))

					if banDo[down[0]][down[1]] == "7":
						banDo[down[0]][down[1]] = "7a"
					elif banDo[down[0]][down[1]] == "7a":
						banDo[down[0]][down[1]] = "7b"
						totalCross += 1
			else:
				newState = (currentNode[0], down[0], down[1])
				if newState not in exploredSet:
					listToReturn.append((currentNode[0], down[0], down[1], "None", currentNode[4] + 1))

	''' LEFT '''
	if left[1] >= 0 and currentAvailablePath[2]:
		newAvailablePath = GetAvailablePath(banDo[left[0]][left[1]], left[2])
		if newAvailablePath[3]:
			if banDo[left[0]][left[1]][0] == "7":
				newState = (currentNode[0], left[0], left[1])
				if newState not in exploredSet:
					listToReturn.append((currentNode[0], left[0], left[1], "ngang", currentNode[4] + 1))

					if banDo[left[0]][left[1]] == "7":
						banDo[left[0]][left[1]] = "7a"
					elif banDo[left[0]][left[1]] == "7a":
						banDo[left[0]][left[1]] = "7b"
						totalCross += 1
			else:
				newState = (currentNode[0], left[0], left[1])
				if newState not in exploredSet:
					listToReturn.append((currentNode[0], left[0], left[1], "None", currentNode[4] + 1))

	''' RIGHT '''
	if right[1] < col and currentAvailablePath[3]:
		newAvailablePath = GetAvailablePath(banDo[right[0]][right[1]], right[2])
		if newAvailablePath[2]:
			if banDo[right[0]][right[1]][0] == "7":
				newState = (currentNode[0], right[0], right[1])
				if newState not in exploredSet:
					listToReturn.append((currentNode[0], right[0], right[1], "ngang", currentNode[4] + 1))

					if banDo[right[0]][right[1]] == "7":
						banDo[right[0]][right[1]] = "7a"
					elif banDo[right[0]][right[1]] == "7a":
						banDo[right[0]][right[1]] = "7b"
						totalCross += 1
			else:
				newState = (currentNode[0], right[0], right[1])
				if newState not in exploredSet:
					listToReturn.append((currentNode[0], right[0], right[1], "None", currentNode[4] + 1))


	return listToReturn


def BFS(banDo, listOfTramBom):
	totalWaterBeforeLeak = 0

	foundLeak = False
	foundWrongConnect = False

	frontier = collections.deque()
	exploredSet = set()
	goalState = {}
	resultPath = []
	wrongPath = None

	for tram in listOfTramBom:
		frontier.append(tram)
		goalState[tram[0]] = False

	# (Tên trạm, posRow, posCol, ngang hay dọc, số ô có nước)
	# Node = ("A", 7, 8, "None", 9)
	while frontier:
		node = frontier.popleft()
		state = (node[0], node[1], node[2])

		if banDo[node[1]][node[2]].isupper():
			''' Cùng trạm bơm hay không '''
			if node[0].upper() == banDo[node[1]][node[2]]:
				goalState[node[0]] = True
				resultPath.append((node[0], node[1], node[2], node[3], node[4] - 1))
			else:
				foundWrongConnect = True
				wrongPath = (node[0], node[1], node[2], node[3], node[4] - 1)
				break
			continue

		if state not in exploredSet:
			exploredSet.add(state)
			successorList = GetSuccessor(banDo, node, exploredSet)

			if len(successorList) == 0 and node[4] != 0:
				foundLeak = True
				wrongPath = node
				break

			for successor in successorList:
				frontier.append(successor)

	if False in goalState.values() or foundWrongConnect or foundLeak:
		if wrongPath:
			totalWaterBeforeLeak = wrongPath[4] * (len(frontier)+1) - totalCross

		for path in resultPath:
			totalWaterBeforeLeak += path[4]

		return "-" + str(totalWaterBeforeLeak)
	else:
		total = -totalCross
		for path in resultPath:
			total += path[4]

		return str(total)


print(BFS(banDo, listOfTramBom))