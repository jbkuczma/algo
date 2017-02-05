'''
	Each linked list represents a number. Each node is a single digit and
	the digits are stored in reverse order. Write a function
	to add the two numbers.
'''

from node import LinkedList

def getNumber(ll):
	currentNode = ll.head
	number = ''
	while currentNode != None:
		number += str(currentNode.data)
		currentNode = currentNode.getNext()
	return int(number)

def sumLists(ll1, ll2):
	number1 = getNumber(ll1)
	number2  = getNumber(ll2)
	print(number1)
	print(number2)
	return number1 + number2

ll1 = LinkedList()
ll1.addNode(7)
ll1.addNode(1)
ll1.addNode(6)
ll2 = LinkedList()
ll2.addNode(5)
ll2.addNode(9)
ll2.addNode(2)
print(sumLists(ll1, ll2))
	