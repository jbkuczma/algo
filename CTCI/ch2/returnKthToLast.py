'''
	Implement an algorithm to find the Kth to last element of a singly linked list
'''

from node import LinkedList

def returnKthLastElement(ll, index):
	linkedListLength = ll.getSize()
	current = 0
	wantedIndex = linkedListLength - index
	currentNode = ll.head
	while currentNode != None:
		if current == wantedIndex:
			return currentNode.data
		else:
			current+=1
			currentNode = currentNode.getNext()

ll = LinkedList()
ll.addNode(1)
ll.addNode(13)
ll.addNode(41)
ll.addNode(8)
ll.addNode(0)
ll.addNode(100)
ll.addNode(56)
ll.addNode(99)
print(returnKthLastElement(ll, 2))

'''
	prints:
		> 13
'''