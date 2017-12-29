'''
	Implement an algorithm to delete a node in the middle (any node but the first and last node, not necessarily the exact middle)
    of a singly linked list given only access to that node

    ex: given node c in a->b->c->d->e->f
    result:             a->b->d->e->f
'''

from Node import LinkedList, Node

def deleteMiddleNode(linkedList, node):
    # check to see if the node is in the linked list
    if linkedList.findNode(node):
        # get the data for the node
        nodeToDelete = Node(None)
        nodeToCheck = linkedList.head

        while nodeToCheck != None:
            if nodeToCheck.data == node:
                nodeToDelete.data = node
                nodeToDelete.next = nodeToCheck.getNext()
                break
            nodeToCheck = nodeToCheck.getNext()
            
        # check to make sure the node isn't the first or last node
        if  linkedList.head.data != node and nodeToDelete.next != None:
            linkedList.removeNode(node)

l = LinkedList()
l.addNode(9)
l.addNode(7)
l.addNode(5)
l.addNode(8)
l.addNode(10)
l.printList()
deleteMiddleNode(l, 9)
l.printList()