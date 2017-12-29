'''
	Implement a function to check if a linked list is a palindrome
'''

from Node import LinkedList


def check(s):
	start = 0
	end = len(s) - 1
	while start != end:
		if start - end == 1:
			break
		if s[start] == s[end]:
			start+=1
			end-=1
		else:
			return False
	return True


def isPalindrome(li):
	currentNode = li.head
	seen = ''
	while currentNode != None:
		seen += str(currentNode.data)
		currentNode = currentNode.getNext()
	return check(seen)


l = LinkedList()
l.addNode(9)
l.addNode(7)
l.addNode(5)
l.addNode(8)
l.addNode(9)
print(isPalindrome(l))

'''
	prints:
		False
'''

l2 = LinkedList()
l2.addNode(9)
l2.addNode(8)
l2.addNode(5)
l2.addNode(8)
l2.addNode(9)
print(isPalindrome(l2))

'''
	prints:
		True
'''




