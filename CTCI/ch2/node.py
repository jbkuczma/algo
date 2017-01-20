class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, data):
		self.data = data

	def setNext(self, nextNode):
		self.next = nextNode


class LinkedList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def addNode(self, node):
		newNode = Node(node)
		newNode.setNext(self.head)
		self.head = newNode

	def getSize(self):
		currentNode = self.head
		count = 0
		while currentNode != None:
			count+=1
			currentNode = currentNode.getNext()

	def printList(self):
		currentNode = self.head
		output = ""
		while currentNode != None:
			output += str(currentNode.data)
			currentNode = currentNode.getNext()
			if currentNode != None:
				output += ' -> '
		print(output)

	def findNode(self, node):
		currentNode = self.head
		while currentNode != None:
			if currentNode.getData() == node:
				return True
			else:
				currentNode = currentNode.getNext()
		return False

	def removeNode(self, node):
		currentNode = self.head
		previousNode = None
		found = False
		while not found:
			if currentNode.getData() == node:
				found = True
			else:
				currentNode = currentNode.getNext()
		if previousNode == None:
			self.head = currentNode.getNext()
		else:
			previousNode.setNext(currentNode.getNext())


