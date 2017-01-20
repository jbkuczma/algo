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

