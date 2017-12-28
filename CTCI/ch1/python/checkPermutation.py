'''
	Given two strings, write a method to decide if one is a permutation of the other.
'''

def sortString(someString):
	return ''.join(sorted(someString))

def checkPermutation(str1, str2):

	if len(str1) != len(str2):
		return False

	if sortString(str1) != sortString(str2):
		return False
		
	return True

string1 = 'dog'
string2 = 'god'
print(checkPermutation(string1, string2))
'''
	prints:
		> True
'''

string3 = 'Buffalo'
string4 = 'Bills'
print(checkPermutation(string3, string4))
'''
	prints:
		> False
'''

