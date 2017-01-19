'''
	Implement an algorithm to determine if a string has all unique characters.
	What if you can use can't use additional data structures.
'''

def isUnique(inputString):
	lettersSeen = []
	for letter in inputString:
		if letter not in lettersSeen:
			lettersSeen.append(letter)
		else:
			return False

	return True

s = 'Buffalo'
t = 'Raptors'

print(isUnique(s))
print(isUnique(t))

'''
	prints:
		> False
		> True
'''

def isUnique_NoExtraDataStructures(inputString):
	# To Do
	print(inputString)