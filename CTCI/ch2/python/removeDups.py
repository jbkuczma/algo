'''
	write code to remove duplicates from an unsorted linked list
'''

from Node import LinkedList

def removeDups(li):
	currentNode = li.head
	seenNodes = []
	while currentNode != None:
		if currentNode.data in seenNodes:
			li.removeNode(currentNode.data)
		else:
			seenNodes.append(currentNode.data)
		currentNode = currentNode.getNext()


l = LinkedList()
l.addNode(6)
l.addNode(7)
l.addNode(7)
l.addNode(9)
l.printList()
removeDups(l)
l.printList()